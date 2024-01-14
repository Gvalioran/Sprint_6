# Sprint_6
# Проект автоматизации тестирования Яндекс самокат
* Основа для написания автотестов — фреймворк pytest.
* Установить зависимости — pip install -r requirements.txt.
* Команда для запуска — pytest tests --alluredir allure_results
* Команда для формирования отчетов Allure — allure serve allure_results 

constants.py
* Url - Класс описания ссылок
* Answers - Класс описания правильных ответов на вопросы для списка "Вопросы о важном"
* TestsData1 - Класс с первым набором тестовых данных для оформления заказа
* TestsData2 - Класс с вторым набором тестовых данных для оформления заказа

base_page_locators.py
* BasePageLocators - Класс с общими локаторами

order_page_locators.py
* OrderPageLocators - Класс с локаторами для страницы оформления заказа

scooter_page_locators.py
* ScooterPageLocators - Класс с локаторами для главной страницы

base_page.py
* transition_site - функция для перехода на сайт
* find_element_located - функция для поиска элемента
* find_element_located_click - функция для поиска элемента и клика по нему
* find_element_located_input - функция для поиска элемента и ввода данных
* find_elements_located - функция для поиска множества элементов
* accept_the_cookies - функция для принятия куки
* current_url - функция для получения url
* switch_window - функция для переключения между вкладками

order_page.py
* entering_test_data - функция для заполнения формы и оформления заказа
* transition_logo_scooter - функция для перехода на логотип самоката
* transition_dzen - функция для перехода на страницу Дзен

scooter_page.py
* get_text_drop_down_list - функция для открытия вопроса и получения текста ответа

test_drop-down_list.py
* QUESTION_ANSWER - список тестовых данных отформатированный для параметризации
* test_drop_down_list_text_1 - функция для тестирования списка "Вопросы о важном"