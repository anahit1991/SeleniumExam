import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from locators import Signup
from locators import Login
from locators import Hotels
from locators import SearchHotel
from locators import SelectRoom
from locators import Authorization


class TestTravels(unittest.TestCase):
    website_url = 'https://www.phptravels.net/signup'
    manual_url = 'https://www.agoda.com/ru-ru/book/payment/?cnty=246&secdat=qYWM4u9zM1a%252FP7%252BzqmpO61hpq7WiEBbDNjnhz7ndtIQDODIOinqHL3krtYzZNFSVxZXS%252Fro9h9ctJIxNXHnDCxl4tOj%252BvlCyLw8qSIb0tIs6%252FxCHr9y9eGonp3BL89gW614quRDVndjnoX9eWoK1oA7OW3OVqcoIRGt2PDx19XwU7xKGcHP5xoQl42CinvXZbUUA6ObW5l11OkTgCx2AGTrpaLBC0Rlc5Qa%252BVZcZBcb7wB0ptC%252BRbj3tp4tqLbvASUwsOIXM4aYGhr22UkxIKA%253D%253D&v=29&cnIcp=0&dclid=&gclid=&ame=&aso=&aca=&aco=&ate=&mrs=0&siteId=1743607&ori=AM&r0=JKowrovx3llakSd6X0z0onuTAjvJnQ7qPIpPbXI%252Ftp3IbOgZiGkGoP5M%252BHys%252BtEIRRy3zg1BMAux7VeCsZda%252FBW7kDW3SUO420aSmVp3MbNTc%252FFlZzzM27RnyfM3w0TUvhhKtSrQ6E8mPgej%252BNnyJ3LdI4vj1skdzGczY%252ByfelP6mkwvxGJVISFRYILvjE2KOfFg8XC1%252BTdWura1tDba69uXH%252BrefzqmmHeeBfZ77miK2xmXs4rDiYStaPeSnBZ9O2X7SusjR14RybBhMhul%252BGb%252BfiQto80KPSnPorANQBnHNaIXYHsnmQTLSVkrGpR%252F7Raw%252Bbb3uME1eckA6dBXtk95VYbLgU1qNfffeyxAROGuXEV6wSRRNfVhlikrynsMpnjAag1WS7u%252BBxaJJSFcYBbT2NH6GINAePyqYQF7mOc%253D&nr0=1&xbr0=&sarg=%252Fzg4tKBd6U1Iq9dzvlCuLIPUADo%252B6ZZnoYz3TBlW%252FnPOO8OOfCLUtUHJjeKj6WZTLf0DC%252B2GV%252FrIlp7qfgf8699LXeWL33dxlkDfeAD2uhD6y%252BuPoeH7cAdIMjC%252B%252B30dlNlib1iws7NwcDQHdJiBI71tLs6HrYE5aM10BSLTFeje6cVYLlECOveUk3LWA0bl866coHRQLq9nl6z9lExJrdJQfp1yb6jCfm0S7b40LsFflbkJYRyYY9XQ3jHHh1vw&m=601&sreq=-1&finc=false&nco=0'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.website_url)

    def signup(self):
        time.sleep(2)
        driver = self.driver
        action = ActionChains(driver)
        driver.find_element(By.XPATH, Signup.firstname).send_keys('Test')
        time.sleep(2)
        driver.find_element(By.XPATH, Signup.lastname).send_keys('Testik')
        time.sleep(2)
        driver.find_element(By.XPATH, Signup.phone).send_keys('094323108')
        driver.find_element(By.XPATH, Signup.email).send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element(By.XPATH, Signup.email).send_keys('test1@gmail.com')
        time.sleep(2)
        driver.find_element(By.XPATH, Signup.password).send_keys('tonkpo123')
        time.sleep(2)
        signup_button1 = driver.find_element(By.XPATH, Signup.signup_button)
        action.move_to_element(signup_button1).click().perform()
        time.sleep(2)

    def login(self):
        time.sleep(4)
        driver = self.driver
        action = ActionChains(driver)
        driver.find_element(By.XPATH, Login.email).send_keys('test1@gmail.com')
        time.sleep(2)
        driver.find_element(By.XPATH, Login.password).send_keys('tonkpo123')
        time.sleep(2)
        login_button1 = driver.find_element(By.XPATH, Login.login_button)
        action.move_to_element(login_button1).click().perform()
        time.sleep(2)

    def hotel(self):
        time.sleep(2)
        driver = self.driver
        action = ActionChains(driver)
        click_hotels = driver.find_element(By.XPATH, Hotels.hotel_menu)
        action.move_to_element(click_hotels).click().perform()
        time.sleep(2)

    def search_hotel_yerevan(self):
        time.sleep(2)
        driver = self.driver
        action = ActionChains(driver)
        driver.find_element(By.XPATH, SearchHotel.hotels_in_yerevan).click()
        time.sleep(2)
        write_text = driver.find_element(By.XPATH, '//*[@id="fadein"]/span/span/span[1]/input')
        write_text.send_keys('Yerevan')
        time.sleep(2)
        driver.find_element(By.XPATH, SearchHotel.select_country_flag).click()
        time.sleep(2)
        search_button2 = driver.find_element(By.XPATH, SearchHotel.search_button)
        action.move_to_element(search_button2).click().perform()
        time.sleep(2)
        search_name = driver.find_element(By.XPATH, SearchHotel.search_by_name)
        action.move_to_element(search_name).click().perform()
        search_name.send_keys(SearchHotel.search_wishes_hotel)
        time.sleep(3)
        select_hotel = driver.find_element(By.XPATH, SearchHotel.select_hotel)
        action.move_to_element(select_hotel).click().perform()
        self.driver.switch_to.window(self.driver.window_handles[1])
        booking = driver.find_element(By.XPATH, SelectRoom.select_room)
        action.move_to_element(booking).click().perform()
        driver.switch_to.window(driver.window_handles[2])
        time.sleep(5)
        driver.find_element(By.XPATH, SelectRoom.booking_now).click()
        time.sleep(2)

    def authorisation(self):
        self.driver.find_element(By.XPATH, Authorization.xik).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Authorization.name).send_keys('Test Testik')
        time.sleep(2)
        self.driver.find_element(By.XPATH, Authorization.email).send_keys('test1@gmail.com')
        time.sleep(2)
        self.driver.find_element(By.XPATH, Authorization.repeat_email).send_keys('test1@gmail.com')
        time.sleep(2)
        self.driver.find_element(By.XPATH, Authorization.phone_number).send_keys('094323104')
        time.sleep(5)
        self.driver.find_element(By.XPATH, Authorization.submit).click()
        time.sleep(5)
        manual = self.manual_url
        selenium_url = self.driver.current_url
        assert manual == selenium_url

    def test_case_website(self):
        self.signup()
        self.login()
        self.hotel()
        self.search_hotel_yerevan()
        self.authorisation()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
