import pyautogui
from base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для сервера "Диплом"
    def server_diploma_locator(self):
        return By.XPATH, f'//div[text()="СерверДилом"]'

    # Локатор для канала для тестов (#6)
    def channel_locator(self):
        return By.XPATH, f'//div[text()="6"]'

    # Локатор для поля ввода сообщения
    def message_input_locator(self):
        return By.XPATH, f'//div[@role="textbox"]'

    # Локатор для сообщения
    def message_locator(self):
        return By.XPATH, f'//div[@aria-roledescription="Сообщение"]//div[@class="markup_f8f345 messageContent_f9f2ca"]'

    # Локатор для формы сообщения
    def form_message_locator(self):
        return By.XPATH, f'//div[@aria-roledescription="Сообщение"]'

    # Локатор для кнопки редактирования сообщения
    def actions_button_edit_locator(self):
        return By.XPATH, f'//div[@aria-roledescription="Сообщение"]//div[@class="buttonContainer_f9f2ca"]//div[@aria-label="Действия с сообщениями"]//div[@aria-label="Изменить"]'

    # Локатор для кнопки реакции на сообщение
    def actions_button_reaction_locator(self):
        return By.XPATH, f'//div[@aria-roledescription="Сообщение"]//div[@class="buttonContainer_f9f2ca"]//div[@aria-label="Действия с сообщениями"]//div[@aria-label="Нажмите, чтобы отреагировать эмодзи thumbsup"]'

    # Локатор для многоточия (в меню сообщения)
    def actions_button_more_locator(self):
        return By.XPATH, f'//div[@aria-roledescription="Сообщение"]//div[@class="buttonContainer_f9f2ca"]//div[@aria-label="Действия с сообщениями"]//div[@aria-label="Ещё"]'

    # Локатор для кнопки "Удалить сообщение"
    def delete_message_button_locator(self):
        return By.XPATH, f'//div[@id="message-actions-delete"]'

    # Локатор для кнопки "Подтвердить" при удалении сообщения
    def delete_message_confirm_button_locator(self):
        return By.XPATH, f'//button[@type="submit"]'

    # Локатор для реакции под сообщением
    def reaction_locator(self):
        return By.XPATH, f'//div[@class="reactionInner_ec6b19"]'

    # Локатор для существующего отправителя сообщения
    def mentioned_user_locator(self):
        return By.XPATH, f'//div[@class="markup_f8f345 messageContent_f9f2ca"]//span[@role="button"]'

    # Локатор для несуществующего отправителя сообщения
    def mentioned_non_exist_user_locator(self):
        return By.XPATH, f'//div[@class="markup_f8f345 messageContent_f9f2ca"]'

    # Метод для клика по серверу Диплом
    def clic_to_server_diploma(self):
        self.find_element(self.server_diploma_locator())
        self.click(self.server_diploma_locator())

    # Метод для клика по каналу "Основной"
    def clic_to_channel(self):
        self.find_element(self.channel_locator())
        self.click(self.channel_locator())

    # Метод для ввода и отправки сообщения
    def send_message_in_channel(self, text):
        self.send_message(self.message_input_locator(), {text})


    # Метод для редактирования сообщения
    def edit_message(self):
        self.hover(self.form_message_locator())
        self.click(self.actions_button_edit_locator())
        pyautogui.typewrite("... and fun")
        pyautogui.press('enter')

    # Метод для удаления сообщения
    def delete_message(self):
        self.hover(self.form_message_locator())
        self.click(self.actions_button_more_locator())
        self.click(self.delete_message_button_locator())
        self.click(self.delete_message_confirm_button_locator())

    # Метод для добавления реакции через меню (многоточие)
    def send_reaction(self):
        self.hover(self.form_message_locator())
        self.click(self.actions_button_reaction_locator())

    # Метод для удаления реакции
    def delete_reaction(self):
        self.click(self.reaction_locator())

    # Метод для проверки видимости реакции
    def is_reaction_displayed(self):
        return self.find_element(self.reaction_locator())

   # Метод для получения атрибута существующего пользователя
    def is_mentioned_user_exists(self):
        return self.find_element(self.mentioned_user_locator()).get_attribute("role")

    # Метод для получения атрибута несуществующего пользователя
    def is_mentioned_user_non_exists(self):
        return self.find_element(self.mentioned_non_exist_user_locator()).get_attribute("role")

    # Метод для локализации текста в сообщении
    def is_message_send(self):
        return self.find_element(self.message_locator()).text





