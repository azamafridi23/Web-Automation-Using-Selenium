from selenium import webdriver
import booking.constants as const
import os
from selenium.webdriver.common.by import By
import time
from booking.booking_filteration import BookingFiltration

# I have integrated webdriver.Chrome functionality into my own class called Booking
class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r'C:/Selenium drivers downloaded by azam for web scrapping',tear_down=False):
        self.driver_path = driver_path
        self.tear_down=tear_down
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__() # to call webdriver.Chrome
        self.implicitly_wait(15) # all .find will take atmax 15 sec
        self.maximize_window()

    # Context manager in python = https://www.geeksforgeeks.org/context-manager-in-python/
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.tear_down:
            self.quit() # to close down browser available in webdriver.chrome class
    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self,currency='USD'):
        currency_element = self.find_element('css selector','''button[data-tooltip-text="Choose your currency"]''')
        currency_element.click()
        # watch from 1:12:00 to learn about how to find element based on substring
        usd = self.find_element('css selector',f'a[data-modal-header-async-url-param="changed_currency=1&selected_currency={currency}&top_currency=1"]')
        usd.click()
        #time.sleep(2)

    def select_place(self,place_to_go):
        search_field = self.find_element('id','ss')
        search_field.clear() # to clean the existing text
        search_field.send_keys(place_to_go)

        select_option = self.find_element('css selector','li[data-i="0"]')
        select_option.click()
        time.sleep(2)

    def select_date(self,check_in="2023-02-17",check_out="2023-03-15"):
        open_options = self.find_element('css selector','svg[class="bk-icon -experiments-calendar sb-date-picker_icon-svg"]')
        open_options.click()
        check_in_element = self.find_element('css selector',f'td[data-date="{check_in}"]')
        check_in_element.click()
        check_out_element = self.find_element('css selector',f'td[data-date="{check_out}"]')
        check_out_element.click()
        #time.sleep(2)
        # data-date="2023-03-15"

    def select_adults(self,no_of_adults=1):
        if(no_of_adults)<1:
            no_of_adults=1
        open_options = self.find_element('id','xp__guests__toggle')
        open_options.click()

        default_adults = self.find_element('css selector','span[data-bui-ref="input-stepper-value"]').text
        if(int(default_adults) > no_of_adults):
            subtract_btn = self.find_element('css selector','button[data-bui-ref="input-stepper-subtract-button"]')
            loop = int(default_adults)-no_of_adults
            for i in range(loop):
                subtract_btn.click()
        elif(int(default_adults) < no_of_adults):
            add_btn = self.find_element('css selector', 'button[data-bui-ref="input-stepper-add-button"]')
            loop = no_of_adults - int(default_adults)
            for i in range(loop):
                add_btn.click()


        time.sleep(3)

    def search(self):
        search_button = self.find_element('css selector','button[type="submit"]')
        search_button.click()
        time.sleep(2)

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(4, 5)
        time.sleep(10)
