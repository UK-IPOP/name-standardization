"""This module contains the ruleset for standardizing names.

Each rule is enforced by a function.

In order to maintain separation of concerns, each rule has its own function.

Then, if deemed relevant, utility functions/classes may be written to combine similar rules.
"""

HONORIFICS = {
    "Mr.",
    "Mrs.",
    "Ms.",
    "Miss",
}
"""Set of honorofics."""


# TODO: all of these should have double capitals, so title_case function doesn't work...
ACADEMIC_TITLES = {
    "Dr.",
    "Ph.D.",
    "M.D.",
    "M.S.",
    "M.A.",
    "B.A.",
    "B.S.",
}
"""Set of academic titles from doctorate to bachelors."""

SUFFIXES = {
    "Jr.",
    "Sr.",
    "II",  # TODO: Is this an "eye" or a "bar"?
    "III"
}


def title_case(name: str) -> str: return name.title()
"""Title cases the name.

Capitalizes the first letter of each word.

Args:
    name: String to strip periods from.

Returns:
    str: Title-cased string.
"""


def strip_periods(name: str) -> str: return name.replace(".", "")
"""Strips periods from the string.

This is particularly useful for standardizing prefixes and suffixes.

Args:
    name: String to strip periods from.

Returns:
    str: Original string without '.'
"""


RULES = (title_case, strip_periods,)
