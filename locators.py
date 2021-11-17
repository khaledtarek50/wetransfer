from selenium.webdriver.common.by import By


WELCOME_MESSAGE = By.CSS_SELECTOR, ".welcome__buttons button:first-of-type"
PROMOTION = By.CLASS_NAME, "transfer__button"
FILE_INPUT = By.CSS_SELECTOR, ".uploader__files input"
ALMOST_THERE_AD = By.CSS_SELECTOR, ".transfer__footer button"
TITLE = By.CSS_SELECTOR, ".uploader__display-name input"
MESSAGE = By.CSS_SELECTOR, ".uploader__message textarea"
TIME_ELEMENT = By.XPATH, "//p[contains(text(),'remaining')]"
OPTIONS_BUTTON = By.CSS_SELECTOR, ".transfer__footer button"
TRANSFER_BUTTON = By.XPATH, "//*[ text() = 'Get transfer link']/preceding-sibling::div"
GET_LINK_BUTTON = By.CSS_SELECTOR, ".transfer__footer .transfer__button"
LINK_INPUT =  By.CSS_SELECTOR, ".transfer-link__url-button-wrapper input"
PROGRESS_BAR = By.CSS_SELECTOR, ".transfer__contents .spinner__label"
DOWNLOAD_BUTTON = By.CSS_SELECTOR, ".transfer__footer .transfer__button"