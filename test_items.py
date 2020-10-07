import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button_is_enable(browser):
    browser.get(link)
    button_basket = browser.find_element_by_class_name("btn-add-to-basket")
    assert button_basket, f"{button_basket} not found!!!"