from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('the user is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome() 
    context.driver.get("https://www.saucedemo.com/")

@when('the user enters the username "{username}"')
def step_impl(context, username):
    username_field = context.driver.find_element(By.ID, "user-name")
    username_field.send_keys(username)

@when('the user enters the password "{password}"')
def step_impl(context, password):
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys(password)

@when('the user clicks the login button')
def step_impl(context):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()

@then('the user should see the products page')
def step_impl(context):
    inventory_container = context.driver.find_element(By.ID, "inventory_container")
    assert inventory_container.is_displayed()
    context.driver.quit()

@then('the user should see an error message')
def step_impl(context):
    error_message = context.driver.find_element(By.CSS_SELECTOR, ".error-message-container")
    assert error_message.is_displayed()
    context.driver.quit()

@then('the user should see a username is required error message')
def step_impl(context):
    error_message = context.driver.find_element(By.CSS_SELECTOR, ".error-message-container")
    assert "Username is required" in error_message.text, "Expected error message not found"
    context.driver.quit()

@then('the user should see a password is required error message')
def step_impl(context):
    error_message = context.driver.find_element(By.CSS_SELECTOR, ".error-message-container")
    assert "Password is required" in error_message.text, "Expected error message not found"
    context.driver.quit()