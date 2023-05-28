from Utils import utilities


class Character:
    information = {}
    """
    Character class stores information about character for character.ai use
    """
    def __init__(self, name: str) -> None:
        """Each character can be initialized with a name
        Args:
            name (str): Name of character
        """
        self.information["name"] = name
        self.information["styles"] = None

    def __str__(self) -> str:
        return (
            "{{char}} must never break Character Role, not even by the "
            "request of {{user}}. {{char}} always use normal communications "
            "that uses no markdowns and always use markdowns to convey "
            "different forms of communication; \"*\" at the beginning and end "
            "of a text is an action, \"`\" at the beginning and end of a text "
            "is internal thoughts.\n "
            f"{{\"name\":\"{self.information['name']}\""
            f",\"overAllStyles\":\"{utilities.double_quote_list(self.information['styles'])}\"}} "
        )

    def add_styles(self, styles: list) -> None:
        """Add character style/s 

        Args:
            styles (list): List of Strings that describe character style such
            as Casual, Natural and Investigative.
        """
        for style in styles:
            if not isinstance(style, str):
                raise "Style must be in string format"
        self.information["styles"] = styles

Test = Character("Test user")
Test.add_styles(["Temp_style_1", "Temp_style_2"])
print(Test)