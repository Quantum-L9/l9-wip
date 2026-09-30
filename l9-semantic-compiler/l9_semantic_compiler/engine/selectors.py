from __future__ import annotations
import re
from copy import deepcopy
from typing import Any
from .errors import SelectorError
_FIELD = r"[A-Za-z0-9_\-]+"
FILTER_EQUALITY = re.compile(
    rf"""
    ^\$\.
    (?P<collection>{_FIELD})
    \[
      \?\(
        @\.
        (?P<field>{_FIELD})
        ==
        "(?P<value>[^"]*)"
      \)
    \]
    $
    """,
    re.VERBOSE,
)
FILTER_CONTAINS = re.compile(
    rf"""
    ^\$\.
    (?P<collection>{_FIELD})
    \[
      \?\(
        @\.
        (?P<field>{_FIELD})
        \s+contains\s+
        "(?P<value>[^"]*)"
      \)
    \]
    $
    """,
    re.VERBOSE,
)
def select(
    document: Any,
    selector: str,
) -> Any:
    if selector == "$":
        return deepcopy(document)
    equality = FILTER_EQUALITY.match(
        selector
    )
    if equality:
        return _filter_collection(
            document=document,
            collection=equality.group(
                "collection"
            ),
            field=equality.group("field"),
            value=equality.group("value"),
            mode="equal",
        )
    contains = FILTER_CONTAINS.match(
        selector
    )
    if contains:
        return _filter_collection(
            document=document,
            collection=contains.group(
                "collection"
            ),
            field=contains.group("field"),
            value=contains.group("value"),
            mode="contains",
        )
    if not selector.startswith("$."):
        raise SelectorError(
            f"unsupported selector: {selector}"
        )
    tokens = selector[2:].split(".")
    return _walk(
        document,
        tokens,
        selector=selector,
    )
def _walk(
    current: Any,
    tokens: list[str],
    *,
    selector: str,
) -> Any:
    if not tokens:
        return deepcopy(current)
    token = tokens[0]
    remaining = tokens[1:]
    if token.endswith("[*]"):
        field = token[:-3]
        if not isinstance(current, dict):
            raise SelectorError(
                f"expected object while resolving {selector}"
            )
        collection = current.get(field)
        if not isinstance(collection, list):
            raise SelectorError(
                f"{field} is not an array in {selector}"
            )
        if not remaining:
            return deepcopy(collection)
        values: list[Any] = []
        for item in collection:
            try:
                values.append(
                    _walk(
                        item,
                        remaining,
                        selector=selector,
                    )
                )
            except SelectorError:
                continue
        return values
    if not isinstance(current, dict):
        raise SelectorError(
            f"expected object while resolving {selector}"
        )
    if token not in current:
        raise SelectorError(
            f"missing selector field {token} in {selector}"
        )
    return _walk(
        current[token],
        remaining,
        selector=selector,
    )
def _filter_collection(
    *,
    document: Any,
    collection: str,
    field: str,
    value: str,
    mode: str,
) -> list[Any]:
    if not isinstance(document, dict):
        raise SelectorError(
            "filter selector requires root object"
        )
    items = document.get(collection)
    if not isinstance(items, list):
        raise SelectorError(
            f"{collection} is not an array"
        )
    matched: list[Any] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        actual = item.get(field)
        if mode == "equal":
            if actual == value:
                matched.append(
                    deepcopy(item)
                )
        elif mode == "contains":
            if (
                isinstance(actual, list)
                and value in actual
            ):
                matched.append(
                    deepcopy(item)
                )
            elif (
                isinstance(actual, str)
                and value in actual
            ):
                matched.append(
                    deepcopy(item)
                )
    return matched
