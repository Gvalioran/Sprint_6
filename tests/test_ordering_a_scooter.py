import allure
import pytest

from constants.constants import Url, TestsData1, TestsData2
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


@allure.story('Тесты оформления заказа')
class TestOrderingScooter:
    @allure.title('Позитивный тест оформления заказа')
    @pytest.mark.parametrize('button_order, data', [(OrderPageLocators.TO_ORDER_1, TestsData1),
                                                    (OrderPageLocators.TO_ORDER_2, TestsData2)])
    def test_ordering_a_scooter(self, driver, button_order, data):
        order_page = OrderPage(driver)
        order_page.transition_site(Url.BASE_URL)
        order_page.accept_the_cookies()
        order_page.transition_order(button_order)
        order_page.entering_test_data_page1(data)
        order_page.transition_page2()
        order_page.entering_test_data_page2(data)
        result = order_page.checking_completed_order()
        assert result == "Посмотреть статус"
