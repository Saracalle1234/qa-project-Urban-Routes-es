from selenium.webdriver.common.by import By
from data import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from data.data import phone_number
from pages import urban_routes_page as urp

import sys
import os


class TestUrbanRoutes:

    driver = None
    routes_page = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs",{'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(),options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = urp.UrbanRoutesPage(self.driver)
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

    def test_confirmar(self):
        self.routes_page.click_on_confirmar_button()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
