__version__ = "0.1.0"

from dataclasses import dataclass

from . import rules


@dataclass
class NameStandardizer:
    """This class provides utilities to standardize names.

    # TODO: eventually this class will have attributes for 'strict', and other params regarding the rules in rules.py
    """

    def standardize(self, name: str) -> str:
        """Method to standardize a name.

        Standardize takes a string name representation and
        sequentially enforces rules (using rules.py utility
        functions).

        Args:
            name: Name to standardize

        Returns:
            str: Standardized representation of the input name.
        """
        clean_name = name
        for rule in rules.RULES:
            clean_name = rule(clean_name)
        return clean_name

    def standardize_many(self, names: list[str]) -> list[str]:
        """Standardize many simply provides a helper function to run standardize
         on multiple names at once.

         Args:
             names: Iterable array of names to standardize.

        Returns:
            list[str]: A list of standardized names.
        """
        assert type(names) == list
        return [self.standardize(name) for name in names]
