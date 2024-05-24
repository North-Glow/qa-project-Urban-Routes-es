import data
import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.common.by import By


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
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.loading_wait()
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_comfort_mode(self):
        routes = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes.set_mode_comfort()
        assert self.driver.find_element(By.XPATH, '//div[@class="tariff-cards"]//div[@class="tcard active"]//div[contains(text(), "Comfort")]').text == "Comfort"

    def test_set_phone(self):
        routes = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes.set_phone_number(phone_number)
        assert self.driver.find_element(By.CLASS_NAME, "np-text").text == "+1 123 123 12 12"
    def test_add_card(self):
        routes = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        routes.set_credit_card(card_number, card_code)
        assert self.driver.find_element(By.XPATH, '//div[@class="pp-value-text"]').text == "Tarjeta"

    def test_message_for_driver(self):
        routes = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        message = data.message_for_driver
        routes.set_message(message)
        assert self.driver.find_element(By.ID, "comment").get_attribute("value") == "Muéstrame el camino al museo"

    def test_requirements(self):
        routes = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes.set_requirements()
        assert (By.XPATH, '//span[@class="slider round"]')

    def test_ice_cream(self):
        routes = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes.add_ice_cream()
        assert self.driver.find_element(By.XPATH, "//div[contains(text(), 'Helado')]/following-sibling::div//div[@class='counter-value']").text == "2"

    def test_main_button(self):
        routes = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes.click_main_button()
        assert self.driver.find_element(By.CLASS_NAME, "order-header-title").is_displayed() == True

    def test_wait_for_driver_info(self):
        routes = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes.loading_driver_info()
        assert self.driver.find_element(By.CLASS_NAME, "order-number").is_displayed() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
