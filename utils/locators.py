from selenium.webdriver.common.by import By


class SignInPageLocator(object):
    email = (By.XPATH, "//input[@id='tl_login']")
    password = (By.XPATH, "//input[@id='tl_password']")
    signInBtn = (By.XPATH, "//input[@id='tl_login_button']")
