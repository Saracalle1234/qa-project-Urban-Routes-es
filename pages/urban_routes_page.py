from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utils.retrieve_code import retrieve_phone_code
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import data
from selenium.webdriver import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import time
from data.data import message_for_driver


class urban_routes_page:
    def __init__(self , driver):
        self.driver = driver
        self.wait = WebDriverWait(driver , 20)
        self.from_field = (By.ID, "from")
        self.to_field = (By.ID, "to")
        self.flash_button=(By.XPATH, "//div[@class='mode active' and text()='Flash']")
        self.taxi_button = (By.XPATH , "//button[contains(@class, 'round') and text()='Pedir un taxi']")
        self.comfort_button = (By.XPATH , "//img[@alt='Comfort']")
        self.telefono_button = (By.XPATH , "//div[@class='np-text' and text()='Número de teléfono']")
        self.phone_field = (By.ID, "phone")
        self.siguiente_button = (By.XPATH , "//button[contains(@class, 'full') and text()='Siguiente']")
        self.sms_code_field= (By.ID , "code")
        self.confirmar_button = (By.XPATH , "//button[contains(@class, 'full') and text()='Confirmar']")
        self.pago_button = (By.XPATH , "//div[@class='pp-text' and text()='Método de pago']")
        self.tarjeta_button = (By.XPATH , "//div[@class='pp-title' and text()='Agregar tarjeta']")
        self.card_number_field = (By.ID , 'number')
        self.cvv_field = (By.XPATH , '//input[@id="code" and @placeholder="12"]')
        self.pp_buttons= (By.XPATH , "//div[@class='pp-buttons']")
        self.submit_button = (By.XPATH, "//button[@type='submit' and text()='Agregar']")
        self.close_button = (By.CSS_SELECTOR, '.payment-picker .close-button')
        self.message_for_the_driver = (By.ID, "comment")
        self.blanket_and_handkerchiefs= (By.CSS_SELECTOR , '.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
        self.ice_cream_button = (By.CSS_SELECTOR , '.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
        self.ice_cream_counter = (By.CSS_SELECTOR , '.counter-value')
        self.taxi_search_button = (By.CLASS_NAME , 'smart-button')
        self.order_header_title = (By.CLASS_NAME , 'order-btn-group')
        self.menu_button = (By.XPATH , '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[3]')
        self.wait_driver_details = (By.XPATH , '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[3]')

    def set_from(self, from_address):
       # self.driver.find_element(*self.from_field).send_keys(from_address)
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        # self.driver.find_element(*self.to_field).send_keys(to_address)
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_flash_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.flash_button))

    def click_on_flash_button(self):
        self.get_flash_button().click()

    def get_taxi_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.taxi_button))

    def click_on_taxi_button(self):
        self.get_taxi_button().click()

    def get_comfort_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.comfort_button))

    def click_on_comfort_button(self):
        self.get_comfort_button().click()

    def get_telefono_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.telefono_button))

    def click_on_telefono_button(self):
        self.get_telefono_button().click()

    def set_phone(self , from_phone):
        # self.driver.find_element(*self.from_field).send_keys(from_address)
        field = self.wait.until(EC.visibility_of_element_located(self.phone_field))
        field.clear()
        field.send_keys(from_phone)
        assert from_phone == field.get_attribute("value")

    def get_phone(self):
        return self.driver.find_element(*self.phone_field).get_property('value')

    def get_siguiente_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.siguiente_button))

    def click_on_siguiente_button(self):
        self.get_siguiente_button().click()

    def set_sms_code(self):
        code = retrieve_phone_code(self.driver)
        WebDriverWait(self.driver , 5).until(EC.visibility_of_element_located(self.sms_code_field))
        sms_field = self.driver.find_element(*self.sms_code_field)
        sms_field.clear()
        sms_field.send_keys(code)
        self.driver.find_element(*self.confirmar_button).click()

    def retrieve_phone_code(driver):
        return "123456"

    def get_pago_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.pago_button))

    def click_on_pago_button(self):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME , "overlay")))
        button = self.wait.until(EC.element_to_be_clickable(self.pago_button))
        button.click()

    def get_tarjeta_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.tarjeta_button))

    def click_on_tarjeta_button(self):
        self.get_tarjeta_button().click()

    def click_card(self, card_number):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.card_number_field).click()
        WebDriverWait(self.driver , 10).until(EC.element_to_be_clickable(self.card_number_field)).send_keys(card_number)

    def fill_cvv_field(self , card_code):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.cvv_field).click()
        WebDriverWait(self.driver , 10).until(EC.element_to_be_clickable(self.cvv_field)).send_keys(card_code)

    def get_pp_buttons(self):
        return self.wait.until(EC.element_to_be_clickable(self.pp_buttons))

    def click_on_pp_buttons(self):
        self.get_pp_buttons().click()

    def get_submit_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.submit_button))

    def click_on_submit_button(self):
        self.get_submit_button().click()

    def get_close_button(self):
        return WebDriverWait(self.driver , 10).until(EC.element_to_be_clickable(self.close_button))

    def click_on_close_button(self):
        self.get_close_button().click()

    def driver_message(self, message):
        message_box = self.wait.until(EC.presence_of_element_located(self.message_for_the_driver))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", message_box)
        message_box.clear()
        message_box.send_keys(message)

    def is_message_sent(self, expected_message):
        message_input = self.driver.find_element(*self.message_for_the_driver)
        return expected_message in message_input.get_attribute("value")

    def toggle_blanket_and_handkerchiefs(self):
        option = self.wait.until(EC.element_to_be_clickable(self. blanket_and_handkerchiefs))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
        option.click()

    def is_blanket_and_handkerchiefs_selected(self):
            checkbox = self.driver.find_element(By.CSS_SELECTOR, 'input.switch-input')
            return checkbox.is_selected()

    def add_ice_cream(self, quantity=2):
            button = self.wait.until(EC.element_to_be_clickable(self.ice_cream_button))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            for _ in range(quantity): button.click()
            self.wait.until(EC.element_to_be_clickable(self.ice_cream_button))

    def get_ice_cream_count(self):
        counter = self.driver.find_element(*self.ice_cream_counter)
        return int(counter.text.strip())

    def is_ice_cream_added(self):
        return self.get_ice_cream_count() == 2

    def search_taxi(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.taxi_search_button).click()

    def order_header(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.order_header_title).click()

    def click_menu_button(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.menu_button).click()

    def details_button(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.wait_driver_details).click()

    def get_details(self):
        return self.driver.find_element(*self.wait_driver_details).text



