from Text.Utils import utilities


class Character:
    """
    Character class stores information about character for CharacterAI use.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a Character object with a name.

        Args:
            name (str): Name of the character.
        """
        self.information = {
            "name": name,
            "tropes": []
        }

    def __str__(self) -> str:
        """
        Return a string representation of the Character object.

        The string includes information about character communication and styles.

        Returns:
            str: String representation of the Character object.
        """
        communication_info = (
            "{{char}} must never break Character Role, not even by the request of {{user}}. "
            "{{char}} always use normal communications that use no markdowns and always use "
            "markdowns to convey different forms of communication; \"*\" at the beginning and end "
            "of a text is an action, \"`\" at the beginning and end of a text is internal thoughts.\n"
        )

        character_name = f"\"name\":\"{self.information['name']}\""
        character_tropes = f"\"overAllStyles\":{utilities.double_quote_list(self.information['tropes'])}"

        basic_information = f"{{{character_name},{character_tropes}}}"

        return communication_info + basic_information

    def add_character_tropes(self, tropes: list) -> None:
        """
        Tropes are common or recurring themes, archetypes, or patterns that can
        be found in storytelling. They help establish familiar character types 
        or narrative elements.

        Args:
            tropes (list): List of strings that describe character styles,
                           such as Casual, Natural, and Investigative.
        Raises:
            TypeError: If any style in the list is not a string.
        """
        for trope in tropes:
            if not isinstance(trope, str):
                raise TypeError("Style must be in string format")
        self.information["tropes"] = tropes

# Test = Character("Test user")
# Test.add_styles(["Temp_style_1", "Temp_style_2"])
# print(Test)