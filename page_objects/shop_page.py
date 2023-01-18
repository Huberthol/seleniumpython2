from seleniumbase import BaseCase

class ShopPage(BaseCase):
    search_input = '#woocommerce-product-search-field-0'
    search_btn = '#woocommerce_product_search-1 > form > button'
    product_img = '//*[@id="product-375"]/div[1]/figure/div/a'
    no_products_txt = '//*[@id="primary"]/p'

    def open_page(self):
        self.open("https://practice.automationbro.com/shop/")
