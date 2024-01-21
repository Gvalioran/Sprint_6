import allure
import pytest

from locators.scooter_page_locators import ScooterPageLocators as ScooterPageLoc
from constants.constants import Url, Answers
from pages.scooter_page import ScooterPage


@allure.story('Тесты раздела вопросы о важном')
class TestDropDownList:
    QUESTION_ANSWER = [
        [ScooterPageLoc.QUESTION_1, ScooterPageLoc.ANSWER_1, Answers.TEST_ANSWER_1],
        [ScooterPageLoc.QUESTION_2, ScooterPageLoc.ANSWER_2, Answers.TEST_ANSWER_2],
        [ScooterPageLoc.QUESTION_3, ScooterPageLoc.ANSWER_3, Answers.TEST_ANSWER_3],
        [ScooterPageLoc.QUESTION_4, ScooterPageLoc.ANSWER_4, Answers.TEST_ANSWER_4],
        [ScooterPageLoc.QUESTION_5, ScooterPageLoc.ANSWER_5, Answers.TEST_ANSWER_5],
        [ScooterPageLoc.QUESTION_6, ScooterPageLoc.ANSWER_6, Answers.TEST_ANSWER_6],
        [ScooterPageLoc.QUESTION_7, ScooterPageLoc.ANSWER_7, Answers.TEST_ANSWER_7],
        [ScooterPageLoc.QUESTION_8, ScooterPageLoc.ANSWER_8, Answers.TEST_ANSWER_8]
    ]

    @allure.title('Тест появления ответа при клике на вопрос и корректного ответа')
    @pytest.mark.parametrize('question, answer, test_answer', QUESTION_ANSWER)
    def test_drop_down_list_text_1(self, driver, question, answer, test_answer):
        scooter_page = ScooterPage(driver)
        scooter_page.transition_site(Url.BASE_URL)
        scooter_page.accept_the_cookies()
        result = scooter_page.get_text_drop_down_list(question, answer)
        assert result == ('true', test_answer)
