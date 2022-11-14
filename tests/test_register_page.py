from pagesRT.register_page import RegPage
import time
from selenium.webdriver.common.by import By


def test_contents_register_page(driver):
    page = RegPage(driver)
    page.link_reg.click()
    page.driver.save_screenshot('Register_page.png')


def test_FirstName_register_page(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('Тест')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.click()
    page.driver.save_screenshot('FN_register_page.png')


def test_FirstName_register_1_symbol(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('Т')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.click()
    page.driver.save_screenshot('FN_1symbol.png')


def test_FirstName_register_12_symbols(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('ТестТестТестТест')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.click()
    page.driver.save_screenshot('FN_12symbols.png')


def test_FirstName_register_24_symbols(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('ТестТестТестТестТестТест')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.click()
    page.driver.save_screenshot('FN_24symbols.png')


def test_FirstName_register_Latinica_symbols(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('Test')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.click()
    page.driver.save_screenshot('FN_Lat_sym.png')


def test_LastName_register_page(driver):
    page = RegPage(driver)
    page.link_reg.click()
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.clear()
    lastname.send_keys('Тестовый')
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.click()
    page.driver.save_screenshot('LN_register_page.png')


def test_LastName_register_1_symbol(driver):
    page = RegPage(driver)
    page.link_reg.click()
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.clear()
    lastname.send_keys('Т')
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.click()
    page.driver.save_screenshot('LN_1symbol.png')


def test_LastName_register_12_symbols(driver):
    page = RegPage(driver)
    page.link_reg.click()
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.clear()
    lastname.send_keys('ТестовыйТест')
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.click()
    page.driver.save_screenshot('LN_12symbols.png')


def test_LastName_register_24_symbols(driver):
    page = RegPage(driver)
    page.link_reg.click()
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.clear()
    lastname.send_keys('ТестовыйТестовыйТестовый')
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.click()
    page.driver.save_screenshot('LN_24symbols.png')


def test_LastName_register_Latinica_symbols(driver):
    page = RegPage(driver)
    page.link_reg.click()
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.clear()
    lastname.send_keys('Testoviy')
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.click()
    page.driver.save_screenshot('LN_Lat_sym.png')


def test_Email_register_page(driver):
    page = RegPage(driver)
    page.link_reg.click()
    email = driver.find_element(By.ID, 'address')
    email.clear()
    email.send_keys('makar_85@mail.ru')
    password = driver.find_element(By.ID, 'password')
    password.click()
    page.driver.save_screenshot('Email_register_page.png')


def test_Password_register_page(driver):
    page = RegPage(driver)
    page.link_reg.click()
    password = driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys('Makar1234')
    pass_con = driver.find_element(By.ID, 'password-confirm')
    pass_con.click()
    page.driver.save_screenshot('PW_register_page.png')


def test_Password_confirm_register_page(driver):
    page = RegPage(driver)
    page.link_reg.click()
    pass_con = driver.find_element(By.ID, 'password-confirm')
    pass_con.clear()
    pass_con.send_keys('Makar1234')
    password = driver.find_element(By.ID, 'password')
    password.click()
    page.driver.save_screenshot('PW_confirm_register_page.png')


def test_Registration_correct_data(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('Тест')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.clear()
    lastname.send_keys('Тестовый')
    email = driver.find_element(By.ID, 'address')
    email.clear()
    email.send_keys('makar_85@mail.ru')
    password = driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys('Makar1234')
    pass_con = driver.find_element(By.ID, 'password-confirm')
    pass_con.clear()
    pass_con.send_keys('Makar1234')
    btn = driver.find_element(By.NAME, 'register')
    btn.click()
    time.sleep(10)
    page.driver.save_screenshot('Registration.png')


def test_Registration_correct_data_repeat(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('Тест')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.clear()
    lastname.send_keys('Тестовый')
    email = driver.find_element(By.ID, 'address')
    email.clear()
    email.send_keys('makar_85@mail.ru')
    password = driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys('Makar1234')
    pass_con = driver.find_element(By.ID, 'password-confirm')
    pass_con.clear()
    pass_con.send_keys('Makar1234')
    btn = driver.find_element(By.NAME, 'register')
    btn.click()
    time.sleep(10)
    page.driver.save_screenshot('Registration2.png')


def test_Registration_different_PW(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('Тест')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.clear()
    lastname.send_keys('Тестовый')
    email = driver.find_element(By.ID, 'address')
    email.clear()
    email.send_keys('makar_85@mail.ru')
    password = driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys('Makar1234')
    pass_con = driver.find_element(By.ID, 'password-confirm')
    pass_con.clear()
    pass_con.send_keys('Makar2345')
    btn = driver.find_element(By.NAME, 'register')
    btn.click()
    page.driver.save_screenshot('Registration_diff_PW.png')


def test_Registration_No_Data(driver):
    page = RegPage(driver)
    page.link_reg.click()
    btn = driver.find_element(By.NAME, 'register')
    btn.click()
    page.driver.save_screenshot('Registration_No_Data.png')


def test_Registration_cookie(driver):
    page = RegPage(driver)
    page.link_reg.click()
    cookie = driver.find_element(By.XPATH, '//*[@id="app-footer"]/div[1]/div[2]/span/span')
    cookie.click()
    time.sleep(1)
    page.driver.save_screenshot('Registration_cookie.png')


def test_Registration_CP(driver):
    page = RegPage(driver)
    page.link_reg.click()
    cp = driver.find_element(By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')
    cp.click()
    time.sleep(1)
    page.driver.save_screenshot('Registration_CP.png')