from selenium.webdriver.common.by import By
from data import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from data.data import phone_number
from pages import urban_routes_page as urp
from data.data import message_for_driver
from selenium.webdriver.support import expected_conditions as EC

import sys
import os

class TestUrbanRoutes:
    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs",{'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(),options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.urban_routes_page(cls.driver)
        cls.page = urp.urban_routes_page(cls.driver)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = urp.urban_routes_page(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_flash(self):
        self.routes_page.click_on_flash_button()
        self.routes_page.click_on_taxi_button()
        self.routes_page.click_on_comfort_button()
        self.routes_page.click_on_telefono_button()

    def test_set_phone(self):
        self.routes_page.set_phone(data.phone_number)
        assert self.routes_page.get_phone() == data.phone_number

    def test_siguiente(self):
        self.routes_page.click_on_siguiente_button()

    def test_set_sms(self):
        self.routes_page.set_sms_code()

    def test_pago(self):
        self.routes_page.click_on_pago_button()

    def test_tarjeta(self):
        self.routes_page.click_on_tarjeta_button()

    def test_set_card(self):
        self.routes_page.click_card(data.card_number)
        self.routes_page.fill_cvv_field(data.card_code)

    def test_pp_buttons(self):
        self.routes_page.click_on_pp_buttons()

    def test_submit_button(self):
        self.routes_page.click_on_submit_button()

    def test_close_button(self):
        self.routes_page.click_on_close_button()

    def test_driver_message(self):
        self.page.driver_message(message_for_driver)
        assert self.page.is_message_sent(message_for_driver)

    def test_toggle_blanket_and_handkerchiefs(self):
        self.page.toggle_blanket_and_handkerchiefs()
        assert self.page.is_blanket_and_handkerchiefs_selected()

    def test_add_ice_cream(self):
        self.page.add_ice_cream()
        assert self.page.is_ice_cream_added()

    def test_search_taxi(self):
        self.driver.implicitly_wait(10)
        self.routes_page.search_taxi()
        self.routes_page.order_header()
        self.routes_page.click_menu_button()
        self.routes_page.details_button()
        self.routes_page.get_details()
        details_button = self.routes_page.get_details()
        assert self.routes_page.get_details() == details_button

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
