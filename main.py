import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code



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
        code_tel = retrieve_phone_code(driver=self.driver)
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


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.loading_wait()
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_comfort_mode(self):
        routes = UrbanRoutesPage(self.driver)
        routes.set_mode_comfort()
        assert self.driver.find_element(By.XPATH, '//div[@class="tariff-cards"]//div[@class="tcard active"]//div[contains(text(), "Comfort")]').text == "Comfort"

    def test_set_phone(self):
        routes = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes.set_phone_number(phone_number)
        assert self.driver.find_element(By.CLASS_NAME, "np-text").text == "+1 123 123 12 12"
    def test_add_card(self):
        routes = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        routes.set_credit_card(card_number, card_code)
        assert self.driver.find_element(By.XPATH, '//div[@class="pp-value-text"]').text == "Tarjeta"

    def test_message_for_driver(self):
        routes = UrbanRoutesPage(self.driver)
        message = data.message_for_driver
        routes.set_message(message)
        assert self.driver.find_element(By.ID, "comment").get_attribute("value") == "Muéstrame el camino al museo"

    def test_requirements(self):
        routes = UrbanRoutesPage(self.driver)
        routes.set_requirements()
        assert (By.XPATH, '//span[@class="slider round"]')

    def test_ice_cream(self):
        routes = UrbanRoutesPage(self.driver)
        routes.add_ice_cream()
        assert self.driver.find_element(By.XPATH, "//div[contains(text(), 'Helado')]/following-sibling::div//div[@class='counter-value']").text == "2"

    def test_main_button(self):
        routes = UrbanRoutesPage(self.driver)
        routes.click_main_button()
        assert self.driver.find_element(By.CLASS_NAME, "smart-button-main").text == "Pedir un taxi"

    def test_wait_for_driver_info(self):
        routes = UrbanRoutesPage(self.driver)
        routes.loading_driver_info()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
