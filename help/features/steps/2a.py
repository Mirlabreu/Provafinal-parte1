from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import time

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)


@given("a user accesses the home page")
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'utils', 'driver', 'chromedriver.exe'))
    context.driver.get("https://test.jasgme.com/pt/login")
    context.driver.maximize_window()


@when("the user clicks the question mark symbol")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("mirla.santos@dellead.com")

    password_field = context.driver.find_element_by_id("inputPassword")
    password_field.send_keys("abcd1234")

    login_button = context.driver.find_element_by_id("btnLogin")
    login_button.click()

    wait = WebDriverWait(context.driver, 15)
    question_mark = wait.until(
        EC.element_to_be_clickable((By.ID, 'helpers')))
    question_mark.click()


@then("the system displays a list of help options")
def then(context):

    wait = WebDriverWait(context.driver, 30)
    wait.until(EC.presence_of_element_located((By.XPATH,
                                                    '/html/body/app-root/app-sidebar-layout/div/div/app-help-center'
                                                    '/div/app-custom-card/div/div[2]/div/app-custom-card[1]/div/div['
                                                    '1]/span[1]')))
    time.sleep(5)
    context.driver.quit()