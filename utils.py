import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import locators


URL = "https://wetransfer.com/"
match_remaining_time = re.compile(r"(\d+) (second|seconds|minute|minutes|hours)")


def setup_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


def find_element(driver, locator):
    return driver.find_element(*locator)


def navigate_webdriver(driver, url):
    driver.get(url)


def skip_welcome_message(driver):
    try:
        find_element(driver, locators.WELCOME_MESSAGE).click()
    except NoSuchElementException:
        pass


def skip_promotion(driver):  # protected
    try:
        find_element(driver, locators.PROMOTION).click()
    except NoSuchElementException:
        pass


def set_file(driver, file):  # protected
    file_receiver = find_element(driver, locators.FILE_INPUT)
    file_receiver.send_keys(file)


def skip_almost_there_ad(driver):
    try:
        find_element(driver, locators.ALMOST_THERE_AD).click()
    except NoSuchElementException:
        pass


def clear_input(input):
    input.send_keys(Keys.CONTROL + "a")
    input.send_keys(Keys.DELETE)


def set_title(driver, title):  # protected
    title_input = find_element(driver, locators.TITLE)
    clear_input(title_input)
    title_input.send_keys(title)


def set_message(driver, message):  # protected
    message_input = find_element(driver, locators.MESSAGE)
    message_input.send_keys(message)


def get_remaining_time(driver):
    time_element = find_element(driver, locators.TIME_ELEMENT)
    result = match_remaining_time.search(time_element.text)
    unit = result.group(2)
    remaining = int(result.group(1))

    if unit == "hours":
        time = remaining * 60 * 60
    if unit in ("minutes", "minute"):
        time = remaining * 60

    return time_element, time


def is_done(driver):
    try:
        find_element(driver, locators.FILE_INPUT)
        return False
    except NoSuchElementException:
        pass

    try:
        get_progress_bar(driver)
        return False
    except NoSuchElementException:
        pass

    return True


def start_transfer(driver):
    find_element(driver, locators.OPTIONS_BUTTON).click()
    find_element(driver, locators.TRANSFER_BUTTON).click()
    find_element(driver, locators.GET_LINK_BUTTON).click()


def get_link(driver):  # protected
    link_input = find_element(driver, locators.LINK_INPUT)

    return link_input.get_attribute("value")


def get_progress_bar(driver):
    return find_element(driver, locators.PROGRESS_BAR)


def upload(file, driver=None, title=None, message=None):
    if driver is None:
        driver = setup_webdriver()

    navigate_webdriver(driver, URL)
    skip_welcome_message(driver)
    skip_almost_there_ad(driver)
    skip_promotion(driver)
    set_file(driver, file)

    if title:
        set_title(driver, title)

    if message:
        set_message(driver, message)

    start_transfer(driver)

    while not is_done(driver):
        time.sleep(0.5)

    return get_link(driver)


def download(url, driver=None):
    if driver is None:
        driver = setup_webdriver()

    navigate_webdriver(driver, url)
    try:
        skip_welcome_message(driver)
        skip_almost_there_ad(driver)
        skip_promotion(driver)

    except NoSuchElementException:
        pass
    print('before')
    find_element(driver, locators.DOWNLOAD_BUTTON).click()
    print('after')

if __name__ == "__main__":
    FILE = "D:\\python_grinding\\todos\\database.json"
    driver = setup_webdriver()
    url = upload(FILE, driver=driver)
    download(url, driver=driver)

