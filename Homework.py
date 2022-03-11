from selenium import webdriver
import time
import unittest

class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:\\Users\\BEST\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_search(self):
            self.driver.get("https://www.seleniumeasy.com/")
            self.driver.find_element_by_id("edit-search-block-form--2").send_keys("interview")
            self.driver.find_element_by_class_name("input-group-btn").click()
            assert "interview" in self.driver.current_url
            results = self.driver.find_elements_by_css_selector(".search-result>.title")
            for x in results:
                title = x.text.lower()
                # if("interview" in title):
                print(title, "________")
                assert "interview" in title
                #assert title.find("interview") in self.driver.find_elements_by_class_name("search-result")



    @classmethod
    def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
















