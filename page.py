from selenium.webdriver.support.ui import Select

from locators import ExerciseLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class ExercisePage(BasePage):
    """Methods universal across all exercise pages"""

    def __init__(self, driver):
        super().__init__(driver)
        self.good_answer_text = "OK. Good answer"
        self.trail = self.driver.find_element(*ExerciseLocators.trail)

    def get_trail_text(self):
        """Returns the trail text"""
        return self.trail.text

    def press_check_solution_button(self):
        """Presses "Check solution" button"""

        solution_button = self.driver.find_element(
            *ExerciseLocators.solution_button)
        solution_button.click()


class Exercise1Page(ExercisePage):
    """Exercise 1 page action methods"""

    def press_b1_button(self):
        """Presses "B1" button"""

        button_B1 = self.driver.find_element(*ExerciseLocators.button_B1)
        button_B1.click()

    def press_b2_button(self):
        """Presses "B2" button"""

        button_B2 = self.driver.find_element(*ExerciseLocators.button_B2)
        button_B2.click()


class Exercise2Page(ExercisePage):
    """Exercise 2 page action methods"""

    def press_b1_button(self):
        """Presses "B1" button"""

        button_B1 = self.driver.find_element(*ExerciseLocators.button_B1)
        button_B1.click()

    def set_t14_editbox_text(self, text):
        """Set the edit box text"""

        t14_editbox = self.driver.find_element(*ExerciseLocators.input_T14)
        t14_editbox.clear()
        t14_editbox.send_keys(text)


class Exercise3Page(ExercisePage):
    """Exercise 3 page action methods"""

    def select_s13_option(self, option_text):
        select_S13 = Select(self.driver.find_element(
            *ExerciseLocators.select_S13))
        select_S13.select_by_visible_text(option_text)


class Exercise4Page(ExercisePage):
    """Exercise 4 page action methods"""

    def select_group_option(self, group, option_text):
        """Sets option in selected group by "text option" """

        selector = ExerciseLocators.return_radio_selector(group, option_text)
        select = self.driver.find_element(*selector)
        select.click()
