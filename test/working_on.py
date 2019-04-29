def test_apk_subskrybenci_logowanie(self):
    self.driver.find_element_by_xpath("//android.widget.TextView[@text='Polska']").click()
    checkbox = self.driver.find_element_by_id('eu.hbogo.android:id/iv_tick')
    self.assertTrue(checkbox.is_enabled())
    self.driver.find_element_by_xpath('//android.widget.Button[@text="NEXT"]').click()
    self.driver.find_element_by_xpath('//android.view.View[@content-desc="Subskrybenci"]').click()
    textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
    textfields[0].send_keys('adamnowak@gmail.com')
    textfields[1].send_keys('QAZwsx1!')
    self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zaloguj się"]').click()
    info = self.driver.find_element_by_xpath(
        '//android.view.View[@content-desc="Błędna nazwa użytkownika lub hasło (12.20)"]').get_attribute(
        'contentDescription')
    self.assertEqual(u'Błędna nazwa użytkownika lub hasło (12.20)', info)
    sleep(3)


def test_apk_abonenci_odzyskiwanie_hasla(self):
    self.driver.find_element_by_xpath("//android.widget.TextView[@text='Polska']").click()
    checkbox = self.driver.find_element_by_id('eu.hbogo.android:id/iv_tick')
    self.assertTrue(checkbox.is_enabled())
    self.driver.find_element_by_xpath('//android.widget.Button[@text="NEXT"]').click()
    self.driver.find_element_by_xpath('//android.view.View[@content-desc="Abonenci HBO GO u operatorów"]').click()
    self.driver.find_element_by_class_name('android.widget.Spinner').click()
    providers = self.driver.find_element_by_class_name('android.widget.ListView')
    self.assertTrue(providers.is_displayed())
    self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="nc+"]').click()
    self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zapomniałeś hasła?"]').click()
    sleep(3)
    textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
    textfields[2].send_keys('adamnowak@gmail.com')
    self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Wyślij link resetu hasła"]').click()
    info = self.driver.find_element_by_xpath(
        '//android.view.View[@content-desc='
        '"Klient nie został znaleziony w bazie serwisu HBO GO. (4.65)"]').get_attribute(
        'contentDescription')
    self.assertEqual(u'Klient nie został znaleziony w bazie serwisu HBO GO. (4.65)', info)
    sleep(3)


def test_apk_subskrybenci_odzyskiwanie_hasla(self):
    self.driver.find_element_by_xpath("//android.widget.TextView[@text='Polska']").click()
    checkbox = self.driver.find_element_by_id('eu.hbogo.android:id/iv_tick')
    self.assertTrue(checkbox.is_enabled())
    self.driver.find_element_by_xpath('//android.widget.Button[@text="NEXT"]').click()
    self.driver.find_element_by_xpath('//android.view.View[@content-desc="Subskrybenci"]').click()
    self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zapomniałeś hasła?"]').click()
    sleep(3)
    textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
    textfields[2].send_keys('adamnowak@gmail.com')
    self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Wyślij link resetu hasła"]').click()
    info = self.driver.find_element_by_xpath(
        '//android.view.View[@content-desc="Wystąpił błąd podczas autentykacji użytkownika (12.99)"]').get_attribute(
        'contentDescription')
    self.assertEqual(u'Wystąpił błąd podczas autentykacji użytkownika (12.99)', info)
    sleep(3)


def test_apk_abonenci_validacja(self):
    self.driver.find_element_by_xpath("//android.widget.TextView[@text='Polska']").click()
    checkbox = self.driver.find_element_by_id('eu.hbogo.android:id/iv_tick')
    self.assertTrue(checkbox.is_enabled())
    self.driver.find_element_by_xpath('//android.widget.Button[@text="NEXT"]').click()
    self.driver.find_element_by_xpath('//android.view.View[@content-desc="Abonenci HBO GO u operatorów"]').click()
    self.driver.find_element_by_class_name('android.widget.Spinner').click()
    providers = self.driver.find_element_by_class_name('android.widget.ListView')
    self.assertTrue(providers.is_displayed())
    self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="nc+"]').click()
    self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zaloguj się"]').click()
    sleep(3)
    info_mail = self.driver.find_element_by_xpath(
        '//android.view.View[@content-desc="Adres e-mail jest wymagany"]').get_attribute(
        'contentDescription')
    self.assertEqual(u'Adres e-mail jest wymagany', info_mail)
    textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
    textfields[0].send_keys('adamnowak@gmail.com')
    filled_field_mail = self.driver.find_element_by_xpath('//android.widget.EditText[@text="adamnowak@gmail.com"]')
    self.assertEqual(filled_field_mail.text, 'adamnowak@gmail.com')
    self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zaloguj się"]').click()
    sleep(3)
    info_haslo = self.driver.find_element_by_xpath(
        '//android.view.View[@content-desc="Hasło jest wymagane"]').get_attribute(
        'contentDescription')
    self.assertEqual(u'Hasło jest wymagane', info_haslo)
    textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
    textfields[1].send_keys('QAZwsx1!')
    filled_field_haslo = self.driver.find_element_by_xpath(
        '//android.widget.EditText[@text="••••••••"]').get_attribute('text')
    self.assertEqual(filled_field_haslo, u'••••••••')
    sleep(3)


def test_apk_subskrybenci_validacja(self):
    self.driver.find_element_by_xpath("//android.widget.TextView[@text='Polska']").click()
    checkbox = self.driver.find_element_by_id('eu.hbogo.android:id/iv_tick')
    self.assertTrue(checkbox.is_enabled())
    self.driver.find_element_by_xpath('//android.widget.Button[@text="NEXT"]').click()
    self.driver.find_element_by_xpath('//android.view.View[@content-desc="Subskrybenci"]').click()
    self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zaloguj się"]').click()
    sleep(3)
    info_mail = self.driver.find_element_by_xpath('//android.widget.EditText[@text="E-mail"]')
    self.assertTrue(info_mail.is_displayed())
    textfield = self.driver.find_elements_by_class_name('android.widget.EditText')
    textfield[0].send_keys('adamnowak@gmail.com')
    filled_field_mail = self.driver.find_element_by_xpath('//android.widget.EditText[@text="adamnowak@gmail.com"]')
    self.assertEqual(filled_field_mail.text, 'adamnowak@gmail.com')
    self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zaloguj się"]').click()
    sleep(3)
    info_haslo = self.driver.find_element_by_xpath('//android.widget.EditText[@text="Hasło"]')
    self.assertTrue(info_haslo.is_displayed())
    textfield = self.driver.find_elements_by_class_name('android.widget.EditText')
    textfield[1].send_keys('QAZwsx1!')
    filled_field_haslo = self.driver.find_element_by_xpath(
        '//android.widget.EditText[@text="••••••••"]').get_attribute('text')
    self.assertEqual(filled_field_haslo, u'••••••••')
    sleep(3)



    def test_invalid_user_abo(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Polska']").click()
        self.driver.find_element_by_xpath('//android.widget.Button[@text="NEXT"]').click()
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="Abonenci HBO GO u operatorów"]').click()
        self.driver.find_element_by_class_name('android.widget.Spinner').click()
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="nc+"]').click()
        textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
        textfields[0].send_keys('adamnowak@gmail.com')
        textfields[1].send_keys('QAZwsx1!')
        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zaloguj się"]').click()
        info = self.driver.find_element_by_xpath(
            '//android.view.View[@content-desc="Błędna nazwa użytkownika lub hasło (12.20)"]').get_attribute(
            'contentDescription')
        self.assertEqual(u'Błędna nazwa użytkownika lub hasło (12.20)', info)
        sleep(3)


    def test_elements_check_abo(self):
        app_title = self.driver.find_element_by_xpath(
            '//android.widget.ImageView[@resource-id="eu.hbogo.android:id/iv_country_selector_logo"]')
        self.assertTrue(app_title.is_displayed())
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Polska"]').click()
        checkbox = self.driver.find_element_by_id('eu.hbogo.android:id/iv_tick')
        self.assertTrue(checkbox.is_enabled())
        nextbutton = self.driver.find_element_by_xpath('//android.widget.Button[@text="NEXT"]')
        self.assertTrue(nextbutton.is_displayed())
        nextbutton.click()
        abo_a = self.driver.find_element_by_android_uiautomator(
            'UiSelector().description("Abonenci HBO GO u operatorów")').get_attribute('contentDescription')
        self.assertEqual(u'Abonenci HBO GO u operatorów', abo_a)
        abo_b = self.driver.find_element_by_android_uiautomator(
            'UiSelector().description("Jeśli masz abonament wykupiony u operatora")').get_attribute(
            'contentDescription')
        self.assertEqual(u'Jeśli masz abonament wykupiony u operatora', abo_b)
        field = self.driver.find_element_by_android_uiautomator(
            'UiSelector().resourceId("gw_operator_type_signin_b2b")')
        self.assertTrue(field.is_enabled())
        field.click()
        self.driver.find_element_by_class_name('android.widget.Spinner').click()
        providers = self.driver.find_element_by_class_name('android.widget.ListView')
        self.assertTrue(providers.is_displayed())
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="nc+"]').click()
        twoj_oper = self.driver.find_element_by_xpath(
            '//android.view.View[@content-desc="Twój operator"]').get_attribute(
            'contentDescription')
        self.assertEqual(u'Twój operator', twoj_oper)
        adres_e = self.driver.find_element_by_xpath(
            '//android.view.View[@content-desc="Adres e-mail"]').get_attribute(
            'contentDescription')
        self.assertEqual(u'Adres e-mail', adres_e)
        haslo = self.driver.find_element_by_xpath(
            '//android.view.View[@content-desc="Hasło"]').get_attribute(
            'contentDescription')
        self.assertEqual(u'Hasło', haslo)
        zalog = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zaloguj się"]')
        self.assertTrue(zalog.is_displayed())
        zap_has = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zapomniałeś hasła?"]')
        self.assertTrue(zap_has.is_displayed())
        zalog.click()
        sleep(3)
        info_mail = self.driver.find_element_by_xpath(
            '//android.view.View[@content-desc="Adres e-mail jest wymagany"]').get_attribute(
            'contentDescription')
        self.assertEqual(u'Adres e-mail jest wymagany', info_mail)
        textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
        textfields[0].send_keys('adamnowak@gmail.com')
        filled_field_mail = self.driver.find_element_by_xpath('//android.widget.EditText[@text="adamnowak@gmail.com"]')
        self.assertEqual(filled_field_mail.text, 'adamnowak@gmail.com')
        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zaloguj się"]').click()
        sleep(3)
        info_haslo = self.driver.find_element_by_xpath(
            '//android.view.View[@content-desc="Hasło jest wymagane"]').get_attribute(
            'contentDescription')
        self.assertEqual(u'Hasło jest wymagane', info_haslo)
        textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
        textfields[1].send_keys('00000000')
        filled_field_haslo = self.driver.find_element_by_xpath(
            '//android.widget.EditText[@text="••••••••"]').get_attribute('text')
        self.assertEqual(filled_field_haslo, u'••••••••')
        sleep(3)



