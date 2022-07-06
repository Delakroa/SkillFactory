Introduction
------------

This repository contains basic example of usage PageObject
pattern with Selenium and Python (PyTest + Selenium).


Files
-----

[conftest.py](conftest.py) contains all the required code to catch failed test cases.

[pages/base_page.py](pages/base_page.py) contains PageObject pattern implementation for Python.

[pages/locators.py](pages/locators.py) contains helper class to define web elements on web pages.

[tests/test_selenium_Oscar_Sandbox
.py](tests/test_selenium_Oscar_Sandbox
.py) contains several smoke Web UI tests for Oscar_Sandbox.
py Store 
(https://latest.oscarcommerce.com/ru/catalogue/)


How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
    ```


Note:
~/chrome in this example is the file of Selenium WebDriver downloaded and unarchived on step #2.
