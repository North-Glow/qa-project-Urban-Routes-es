import helpers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    wait = (By.CLASS_NAME, "workflow")
    mode = (By.XPATH, '//div[@class="workflow-subcontainer"]//button[@class="button round"]')
    tag = (By.XPATH, '//div[@class="tariff-cards"]//div[@class="tcard"]//div[contains(text(), "Comfort")]')
    phone_number_button = (By.CLASS_NAME, "np-button")
    phone_field = (By.ID, "phone")
    phone_next_button = (By.CLASS_NAME, "button full")
    phone_phone_code_field = (By.ID, "code")
    phone_confirm_button_1 = (By.XPATH, '//div[@class="section active"]//button[@class="button full"]')
    phone_confirm_button_2 = (By.XPATH, '//div[@class="section active"]//button[@class="button full"]')
    payment_method_button = (By.CLASS_NAME, "pp-button")
    plus_button = (By.CLASS_NAME, "pp-plus-container")
    card_number_field = (By.XPATH, '//input[@ID="number"]')
    card_code_field = (By.XPATH, '//div[@class="card-second-row"]//input[@ID="code"]')
    blank_space = (By.XPATH, '//div[@class="plc"]')
    add_card_button = (By.XPATH, '//button[text()="Agregar"]')
    close_button = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    message_for_driver = (By.ID, "comment")
    requirements = (By.XPATH, '//span[@class="slider round"]')
    add_icecream = (By.CLASS_NAME, "counter-plus")
    main_button = (By.CLASS_NAME, "smart-button")
    order_value = (By.CLASS_NAME, "order-number")


    def __init__(self, driver):
        self.driver = driver

    def loading_wait(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.wait))

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_pedir_taxi_button(self):
        self.driver.find_element(*self.mode).click()

    def set_mode(self):
        self.driver.find_element(*self.tag).click()

    def click_phone_button(self):
        self.driver.find_element(*self.phone_number_button).click()

    def set_phone(self, phone_number):
        self.driver.find_element(*self.phone_field).send_keys(phone_number)

    def click_phone_next_button(self):
        self.driver.find_element(*self.phone_confirm_button_1).click()

    def set_code(self):
        code_tel = helpers.retrieve_phone_code(driver=self.driver)
        self.driver.find_element(*self.phone_phone_code_field).send_keys(code_tel)

    def click_phone_confirm_button(self):
        self.driver.find_element(*self.phone_confirm_button_2).click()

    def click_payment_button(self):
        self.driver.find_element(*self.payment_method_button).click()

    def click_plus_button(self):
        self.driver.find_element(*self.plus_button).click()

    def set_card_number(self, card_num):
        self.driver.find_element(*self.card_number_field).send_keys(card_num)

    def set_card_code(self, card_code):
        self.driver.find_element(*self.card_code_field).send_keys(card_code)

    def click_blank_space(self):
        self.driver.find_element(*self.blank_space).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    def click_close_button(self):
        self.driver.find_element(*self.close_button).click()

    def set_comment(self, comments):
        self.driver.find_element(*self.message_for_driver).send_keys(comments)

    def set_requirements(self):
        self.driver.find_element(*self.requirements).click()

    def add_ice_cream(self):
        self.driver.find_element(*self.add_icecream).click()
        self.driver.find_element(*self.add_icecream).click()

    def click_main_button(self):
        self.driver.find_element(*self.main_button).click()

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def set_mode_comfort(self):
        self.click_pedir_taxi_button()
        self.set_mode()

    def set_phone_number(self, phone_number):
        self.click_phone_button()
        self.set_phone(phone_number)
        self.click_phone_next_button()
        self.set_code()
        self.click_phone_confirm_button()

    def set_credit_card(self, card_num, card_code):
        self.click_payment_button()
        self.click_plus_button()
        self.set_card_number(card_num)
        self.set_card_code(card_code)
        self.click_blank_space()
        self.click_add_card_button()
        self.click_close_button()

    def set_message(self, message):
        self.set_comment(message)

    def loading_driver_info(self):
        WebDriverWait(self.driver, 120).until(expected_conditions.visibility_of_element_located(self.order_value))
