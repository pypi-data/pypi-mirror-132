"""Utility that permits deeply accessing objects, defaulting to None on error.

    assert dn(1).get == 1
    assert dn("ASDF").lower().get == "asdf"
    assert dn(123).lower().get is None
    assert dn(123).lower().default("hi") == "hi"
    assert dn("ASDF").strip("F").get == "ASD"
    assert dn("").junk().get is None
    assert dn(3).real.get == 3
    assert dn({"asdf": ["a", "b", "c"]})["asdf"][1].get == "b"
    assert dn({"asdf": ["a", "b", "c"]})["asdf"][1].upper().get == "B"
    assert dn({"asdf": ["a", "b", "c"]})["fdas"][1].upper().get is None
    assert dn(3).fn(str).get == "3"
    assert dn({"a": "b"}).attr("get")("a").get == "b"
    assert dn(123).junk.fn(str).get is None
    assert dn(123).fn(str)
    assert not dn(123).fn(str).junk
    assert bool(dn(123).fn(str))
    assert not bool(dn(123).fn(str).junk.asdf)
    assert list(dn(1).junk) == []
    for x in dn({"x": [3]})["x"]:
        assert x == 3
    assert not any(dn("a").junk)
    assert any(dn([1]))
    assert dn("a") == "a"
    assert "a" == dn("a")
    assert dn("a").upper() == "A"
"""
from __future__ import annotations

import dataclasses
import functools
import logging
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable, List, Protocol, TypeVar, Union


class Action(Protocol):
    """A function that transforms a value to a new value based on a property."""

    def __call__(self, value: Any) -> Any:
        ...


@dataclasses.dataclass(frozen=True)
class CallAction(Action):
    """Action that calls a function on a value."""

    fn: Callable[[Any], Any]

    def __call__(self, value: Any) -> Any:
        return self.fn(value)


@dataclasses.dataclass(frozen=True)
class GetItemAction(Action):
    """Action that gets an item from a value."""

    item: Any

    def __call__(self, value: Any) -> Any:
        return value[self.item]


@dataclasses.dataclass(frozen=True)
class AttrAction(Action):
    """Action that gets an attribute from a value."""

    attr: str

    def __call__(self, value: Any) -> Any:
        return getattr(value, self.attr)


@dataclass(frozen=True)
class DeepNone:
    """Implementation of `dn` utility.

    Note: this class should not be instantiated directly. Use `dn` instead.

    Keeps a record of all actions applied to the origin `value` and utilities
    for applying more actions.

    The `DeepNone` object is not useful until its result is "built". There are
    several ways of getting the built value:

    * `get`: returns the built value
    * `default`: returns the built value or the default value
    * bool(DeepNone_object): returns the truthiness of the built value
    """

    value: Any
    actions: List[Action] = field(default_factory=list)

    def __bool__(self) -> bool:
        """Returns the truthiness of the built value. Convenient when you only
        care about the presence of a deep-property."""
        return bool(self.get)

    def __iter__(self) -> Iterable:
        """Materializes this as an iterable, defaulting to empty list."""
        return self.fn(iter).default(iter([]))

    def __eq__(self, __o: object) -> bool:
        """Equality method.

        Returns dict-equality if `__o` is `DeepNone`, else compares `self.get` to
        `__o`."""
        if isinstance(__o, DeepNone):
            return self._eq_value == __o._eq_value
        return self.get == __o

    @property
    def _eq_value(self) -> dict:
        return dataclasses.asdict(self)

    def __hash__(self) -> int:
        """Returns hash of dict value."""
        return hash(self._eq_value)

    @functools.cached_property
    def get(self) -> Any:
        """Returns the built value.

        Applies all actions to `value`, returning`None` on failure.
        """
        result = self.value
        for action in self.actions:
            try:
                result = action(result)
            except Exception as e:
                logging.debug(
                    f"Failed to apply action {action} to {result} for dn {self}",
                    exc_info=e,
                )
                return None
        return result

    def default(self, default: T) -> Union[T, Any]:
        """Returns the built value or the default value if falsey."""
        return self.get or default

    @functools.cached_property
    def or_first(self) -> Any:
        """Returns self.default(self.value)"""
        return self.default(self.value)

    def fn(self, function: Callable[[Any], Any]) -> DeepNone:
        """Transforms this by passing current value to `function`.

        I.e., runs function(value) as new `DeepNone` result.
        """
        return self._add(CallAction(function))

    def attr(self, attr: str) -> DeepNone:
        """Safety-hatch for accessing field conflicting with API keywords.

        I.e., if you want to access the attribute `default` on `value`, the
        `default` API keyword does not permit `my_value.default` access.
        Instead, you can use this method `myvalue.attr('default')`.
        """
        return self._add(AttrAction(attr))

    def __getitem__(self, item_key) -> DeepNone:
        """Transforms this by accessing `value[item_key]`."""
        return self._add(GetItemAction(item_key))

    def __getattr__(self, attribute_name) -> DeepNone:
        """Transforms this by returning `my_value.<attribute_name>`."""
        return self._add(AttrAction(attribute_name))

    def __call__(self, *args: Any, **kwds: Any) -> DeepNone:
        """Transforms this by invoking `my_value` and passing args."""
        return self._add(CallAction(lambda x: x(*args, **kwds)))

    def _add(self, action: Action) -> DeepNone:
        """Returns new instance by adding `action` to current value."""
        return self.__class__(self.value, [*self.actions, action])

    @classmethod
    def make(cls, value: Any) -> DeepNone:
        """Returns new instance with `value` as origin.

        If value is already a `DeepNone` instance, returns it.
        """
        return value if isinstance(value, cls) else cls(value)


T = TypeVar("T")


def dn(value: T) -> Union[T, DeepNone]:
    """Returns a new `DeepNone` object for `value`.

    If `value` is already a `DeepNone` object, returns it.

    assert dn(1).get == 1
    assert dn("ASDF").lower().get == "asdf"
    assert dn(123).lower().get is None
    assert dn(123).lower().default("hi") == "hi"
    assert dn("ASDF").strip("F").get == "ASD"
    assert dn("").junk().get is None
    assert dn(3).real.get == 3
    assert dn({"asdf": ["a", "b", "c"]})["asdf"][1].get == "b"
    assert dn({"asdf": ["a", "b", "c"]})["asdf"][1].upper().get == "B"
    assert dn({"asdf": ["a", "b", "c"]})["fdas"][1].upper().get is None
    assert dn(3).fn(str).get == "3"
    assert dn({"a": "b"}).attr("get")("a").get == "b"
    assert dn(123).junk.fn(str).get is None
    assert dn(123).fn(str)
    assert not dn(123).fn(str).junk
    assert bool(dn(123).fn(str))
    assert not bool(dn(123).fn(str).junk.asdf)
    """
    return DeepNone.make(value)
