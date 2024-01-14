import allure

from pages.base_page import BasePage


class ScooterPage(BasePage):
    @allure.step("Get text from drop-down list")
    def get_text_drop_down_list(self, question, answer):
        self.find_element_located_click(question)
        element_questions = self.find_element_located(question).get_attribute("aria-disabled")
        element_answers = self.find_element_located(answer).text
        return element_questions, element_answers
