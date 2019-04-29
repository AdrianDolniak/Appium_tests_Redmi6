#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))

class TestowaniePowiadomien(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_caps = {
            'deviceName': 'Redmi6',
            'udid': 'a49b96de7d28',
            'platformName': 'Android',
            'platformVersion': '8.1',
            'skipUnlock': 'true',
            'app': PATH('/home/adi/Appium/apps/API Demos for Android_v1.9.0_apkpure.com.apk'),
            'appPackage': 'com.touchboarder.android.api.demos',
            'appActivity': 'com.touchboarder.androidapidemos.MainActivity',
            'fullReset': False
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test_powiadomien(self):
        self.driver.open_notifications()
        sleep(3)
        elements = self.driver.find_elements_by_class_name('android.widget.TextView')
        title = False  # zmienna pomocnicza
        body = False  # zmienna pomocnicza
        for el in elements:
            text = el.text
            if text == u'Podłączono moduł debugowania USB':
                title = True
            elif text == u'Kliknij, by wyłączyć debugowanie USB.':
                body = True
        self.assertTrue(title)
        self.assertTrue(body)
        self.driver.keyevent(4)



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowaniePowiadomien)
    unittest.TextTestRunner(verbosity=2).run(suite)
