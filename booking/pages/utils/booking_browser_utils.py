from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


class BrowserUtils:
    """
    This class contains common methods that can be used in the browser for some
    testing scenarios. This class should be inherited in the Page Objects.
    """

    def __init__(self, browser: WebDriver) -> None:
        """
        Initializes the Browser and WebDriverWait class
        """
        self.__browser = browser
        self.__wait = WebDriverWait(browser, 3)

    def scroll_up(self) -> None:
        """
        Scrolls up to the top of the app, mainly used to locate elements placed
        at the top of the page, or elements that are being dynamically loaded.
        """
        self.__browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)

    def scroll_down(self) -> None:
        """
        Scrolls down to the bottom of the app, mainly used to locate elements placed
        at the bottom of the page, or elements that are being dynamically loaded.
        """
        self.__browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

    def load_hidden_elements(self) -> None:
        """
        This helps to dynamically load displayed/generated elements that are required
        for some test cases. It scrolls down to the bottom of the app, waits 1 second
        for the elements to be displayed, and then scrolls up to the top of the app
        and waits another extra second, in case some elements haven't rendered
        """
        self.scroll_up()
        self.scroll_down()

    def get_current_url(self) -> str:
        """
        This methods helps to get the current URL of the Browser
        """
        return self.__browser.current_url

    def refresh_browser(self, explicit_wait=2) -> None:
        """
        This method helps to reload the current URL in the browser
        """
        self.__browser.refresh()
        time.sleep(explicit_wait)

    def accept_alert(self) -> None:
        """
        This method helps to accept an alert, or raise an Exception
        when the alert is not present
        """
        try:
            self.__wait.until(EC.alert_is_present())
            self.__browser.switch_to.alert.accept()
        except:
            raise Exception('Alert is not present')

    def dismiss_alert(self) -> None:
        """
        This method helps to dismiss an alert, or raise an Exception
        when the alert is not present
        """
        try:
            self.__wait.until(EC.alert_is_present())
            self.__browser.switch_to.alert.dismiss()
        except:
            raise Exception('Alert is not present')

    def get_alert_text(self) -> str:
        """
        This method helps to get the alert text, or raise an Exception
        when the alert is not present
        """
        try:
            self.__wait.until(EC.alert_is_present())
            return self.__browser.switch_to.alert.text
        except:
            raise Exception('Alert is not present')

    def switch_tab(self, tab: int, explicit_wait=2) -> None:
        """
        This method helps to switch to a specific tab defined by the parameter,
        or raise an Exception when the tab is not present
        """
        try:
            self.__browser.switch_to.window(self.__browser.window_handles[tab])
            time.sleep(explicit_wait)
        except:
            raise Exception(f'Tab "{tab}" is not present')
