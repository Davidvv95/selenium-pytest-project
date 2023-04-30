from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions
from pytest import fixture
from config import Config

# Selenium Implicit Wait Time
DEFAULT_WAIT_TIME = 5

# Browser windows size
WIDTH = 1024
HEIGHT = 768


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='chrome',
        help='Browser to run tests: chrome (default) | firefox',
        choices=('chrome', 'firefox')
    )
    parser.addoption(
        '--gui',
        action='store_true',
        default=False,
        help='Browser option to enable the GUI during the tests: False (default)'
    )


@fixture(scope='session')
def config_browser(request):
    return request.config.getoption('--browser')


@fixture(scope='session')
def gui(request):
    return request.config.getoption('--gui')


@fixture(scope='session')
def app_config():
    return Config()


@fixture(scope='module')
def browser(gui, config_browser):
    '''Initializes the webdriver'''
    if config_browser == 'chrome':
        options = ChromeOptions()
        if not gui:
            options.add_argument('headless')
        options.add_argument('-incognito')
        options.add_argument('--disable-logging')
        options.add_argument(f'--window-size={WIDTH},{HEIGHT}')
        driver = Chrome(options=options)
    else:
        options = FirefoxOptions()
        if not gui:
            options.add_argument('-headless')
        options.add_argument('-private')
        options.add_argument(f'--width={WIDTH}')
        options.add_argument(f'--height={HEIGHT}')
        driver = Firefox(options=options)
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(DEFAULT_WAIT_TIME)
    # Return the driver object at the end of setup
    yield driver
    # For cleanup, quit the driver
    driver.quit()
