from selenium.webdriver.common.by import By

def test_cart_button_existence(browser):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    element = browser.find_elements(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    assert len(element) > 0, 'No such element'