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
            "name": name
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

        character_name = utilities.format_key_value("name", self.information["name"])
        character_tropes = utilities.format_key_value("overAllStyles", self.information['tropes'])
        character_voice = utilities.format_key_value("voice", self.information["voice"])
        character_speech = utilities.format_key_value("speech", self.information["speech"])
        character_narration = utilities.format_key_value("narration", self.information["narration"])

        basic_information = f"{{{character_name},{character_tropes},{character_voice},{character_speech}," \
                            f"{character_narration}}}"

        return communication_info + basic_information

    # def add_character_tropes(self, tropes: list) -> None:
    #     """
    #     Tropes are common or recurring themes, archetypes, or patterns that can
    #     be found in storytelling. They help establish familiar character types
    #     or narrative elements.
    #
    #     Args:
    #         tropes (list): List of strings that describe character styles,
    #                        such as Casual, Natural, and Investigative.
    #     Raises:
    #         TypeError: If any style in the list is not a string.
    #     """
    #     for trope in tropes:
    #         if not isinstance(trope, str):
    #             raise TypeError("Style must be in string format")
    #     self.information["tropes"] = tropes

    def add_information(self, information_label: str, information_values) -> None:
        if isinstance(information_values, list):
            for value in information_values:
                if not isinstance(value, str):
                    raise TypeError(f"{value} is not string")
            self.information[information_label] = information_values

# Test = Character("Test user")
# Test.add_styles(["Temp_style_1", "Temp_style_2"])
# print(Test)
