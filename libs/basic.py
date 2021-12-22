from testdata.testdata import url


def start(get_driver):
    get_driver.get(url)
    get_driver.maximize_window()
    get_driver.implicitly_wait(5)


def click(get_driver, element):
    get_driver.find_element(*element).click()


def send_keys(get_driver, element, text):
    get_driver.find_element(*element).send_keys(text)
