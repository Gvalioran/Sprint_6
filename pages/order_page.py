import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Переход к оформлению заказа")
    def transition_order(self, button_order):
        self.find_element_located_click(button_order)

    @allure.step("Ввод данных для оформления заказа в первой форме")
    def entering_test_data_page1(self, data):
        self.find_element_located_input(OrderPageLocators.NAME_INPUT_FIELD, data.TEST_NAME)
        self.find_element_located_input(OrderPageLocators.SURNAME_INPUT_FIELD, data.TEST_SURNAME)
        self.find_element_located_input(OrderPageLocators.ADDRESS_INPUT_FIELD, data.TEST_ADDRESS)
        self.find_element_located_input(OrderPageLocators.UNDERGROUND_INPUT_FIELD, data.TEST_UNDERGROUND)
        self.find_element_located_click(OrderPageLocators.SELECT_UNDERGROUND)
        self.find_element_located_input(OrderPageLocators.NUMBER_INPUT_FIELD, data.TEST_NUMBER)

    @allure.step("Переход на вторую форму")
    def transition_page2(self):
        self.find_element_located_click(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Ввод данных для оформления заказа в второй форме")
    def entering_test_data_page2(self, data):
        self.find_element_located_input(OrderPageLocators.DATE_INPUT_FIELD, data.TEST_DATE)
        self.find_element_located_click(OrderPageLocators.COLOR_BLACK)
        self.find_element_located_click(OrderPageLocators.THE_RENTAL_PERIOD)
        self.find_element_located_click(OrderPageLocators.PERIOD_TWO_DAYS)
        self.find_element_located_input(OrderPageLocators.COMMENT_INPUT_FIELD, data.TEST_COMMENT)
        self.find_element_located_click(OrderPageLocators.TO_ORDER_3)
        self.find_element_located_click(OrderPageLocators.CONFIRMATION_ORDER)

    @allure.step("Проверка успешного оформления заказа")
    def checking_completed_order(self):
        return self.find_element_located(OrderPageLocators.ORDER_PLACED).text

    @allure.step("Переход по логотипу самоката")
    def transition_logo_scooter(self):
        self.find_element_located_click(OrderPageLocators.LOGO_SCOOTER)

    @allure.step("Переход на страницу Яндекса")
    def transition_dzen(self):
        self.find_element_located_click(OrderPageLocators.YANDEX)

    @allure.step("Переключение на страницу яндекса c ожиданием логотипа дзен")
    def switch_dzen(self):
        self.switch_window(OrderPageLocators.LOGO_YA, 1)
