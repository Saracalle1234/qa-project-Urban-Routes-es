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
        self.cvv_field = driver.find_elements(By.CLASS_NAME, "card-input")
        self.submit_button = (By.XPATH, "//button[contains(@class, 'button full') and text()='Add']")

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

    def fill_card_number(self , card_number , card_code):
        try:
            number_element = WebDriverWait(self.driver , 10).until(EC.element_to_be_clickable((By.ID , "card_number")))
            number_element.clear()
            number_element.send_keys(card_number)

            code_element = WebDriverWait(self.driver , 10).until( EC.element_to_be_clickable((By.ID , "code")) )
            code_element.clear()
            code_element.send_keys(card_code)
            time.sleep(0.5)
            code_element.send_keys(Keys.TAB)

            print("Número de tarjeta y código ingresados correctamente")

        except StaleElementReferenceException:

            print("El campo fue modificado en el DOM. Reintentando...")
            self.fill_card_number(card_number , card_code)
            # Reintenta una vez
        except TimeoutException: (print("No se encontró uno de los campos en el DOM"))



