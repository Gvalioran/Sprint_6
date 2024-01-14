from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class OrderPageLocators(BasePageLocators):
    TO_ORDER_1 = (By.XPATH, ".//*[@class='Button_Button__ra12g']")
    TO_ORDER_2 = (By.XPATH, ".//*[@class='Home_FinishButton__1_cWm']")
    TO_ORDER_3 = (By.XPATH, ".//*[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    NAME_INPUT_FIELD = (By.XPATH, ".//*[@placeholder='* Имя']")
    SURNAME_INPUT_FIELD = (By.XPATH, ".//*[@placeholder='* Фамилия']")
    ADDRESS_INPUT_FIELD = (By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']")
    UNDERGROUND_INPUT_FIELD = (By.XPATH, ".//*[@placeholder='* Станция метро']")
    SELECT_UNDERGROUND = (By.XPATH, ".//*[@class='select-search__row']")
    NUMBER_INPUT_FIELD = (By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, ".//*[text()='Далее']")
    DATE_INPUT_FIELD = (By.XPATH, ".//*[@placeholder='* Когда привезти самокат']")
    THE_RENTAL_PERIOD = (By.XPATH, ".//*[text()='* Срок аренды']")
    PERIOD_TWO_DAYS = (By.XPATH, ".//*[text()='двое суток']")
    COLOR_BLACK = (By.XPATH, ".//*[@id='black']")
    COMMENT_INPUT_FIELD = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")
    CONFIRMATION_ORDER = (By.XPATH, ".//*[text()='Да']")
    ORDER_PLACED = (By.XPATH, ".//*[text()='Посмотреть статус']")
