import time

from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)


@given("a user accesses the platform homepage (3a)")
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'utils', 'driver', 'chromedriver.exe'))
    context.driver.get("https://test.jasgme.com/pt/login")
    context.driver.maximize_window()

@when("the user clicks editions")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("mirla.santos@dellead.com")

    password_field = context.driver.find_element_by_id("inputPassword")
    password_field.send_keys("abcd1234")

    login_button = context.driver.find_element_by_id("btnLogin")
    login_button.click()

    wait = WebDriverWait(context.driver, 30)
    editions_menu = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/app-root/app-sidebar-layout/div/nav/div/div[2]/ul[1]/li[2]/a')))
    editions_menu.click()

    time.sleep(5)


@then("the system displays the list of registered editions")
def then(context):
    wait = WebDriverWait(context.driver, 30)
    wait.until(EC.presence_of_element_located((By.ID, 'name')))
    context.driver.quit()
