import platform

from selenium.webdriver.chrome.options import Options
from seleniumwrapper import create, connect


chrome_options = Options()
chrome_options.add_experimental_option("prefs", {'download.prompt_for_download': False})


def driver_win():
    """ Подготавливает драйвер для Windows
    """
    driver = create('chrome', options=chrome_options).unwrap
    driver.maximize_window()
    return driver


def driver_linux():
    """ Подготавливает драйвер для Linux
    """
    caps = chrome_options.to_capabilities()
    driver = create('chrome', custom_capabilities=caps).unwrap
    driver.set_window_size(1920, 1080)
    return driver


def prepare_driver():
    """ Подготавливает браузер
    """
    os_system = platform.system()
    if os_system == 'Windows':
        driver = driver_win()
    else:
        driver = driver_linux()
    driver.timeout = 20
    return driver
