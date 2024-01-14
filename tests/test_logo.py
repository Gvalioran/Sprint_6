import time
import allure

from constants.constants import Url
from pages.order_page import OrderPage


@allure.story('Тесты логотипа Яндекс Самокат')
class TestOrderingScooter:
    @allure.title('Тест перехода на главную страницу')
    def test_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.transition_site(Url.ORDER_URL)
        order_page.transition_logo_scooter()
        result = order_page.transition_logo_scooter()
        assert result == Url.BASE_URL

    @allure.title('Тест перехода на страницу Яндекса')
    def test_go_dzen(self, driver):
        order_page = OrderPage(driver)
        order_page.transition_site(Url.ORDER_URL)
        order_page.transition_dzen()
        order_page.switch_window(1)
        time.sleep(1)
        current_url = order_page.current_url()
        assert 'https://dzen.ru/' in current_url
