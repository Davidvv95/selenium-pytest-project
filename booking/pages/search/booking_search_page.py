from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pages.utils import BookingUtils, BrowserUtils

from time import sleep


class BookingSearchPage(BrowserUtils):
    """
    Contains all the objects and interaction methods related to
    the Booking search page
    """

    __SEARCH_PAGE_URL = ''

    # Pop-up
    __DISMISS_SIGN_IN_INFO_X_BUTTON = (By.XPATH, '//button[@aria-label="Dismiss sign-in info."]')

    # Search Menu
    __STAYS_MENU_BUTTON = (By.ID, 'accommodations')
    __FLIGHTS_MENU_BUTTON = (By.ID, 'flights')
    __CARS_MENU_BUTTON = (By.ID, 'cars')
    __ATTRACTIONS_MENU_BUTTON = (By.ID, 'attractions')
    __TAXIS_MENU_BUTTON = (By.ID, 'airport_taxis')

    # Search textbox fields
    __DESTINATION_TEXTBOX = (By.ID, ':Ra9:')
    __CHECK_IN_DATE_BUTTON = (By.XPATH, '//button[@data-testid="date-display-field-start"]')
    __CHECK_OUT_DATE_BUTTON = (By.XPATH, '//button[@data-testid="date-display-field-end"]')
    __OCCUPANCY_BUTTON = (By.XPATH, '//button[@data-testid="occupancy-config"]')
    __ADULT_PLUS_BUTTON = (By.XPATH, '(//label[text()="Adults"]//ancestor::div[2]//child::button)[2]')
    __ADULT_COUNTER = (By.XPATH, '(//label[text()="Adults"]//ancestor::div[2]//child::span)[3]')
    __SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')

    def __init__(self, browser, app_config):
        """Initializes the browser fixture through BookingUtils."""
        super().__init__(browser)
        self.booking_utils = BookingUtils(browser, app_config)

    # Interaction methods
    def load(self):
        """Loads the specified URL."""
        self.booking_utils.load_page(self.__SEARCH_PAGE_URL, 3)

    def find_stays_menu_button(self):
        """Finds the Stays button in the search page"""
        return self.booking_utils.find_element(self.__STAYS_MENU_BUTTON)

    def find_flights_menu_button(self):
        """Finds the Flights button in the search page"""
        return self.booking_utils.find_element(self.__FLIGHTS_MENU_BUTTON)

    def find_cars_menu_button(self):
        """Finds the Cars button in the search page"""
        return self.booking_utils.find_element(self.__CARS_MENU_BUTTON)

    def find_attractions_menu_button(self):
        """Finds the Attractions button in the search page"""
        return self.booking_utils.find_element(self.__ATTRACTIONS_MENU_BUTTON)

    def find_taxis_menu_button(self):
        """Finds the Airport Taxis button in the search page"""
        return self.booking_utils.find_element(self.__TAXIS_MENU_BUTTON)

    def clear_destination_textbox(self):
        """Clears the Where are you going? textbox"""
        self.booking_utils.clear_element(self.__DESTINATION_TEXTBOX)

    def fill_destination_textbox(self, destination):
        """Fills the Where are you going? textbox"""
        self.clear_destination_textbox()
        self.booking_utils.fill_element(self.__DESTINATION_TEXTBOX, destination)
        sleep(1)

    def select_destination(self, destination):
        """Selects a destination in the Where are you going? textbox"""
        self.fill_destination_textbox(destination)
        self.booking_utils.fill_element(self.__DESTINATION_TEXTBOX, (Keys.DOWN, Keys.ENTER))
        sleep(1)

    def find_dismiss_sign_in_info_button(self):
        """Finds the Dismiss sign-in info button in the Sign-in or Register modal"""
        return self.booking_utils.find_element(self.__DISMISS_SIGN_IN_INFO_X_BUTTON)

    def click_dismiss_sign_in_info_button(self):
        """Clicks the Dismiss sign-in info button in the Sign-in or Register modal"""
        self.booking_utils.click_element(self.__DISMISS_SIGN_IN_INFO_X_BUTTON)

    def click_check_in_date_button(self):
        """Clicks the Check-in date button"""
        self.booking_utils.click_element(self.__CHECK_IN_DATE_BUTTON)

    def find_specific_date(self, date):
        """Finds a specific date among the check-in dates"""
        selector = (By.XPATH, f'(//span[text()="{date}"])[2]')
        return self.booking_utils.find_element(selector)

    def click_specific_date(self, date):
        """Clicks a specific date among the check-in dates"""
        selector = (By.XPATH, f'(//span[text()="{date}"])[2]')
        self.booking_utils.click_element(selector)

    def select_check_in_out_dates(self, check_in_date, check_out_date):
        """Selects a check-in and out date"""
        self.click_specific_date(check_in_date)
        self.click_specific_date(check_out_date)

    def click_occupancy_button(self):
        """Clicks the Occupancy button"""
        self.booking_utils.click_element(self.__OCCUPANCY_BUTTON)

    def click_adults_plus_button(self):
        """Clicks the Adults + button in the Occupancy section"""
        self.booking_utils.click_element(self.__ADULT_PLUS_BUTTON)

    def get_adult_count(self):
        """Gets the adult count in the Occupancy section"""
        return self.booking_utils.get_element_attribute(self.__ADULT_COUNTER, 'textContent')

    def click_search_button(self):
        """Clicks on the Search button"""
        self.booking_utils.click_element(self.__SEARCH_BUTTON, 1)
