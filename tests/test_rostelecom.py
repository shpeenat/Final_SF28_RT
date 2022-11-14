from pagesRT.rt_page import AuthPage
import time


def test_EXP001_RT_page(driver):
    page = AuthPage(driver)
    page.driver.save_screenshot('RT_page.png')


def test_EXP002_RT_with_correct_data(driver):
    page = AuthPage(driver)
    page.enter_email('makar_85@mail.ru')
    page.enter_pass('Makar1234')
    page.btn_click()
    time.sleep(3)
    page.driver.save_screenshot('RT_Makar85.png')


def test_EXP003_RT_with_incorrect_email(driver):
    page = AuthPage(driver)
    page.enter_email('test@mail.ru')
    page.enter_pass('test1234')
    page.btn_click()
    page.driver.save_screenshot('RT_Incorrect_email.png')


def test_EXP004_RT_with_incorrect_pass(driver):
    page = AuthPage(driver)
    page.enter_email('makar_85@mail.ru')
    page.enter_pass('Makar2345')
    page.btn_click()
    page.driver.save_screenshot('RT_Incorrect_PW.png')


def test_EXP005_RT_vk(driver):
    page = AuthPage(driver)
    page.link_vk.click()
    page.driver.save_screenshot('RT_VK_link.png')


def test_EXP006_RT_ok(driver):
    page = AuthPage(driver)
    page.link_ok.click()
    page.driver.save_screenshot('RT_OK_link.png')


def test_EXP007_RT_Mail(driver):
    page = AuthPage(driver)
    page.link_mail.click()
    page.driver.save_screenshot('RT_Mail_link.png')


def test_EXP008_RT_Google(driver):
    page = AuthPage(driver)
    page.link_google.click()
    page.driver.save_screenshot('RT_Google_link.png')


def test_EXP009_RT_Ya(driver):
    page = AuthPage(driver)
    page.link_ya.click()
    page.driver.save_screenshot('RT_Ya_link.png')


def test_EXP010_RT_Cookies(driver):
    page = AuthPage(driver)
    page.link_cookie.click()
    page.driver.save_screenshot('RT_Cookies.png')


def test_EXP011_RT_CP(driver):
    page = AuthPage(driver)
    page.link_cp.click()
    time.sleep(1)
    page.driver.save_screenshot('RT_CP_link.png')


def test_EXP012_RT_register(driver):
    page = AuthPage(driver)
    page.link_reg.click()
    page.driver.save_screenshot('RT_register_link.png')
