import allure

from pages.base_page import BasePage


class ScooterPage(BasePage):
    @allure.step("Метод получения текста ответа из выпадающего списка")
    def get_text_drop_down_list(self, question, answer):
        self.find_element_located_click(question)
        element_questions = self.get_attribute(question, "aria-disabled")
        element_answers = self.get_element_text(answer)
        return element_questions, element_answers
