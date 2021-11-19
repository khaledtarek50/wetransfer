from utils import download, get_file_name, upload, setup_webdriver
import os
from pathlib import Path
import filecmp

FILE = "D:\\python_grinding\\todos\wetransfer_bot\\database.json"
FILE_NAME = os.path.basename(FILE)
URL = "https://wetransfer.com/"
HOME = Path.home()
DOWNLOADS_DIR = HOME / 'Downloads'

def test(driver, file):
    # upload a file then download the file then test if the downloaded file is the uploaded file
    url = upload(FILE, driver=driver)
    download(url, driver=driver)
    files_equal = filecmp.cmp(FILE, DOWNLOADS_DIR / FILE_NAME, shallow=False)

    if not files_equal:
        raise Exception()
