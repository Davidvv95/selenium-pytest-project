from pages.search import BookingSearchPage
from pages.results import BookingResultsPage

from pytest import mark, fixture


@fixture(scope='module', autouse=True)
def setup_search_page(browser, app_config):
    """
    This setup method loads the search page, and removes the Sign-in
    or Register if it appears
    """
    search_page = BookingSearchPage(browser, app_config)
    search_page.load()
    if search_page.find_dismiss_sign_in_info_button() is not None:
        search_page.click_dismiss_sign_in_info_button()

@mark.smoke
def bkg_1_search_menu_buttons(browser, app_config):
    """
    This method tests if all the expected menu options are displayed in
    the search page
    """
    search_page = BookingSearchPage(browser, app_config)
    assert search_page.find_stays_menu_button() is not None
    assert search_page.find_flights_menu_button() is not None
    assert search_page.find_cars_menu_button() is not None
    assert search_page.find_attractions_menu_button() is not None
    assert search_page.find_taxis_menu_button() is not None

@mark.smoke
def bkg_2_fill_search_fields(browser, app_config):
    """
    This method tests if the destination, dates and occupancy fields
    can be filled out correctly. It also verifies that the occupancy
    counter works as expected
    """
    search_page = BookingSearchPage(browser, app_config)
    search_page.select_destination('Granada, Spain')
    if search_page.find_specific_date('1') is not None:
        search_page.select_check_in_out_dates('1', '7')
    else:
        search_page.click_check_in_date_button()
        search_page.select_check_in_out_dates('1', '7')
    search_page.click_occupancy_button()
    while search_page.get_adult_count() != '4':
        search_page.click_adults_plus_button()
    assert search_page.get_adult_count() == '4'

@mark.smoke
def bkg_3_search_destination(browser, app_config):
    """
    This method tests if the search button works as expected, and verifies
    we are taken to the results page successfully
    """
    search_page = BookingSearchPage(browser, app_config)
    search_page.click_search_button()
    results_page = BookingResultsPage(browser, app_config)
    assert results_page.find_search_results_breadcrumb() is not None
