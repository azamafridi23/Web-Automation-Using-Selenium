#This file will include a class with instance methods.
#That will be responsible to interact with our website
#After we have some results, to apply filtrations.
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
    def __init__(self, driver:WebDriver): # here we have specified that the type of driver variable has been specified which is of type 'WebDriver'. so that when we press .(dot) we get its methods list
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element('id','filter_group_class_:R1cq:')
        star_child_elements = star_filtration_box.find_elements('css selector','*') # gives me all child elements of id='filter_class' tag

        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()
