from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pages.utils import BookingUtils, BrowserUtils


class BookingResultsPage(BrowserUtils):
    """
    Contains all the objects and interaction methods related to
    the Booking results page
    """

    # Labels
    __SEARCH_RESULTS_BREADCRUMB = (By.XPATH, '//span[text()="Search results"]')

    # Filters
    __SORT_BY_BUTTON = (By.XPATH, '//button[@data-testid="sorters-dropdown-trigger"]')

    # Search section
    __DESTINATION_TEXTBOX = (By.ID, ':Rp5:')
    __CHECK_IN_DATE_BUTTON = (By.XPATH, '//button[@data-testid="date-display-field-start"]')
    __CHECK_OUT_DATE_BUTTON = (By.XPATH, '//button[@data-testid="date-display-field-end"]')
    __OCCUPANCY_BUTTON = (By.XPATH, '//button[@data-testid="occupancy-config"]')
    __ADULT_PLUS_BUTTON = (By.XPATH, '(//label[text()="Adults"]//ancestor::div[2]//child::button)[2]')
    __ADULT_COUNTER = (By.XPATH, '(//label[text()="Adults"]//ancestor::div[2]//child::span)[3]')
    __SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    __OCCUPANCY_DONE_BUTTON = (By.XPATH, '//span[text()="Done"]/parent::button')
    __SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')

    # Property ratings
    __ONE_STAR_CHECKBOX = (By.ID, ':Rhf9cq:')
    __TWO_STARS_CHECKBOX = (By.ID, ':Rif9cq:')
    __THREE_STARS_CHECKBOX = (By.ID, ':Rjf9cq:')
    __FOUR_STARS_CHECKBOX = (By.ID, ':Rkf9cq:')
    __FIVE_STARS_CHECKBOX = (By.ID, ':Rlf9cq:')

    def __init__(self, browser, app_config):
        """Initializes the browser fixture through BookingUtils."""
        super().__init__(browser)
        self.booking_utils = BookingUtils(browser, app_config)

    def find_search_results_breadcrumb(self):
        """Finds the Search results breadcrumb"""
        return self.booking_utils.find_element(self.__SEARCH_RESULTS_BREADCRUMB)

    def find_sort_by_dropdown_button(self):
        """Finds the Sort By dropdown button"""
        return self.booking_utils.find_element(self.__SORT_BY_BUTTON)

    def click_sort_by_dropdown_button(self):
        """Clicks the Sort By dropdown button"""
        self.booking_utils.click_element(self.__SORT_BY_BUTTON, 1)

    def find_sort_by_dropdown_option(self, data_id):
        """Finds the Sort By dropdown options dynamically"""
        selector = (By.XPATH, f'//button[@data-id="{data_id}"]')
        return self.booking_utils.find_element(selector)

    def find_property_ratings_checkbox(self, stars):
        """Finds the Property Ratings checkboxes dynamically"""
        stars_id = {
            'one': ':Rhf9cq:', 'two': ':Rif9cq:', 'three': ':Rjf9cq:',
            'four': ':Rkf9cq:', 'five': ':Rlf9cq:'
            }
        selector = (By.ID, stars_id[stars])
        return self.booking_utils.find_element(selector)

    def check_property_ratings_checkbox(self, stars):
        """Checks the Property Ratings checkboxes dynamically"""
        stars_id = {
            'one': ':Rhf9cq:', 'two': ':Rif9cq:', 'three': ':Rjf9cq:',
            'four': ':Rkf9cq:', 'five': ':Rlf9cq:'
            }
        selector = (By.ID, stars_id[stars])
        self.booking_utils.check_element(selector)
