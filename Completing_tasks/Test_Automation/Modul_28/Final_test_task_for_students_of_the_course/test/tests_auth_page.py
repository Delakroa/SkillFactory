
# python -m pytest -v --driver Chrome --driver-path
# E:\python_library\SkillFaktory\SkillFactory_practice\Completing_tasks\Test_Automation\Modul_28\Final_test_task_for_students_of_the_course\chromedriver.exe
import pytest
from page.auth_page import AuthPage


def test_authorisation(browser):
    page = AuthPage(browser)

    page.email.send_keys('skillfaktory.qap66@gmail.com')

    page.btn1.click()

    page.password.send_keys("2600-421A-95EF")

    page.btn2.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/'