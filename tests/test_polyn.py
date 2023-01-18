from seleniumbase import BaseCase
import time

class ZydTest(BaseCase):

    def test_polyn(self):
        #otwórz stornkę bożą
        self.open("https://doxbin.com/")

        time.sleep(10)

        tabela = '/html/body/div[1]/div[2]/table[2]'
        czlowiek = '/html/body/div[1]/div[2]/table[2]/tbody/tr[1]/td[1]/a'

        #kliknij

        zmienna = self.get_text(tabela)
        print(zmienna)
