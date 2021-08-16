import unittest
from selenium import webdriver
import page


class AntyCaptchaAmberTeam(unittest.TestCase):
    """AntyCaptcha AmberTeam Recruitment Exercises"""

    def setUp(self):
        """Starts webdriver."""

        self.driver = webdriver.Firefox()

    def get_exercise_url(self, exercise_number):
        """Constructs and returns url for the specific exercise number"""

        base_url = "https://antycaptcha.amberteam.pl/exercises/exercise"
        seed_url = "?seed=e88ff36a-e046-473f-8e7c-1a8a611ebbea"
        return base_url + str(exercise_number) + seed_url

    def test_exercise_1(self):
        self.driver.get(self.get_exercise_url(1))
        exercise1_page = page.Exercise1Page(self.driver)
        exercise1_page.press_b2_button()
        exercise1_page.press_b1_button()
        exercise1_page.press_b1_button()
        assert exercise1_page.get_trail_text() == "b2b1b1"
        exercise1_page.press_check_solution_button()
        assert exercise1_page.get_trail_text() == \
            exercise1_page.good_answer_text

    def test_exercise_2(self):
        self.driver.get(self.get_exercise_url(2))
        exercise2_page = page.Exercise2Page(self.driver)
        exercise2_page.set_t14_editbox_text("Smile teach play.")
        exercise2_page.press_b1_button()
        assert exercise2_page.get_trail_text() == "t14:Smile teach play.b1"
        exercise2_page.press_check_solution_button()
        assert exercise2_page.get_trail_text() == \
            exercise2_page.good_answer_text

    def test_exercise_3(self):
        self.driver.get(self.get_exercise_url(3))
        exercise3_page = page.Exercise3Page(self.driver)
        exercise3_page.select_s13_option("Duck Egg Blue")
        assert exercise3_page.get_trail_text() == "s13:v6"
        exercise3_page.press_check_solution_button()
        assert exercise3_page.get_trail_text() == \
            exercise3_page.good_answer_text

    def test_exercise_4(self):
        self.driver.get(self.get_exercise_url(4))
        exercise4_page = page.Exercise4Page(self.driver)
        exercise4_page.select_group_option(0, "Duck Egg Blue")
        exercise4_page.select_group_option(1, "Mango Orange")
        exercise4_page.select_group_option(2, "Anti - Establishment Mint")
        exercise4_page.select_group_option(3, "Amberlite Firemist")
        assert exercise4_page.get_trail_text() == "[6, 1, 7, 8]"
        exercise4_page.press_check_solution_button()
        assert exercise4_page.get_trail_text() == \
            exercise4_page.good_answer_text

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
