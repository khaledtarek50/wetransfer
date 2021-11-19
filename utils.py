import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://wetransfer.com/"
match_remaining_time = re.compile(r"(\d+) (second|seconds|minute|minutes|hours)")


def setup_webdriver(headless=True):
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.headless = headless
    driver = webdriver.Chrome(
        "D:\\python_grinding\\todos\\wetransfer_bot\\chromedriver", options=options
    )
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
    try:
        file_receiver = find_element(driver, locators.FILE_INPUT)
        file_receiver.send_keys(file)
    except NoSuchElementException:
        pass


def skip_almost_there_ad(driver):
    try:
        find_element(driver, locators.ALMOST_THERE_AD).click()
    except NoSuchElementException:
        pass


def get_file_name(driver):
    file_name = find_element(driver, locators.FILE_NAME)
    return file_name.text


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


def get_progress(driver):
    return int(get_progress_bar(driver).text.replace('%', ''))


def upload(file, driver, on_progress_update=None, title=None, message=None):
    if on_progress_update is not None and not isinstance(on_progress_update, callable):
        raise ValueError('on_progress_update is not callable')
    
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
        if on_progress_update is not None:
            progress = get_progress(driver)
            on_progress_update(progress)

    return get_link(driver)


def download(url, driver):
    navigate_webdriver(driver, url)
    skip_welcome_message(driver)
    skip_almost_there_ad(driver)
    skip_promotion(driver)
    download_button = find_element(driver, locators.DOWNLOAD_BUTTON)
    # file_name = get_file_name(driver)
    # time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(download_button)).click()
    # return file_name


class WeTransferBot:
    def __init__(self, driver) -> None:
        self.driver = driver

    def on_progress(self, progress):
        print(progress)

    def upload(self, file):
        return upload(file, driver=self.driver, on_progress_update=self.on_progress)

    def download(self, url):
        return download(url, driver=self.driver)


if __name__ == "__main__":
    # FILE = "D:\\python_grinding\\todos\wetransfer_bot\\database.json"
    FILE = "D:\\movies\\[EgyBest].Arcane.S01E01.WEB-DL.720p.x264.mp4"
    driver = setup_webdriver(headless=False)

    # def update_progress(progress):
    #     print(progress)

    
    # url = upload(FILE, on_progress_update=update_progress ,driver=driver)
    # z = download(url, driver=driver)
    # print(z)
