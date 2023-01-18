from seleniumbase import BaseCase

class HomePage(BaseCase):
    logo_icon = ".custom-logo-link"
    get_started_btn = "#get-started"
    heading_text = "h1"
    copyright_text = ".tg-site-footer-section-1"
    menu_links = "//*[starts-with(@id, 'menu-item')]"
    username = '#username'

    def open_page(self):
        self.open("https://practice.automationbro.com")

    def login(self):
        self.open('https://practice.automationbro.com/my-account/')
        self.add_text(self.username, 'hubertxiaomiarchiwum001')
        self.add_text('#password', 'testuser123!')
        self.click('#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button')
        self.assert_text('Log out', '#post-9 > div > div > div > p:nth-child(2) > a')