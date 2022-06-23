from base import WebPage
from elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://www.ozon.ru/'
        super().__init__(web_driver, url)

    email = WebElement(id='email')    # skillfaktory.qap66@gmail.com

    password = WebElement(id='pass')  # 7370377

    btn = WebElement(class_name='btn.btn-success')
