import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators, LoginPageLocators  
from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
    login_link = browser.find_element(*MainPageLocators.LOGIN_LINK)
    login_link.click()
    
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()  

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


    
   










