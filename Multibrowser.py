from selenium.webdriver.common.by import By


class Pagelocators(driver):
     search_field = (By.ID, "edit-search-block-form--2")
     search_button = (By.CLASS_NAME, "input-group-btn")
     search_result = (By.CLASS_NAME, "search-result")


     def input_search_field(self):
          search_field = self.driver.find_element("search_field")
          search_field.send_keys("interview")

     def click_search_button(self):
          search_button = self.driver.find_element("search_button")
          search_button.click()

     # def searching_result(self):
     #       search_result = self.driver.find_elements("search-result")






