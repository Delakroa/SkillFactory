from base import WebPage
from elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://www.labirint.ru/cabinet/'
        super().__init__(web_driver, url)

    email = WebElement(id='_inputnamecode_59')  # skillfaktory.qap66@gmail.com

    btn_1 = WebElement(id='g-recap-0-btn')

    password = WebElement(id='_inputnamecode_28')  # 7370377

    btn_2 = WebElement(class_name='new-auth__button.js-submitnew-auth__input.full-input__input.new-forms__input_size_m')
