from seleniumbase import BaseCase

class ContactTest(BaseCase):
    # tutaj ojciec dodał przykład logownia przed testem, tak jak Pan Hindus kazał
    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")

        # LOGIN
        self.open('https://practice.automationbro.com/my-account/')
        self.add_text('#username', 'hubertxiaomiarchiwum001')
        self.add_text('#password', 'testuser123!')
        self.click('#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button')
        self.assert_text('Log out', '#post-9 > div > div > div > p:nth-child(2) > a')

        # open home page
        self.open("https://practice.automationbro.com")

    def test_contact_page(self):
        # open page
        self.open("https://practice.automationbro.com/contact")

        #scroll to the empty form and take screenshot
        self.scroll_to("#evf-form-277")
        self.save_screenshot("empty_contact_form", "custom_screenshots")

        # fill in all the fields
        self.send_keys('#evf-277-field_ys0GeZISRs-1', 'Test Name')
        self.send_keys('#evf-277-field_LbH5NxasXM-2', 'test@mail.com')
        self.send_keys('#evf-277-field_66FR384cge-3', '555555555')
        self.send_keys('#evf-277-field_yhGx3FOwr2-4', 'Żydzi Kurwy')

        # take the screenshot when the form is filled
        self.scroll_to("#evf-form-277")
        self.save_screenshot("filled_contact_form", "custom_screenshots")

        # click the submit button
        self.click('#evf-submit-277')

        # verify submit message
        self.assert_text("Thanks for contacting us! We will be in touch with you shortly", '#primary > div > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-e2bbe43.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div > div > div > section.elementor-section.elementor-inner-section.elementor-element.elementor-element-c58f8f7.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div.elementor-column.elementor-col-33.elementor-inner-column.elementor-element.elementor-element-7648d39 > div > div > div > div > div > div > div')

        # 2h 31min HINDUS ROBIMY SCREENY, musze przesunac do gory lekko drugi screen bozy