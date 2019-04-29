import os
import unittest
from appium import webdriver
from time import sleep


PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))

class TestowanieFormularza(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_caps = {
            'deviceName': 'Redmi6',
            'udid': 'a49b96de7d28',
            'platformName': 'Android',
            'platformVersion': '8.1',
            'app': PATH('/home/adi/Appium/apps/ContactManager.apk'),
            'appPackage': 'com.example.android.contactmanager',
            'appActivity': 'com.example.android.contactmanager.ContactManager',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'fullReset': False
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test_formularza(self):
        el = self.driver.find_element_by_accessibility_id('Add Contact')
        el.click()
        textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
        textfields[0].send_keys('Jan Nowak')
        textfields[1].send_keys('444222333')
        textfields[2].send_keys('jan@gmail.com')
        self.assertEqual('444222333', textfields[1].text)
        self.assertEqual('jan@gmail.com', textfields[2].text)

        el = self.driver.find_element_by_class_name('android.widget.Button')
        el.click()

        sleep(3)




if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieFormularza)
    unittest.TextTestRunner(verbosity=2).run(suite)