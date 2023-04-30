from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from typing import List, Tuple
import platform
import time

from config import Config


class BookingUtils:
    """
    Contains different methods that are useful for some automation testing scenarios.
    They can be imported and used in any of the existing Page Objects and tests.
    """

    __CTRL_KEY = Keys.COMMAND if platform.system() == 'Darwin' else Keys.CONTROL

    def __init__(self, browser: WebDriver, app_config: Config) -> None:
        """
        Initializes the Actions class, Base URL, Browser and WebDriverWait class
        """
        self.__actions = ActionChains(browser)
        self.__base_url = app_config.base_url
        self.__browser = browser
        self.__wait = WebDriverWait(browser, 3)

    def load_page(self, url: str, explicit_wait=3) -> None:
        """
        This method helps to load a page and also provides an explicit wait
        """
        self.__browser.get(f'{self.__base_url}{url}')
        time.sleep(explicit_wait)

    def __get_element(self, selector: Tuple[str, str]) -> WebElement:
        """
        This method helps to get an element in the page, or raise an Exception if the
        element is not found. It is defined as Private because it must be used only inside
        the Utils class
        """
        try:
            return self.__wait.until(EC.presence_of_element_located(selector))
        except:
            raise Exception(f'Element with selector "{selector[1]}" was not found')

    def find_element(self, selector: Tuple[str, str]) -> WebElement:
        """
        This method helps to find an element in the Page Object. It
        handles the exception as None if the element is not found
        """
        try:
            return self.__get_element(selector)
        except:
            return None

    def fill_element(self, selector: Tuple[str, str], value: str) -> None:
        """
        This method helps to fill an element in the Page Object, or raises an
        Exception if the element is not found
        """
        element = self.__get_element(selector)
        element.send_keys(value)

    def clear_element(self, selector: Tuple[str, str]) -> None:
        """
        This method helps to clear an element in the Page Object, or raises an
        Exception if the element is not found
        """
        self.fill_element(selector, (f'{self.__CTRL_KEY}a', Keys.BACKSPACE))

    def click_element(self, selector: Tuple[str, str], explicit_wait=0) -> None:
        """
        This method helps to click an element in the Page Object, or raises an
        Exception if the element is not found and also provides an explicit wait
        """
        element = self.__get_element(selector)
        try:
            element.click()
        except:
            self.__browser.execute_script('arguments[0].click();', element)
        time.sleep(explicit_wait)

    def click_elements(self, selector: Tuple[str, str], explicit_wait=0) -> None:
        """
        This method helps to click elements in the Page Object and also provides
        an explicit wait
        """
        for element in self.find_elements(selector):
            try:
                element.click()
            except:
                self.__browser.execute_script('arguments[0].click();', element)
        time.sleep(explicit_wait)

    def find_elements(self, selector: Tuple[str, str]) -> List[WebElement]:
        """
        This method helps to find a list of elements which match with a specific
        selector. It returns an empty list if no elements matches
        """
        return self.__browser.find_elements(*selector)

    def is_selected(self, selector: Tuple[str, str]) -> bool:
        """
        This method helps to verify if a checkbox is selected, or raises an Exception
        if the element is not found and raise an Exception if the element is not
        a checkbox
        """
        element = self.__get_element(selector)
        try:
            return element.is_selected()
        except:
            raise Exception(f'Element with selector "{selector[1]}" is not a checkbox or radio button')

    def check_element(self, selector: Tuple[str, str]) -> None:
        """
        This method helps to check an element if it's not selected, or raises an Exception
        if the element is not found or does not have the selected property
        """
        if not self.is_selected(selector):
            self.click_element(selector)

    def uncheck_element(self, selector: Tuple[str, str]) -> None:
        """
        This method helps to uncheck an element if it's selected,or raises an Exception
        if the element is not found or does not have the selected property
        """
        if self.is_selected(selector):
            self.click_element(selector)

    def select_element(self, selector: Tuple[str, str], option: str, explicit_wait=0) -> None:
        """
        This method helps to select an option in a dropdown element, or raise an Exception
        if the element or the option does not exist
        """
        self.fill_element(selector, option)
        self.click_element((By.XPATH, f'//li[text()="{option}"]'), explicit_wait)

    def is_enabled(self, selector: Tuple[str, str]) -> bool:
        """
        This method helps to verify if an element is enabled, or raises and Exception
        if the element is not found and raise and Exception if the element is not
        valid (Elements that don't support this functionality)
        """
        element = self.__get_element(selector)
        try:
            return element.is_enabled()
        except:
            raise Exception(f'Element with selector "{selector[1]}" does not support this functionality')

    def get_element_attribute(self, selector: Tuple[str, str], attribute: str) -> str:
        """
        This method helps to get an attribute of a specific element in the Page Object,
        or raises an Exception if the element is not found and raise an Exception
        if the element doesn't have the specified attribute
        """
        element = self.__get_element(selector)
        try:
            return element.get_attribute(attribute)
        except:
            raise Exception(f'Element with selector "{selector[1]}" has no attribute "{attribute}"')

    def hover_element(self, selector: Tuple[str, str]) -> None:
        """
        This method helps to hover an element, or raises an Exception if the element
        is not found and also provides an explicit wait
        """
        element = self.__get_element(selector)
        self.__actions.move_to_element(element).perform()

    def switch_to_iframe(self, selector: Tuple[str, str], explicit_wait=2) -> None:
        """
        This method helps to switch to an iframe, or raise an Exception if the
        element is not found
        """
        iframe = self.__get_element(selector)
        self.__browser.switch_to.frame(iframe)
        time.sleep(explicit_wait)

    def switch_from_iframe_to_default(self, explicit_wait=2) -> None:
        """
        This method helps to switch from an iframe back to default page
        """
        self.__browser.switch_to.default_content()
        time.sleep(explicit_wait)
