from selenium import webdriver
import unittest
import HtmlTestRunner

class orangeHRMTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("executable_path"=="C:\Drivers\chromedriver_win32\chromedriver.exe")
        cls.driver.maximize_window()
    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM",self.driver.title,"webpage is not matching")
    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
        self.driver.find_element(By.NAME,"txtPassword").send_keys("admin123")
        self.driver.find_element(By.NAME,"Submit").click()
        self.assertEqual("OrangeHRM",self.driver.title,"webpage is not matching")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("TEST COMPLETED.....")


if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))
    