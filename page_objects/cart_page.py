from seleniumbase import BaseCase

class CartPage(BaseCase):
    converse_add_to_cart_btn = '//*[@id="primary"]/ul/li[3]/a[2]'
    cart_count_text = '#header-action > ul > li.menu-item.tg-menu-item.tg-menu-item-cart > a > span'
    subtotal_text = '//*[@id="post-7"]/div/div[2]/div[2]/div/table/tbody/tr[1]/td/span/bdi'
    product_quantity_input = '/html/body/div[1]/main/div/div/div/article/div/div[2]/form/table/tbody/tr[1]/td[5]/div/input'
    update_cart_btn = '//*[@id="post-7"]/div/div[2]/form/table/tbody/tr[2]/td/button'
    loading_overlay = ".woocommerce-cart-form div[class*='blockOverlay']"
    #proceed_to_checkout_btn = '/html/body/div[1]/main/div/div/div/article/div/div[2]/div[2]/div/div/a'

    def open_page(self):
        self.open("https://practice.automationbro.com/cart/")



