from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@given('the user is logged in with username "{username}" and password "{password}"')
def step_impl(context,username,password):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    username_field = context.driver.find_element(By.ID, "user-name")
    username_field.send_keys(username)
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()
    inventory_container = context.driver.find_element(By.ID, "inventory_container")
    assert inventory_container.is_displayed(), "Inventory container is not displayed"

@when('the user add Sauce Lab Backpack to the cart')
def step_impl(context):
    atc_SauceLabBackpack_button = context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    atc_SauceLabBackpack_button.click()

@when('the user adds "{count}" items to the Cart')
def step_impl(context, count):
    count = int(count)
    add_to_cart_btns = context.driver.find_elements(By.CSS_SELECTOR, ".inventory_item button.btn_inventory")
    for btn in add_to_cart_btns[:count]:
        btn.click()

@then('the cart badge should show "{count}"')
def step_impl(context, count):
    cart_badge = context.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
    assert cart_badge.text == count, f"Cart badge shows {cart_badge.text} instead of {count}"
    time.sleep(5)
    context.driver.quit()

@when('the user removes "{count}" items from the cart')
def step_impl(context,count):
    count = int(count)
    remove_button = context.driver.find_element(By.CSS_SELECTOR, ".cart_item button.cart_button")
    for btn in remove_button[:count]:
        btn.click()

@when('the user click the cart button')
def step_impl(context):
    cart_button = context.driver.find_element(By.ID, "shopping_cart_container")
    cart_button.click()
# def step_impl(context, count):
#     count = int(count)
#     logger.info(f"Attempting to remove {count} items from the cart.")
#     for _ in range(count):
#         try:
#             # Wait for cart page to be available
#             cart_link = WebDriverWait(context.driver, 10).until(
#                 EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
#             )
#             cart_link.click()
#             # Wait for remove buttons to be present
#             remove_buttons = WebDriverWait(context.driver, 10).until(
#                 EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cart_item button.cart_button"))
#             )
#             logger.info(f"Found {len(remove_buttons)} remove buttons.")
#             if remove_buttons:
#                 # Click the first available remove button
#                 remove_buttons[0].click()
#                 logger.info("Removed one item from the cart.")
#         except Exception as e:
#             logger.error(f"Error clicking remove button: {e}")