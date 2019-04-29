#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))

class Testowanie_aplikacji_HBOGO(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8.1',
            'deviceName': 'Redmi6',
            'udid': 'a49b96de7d28',
            'automationName': 'UiAutomator2',
            'otherApps': PATH('/home/adi/Appium/apps/HBO GO_v5.6.0_apkpure.com.apk'),
            'appPackage': 'eu.hbogo.android',
            'appActivity': 'eu.hbogo.android.setup.activity.SetUpActivity',
            'noReset': False
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)


    def tearDown(self):
       self.driver.quit()


    def test_apk_abonenci_logowanie_invalid_user(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Polska']").click()
        checkbox = self.driver.find_element_by_id('eu.hbogo.android:id/iv_tick')
        self.assertTrue(checkbox.is_enabled())
        self.driver.find_element_by_xpath('//android.widget.Button[@text="NEXT"]').click()
        self.driver.find_element_by_xpath('//android.view.View[@text="Abonenci HBO GO u operatorów"]').click()
        self.driver.find_element_by_class_name('android.widget.Spinner').click()
        providers = self.driver.find_element_by_class_name('android.widget.ListView')
        self.assertTrue(providers.is_displayed())
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="nc+"]').click()
        textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
        textfields[0].send_keys('adamnowak@gmail.com')
        textfields[1].send_keys('QAZwsx1!')
        self.driver.find_element_by_xpath('//android.widget.Button[@text="Zaloguj się"]').click()
        info = self.driver.find_element_by_xpath(
            '//android.view.View[@text="Błędna nazwa użytkownika lub hasło (12.20)"]').get_attribute(
            'text')
        self.assertEqual(u'Błędna nazwa użytkownika lub hasło (12.20)', info)
        sleep(3)



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Testowanie_aplikacji_HBOGO)
    unittest.TextTestRunner(verbosity=2).run(suite)
