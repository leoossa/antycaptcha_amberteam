from selenium.webdriver.common.by import By


class ExerciseLocators(object):
    """A class for exercise page locators."""

    # These are universal across all exercises
    trail = (By.ID, 'trail')
    solution_button = (By.ID, 'solution')
    # These are specific to exercises
    button_B2 = (By.ID, 'btnButton2')  # Exercise 1
    button_B1 = (By.ID, 'btnButton1')  # Exercise 1&2
    input_T14 = (By.ID, "t14")  # Exercise 2
    select_S13 = (By.ID, "s13")  # Exercise 3

    # These are specific to the exercise 4
    @staticmethod
    def get_radio_value(group, text_value):
        """Radio value = "v" + "valueNumber" + "radioGroupNumber
        i.e. value="v23" for "Verdoro Green" for group 3"""

        # Watch out! There's '3' missing!
        values = {
            "Beluga Brown": 0,
            "Mango Orange": 1,
            "Verdoro Green": 2,
            "Freudian Gilt": 4,
            "Pink Kong": 5,
            "Duck Egg Blue": 6,
            "Anti - Establishment Mint": 7,
            "Amberlite Firemist": 8,
        }

        return "v" + str(values[text_value]) + str(group)

    @staticmethod
    def return_radio_selector(group, text_value):
        """Returns a selector to click for given group and text_value"""

        radio_value = ExerciseLocators.get_radio_value(group, text_value)
        return (By.CSS_SELECTOR, f"input[value='{radio_value}']")
