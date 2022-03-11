from selenium import webdriver
import time
import unittest
from Multibrowser import Pagelocators

class SearchTest(unittest.TestCase):


    # def driver(cls):
    #     cls.driver = webdriver.Chrome(executable_path='C:\\Users\\BEST\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe')
    #     cls.driver.implicitly_wait(10)
    #     cls.driver.maximize_window()
    #

    def test_search(self):
            self.driver = webdriver.Chrome(executable_path='C:\\Users\\BEST\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe')
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

            self.driver.get("https://www.seleniumeasy.com/")
            pageLoc_obj = Pagelocators()
            pageLoc_obj.input_search_field()
            # self.driver.find_element_by_id("edit-search-block-form--2") .send_keys("interview")
            # self.driver.find_element_by_class_name("input-group-btn").click()
            pageLoc_obj.click_search_button()
            assert "interview" in self.driver.current_url
            # results = self.driver.find_elements_by_class_name("search-result")
            # for x in results:
            #     title = str(x.text).lower()
            #     print(title)
            #     assert title.find("interview") in self.driver.find_elements_by_class_name("search-result")
            #
            time.sleep(2)



    @classmethod
    def tearDownClass(cls):

            cls.driver.close();
            cls.driver.quit();






















