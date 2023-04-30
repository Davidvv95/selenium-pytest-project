from pages.results import BookingResultsPage
from pages.search import BookingSearchPage

from pytest import mark, fixture


@fixture(scope='module', autouse=True)
def setup_results_page(browser, app_config):
    """
    This setup method loads the search page and fills the necessary data
    to perform a successful search
    """
    search_page = BookingSearchPage(browser, app_config)
    search_page.load()
    if search_page.find_dismiss_sign_in_info_button() is not None:
        search_page.click_dismiss_sign_in_info_button()
    search_page.select_destination('Granada, Spain')
    if search_page.find_specific_date('1') is not None:
        search_page.select_check_in_out_dates('1', '7')
    else:
        search_page.click_check_in_date_button()
        search_page.select_check_in_out_dates('1', '7')
    search_page.click_occupancy_button()
    while search_page.get_adult_count() != '4':
        search_page.click_adults_plus_button()
    search_page.click_search_button()

@mark.smoke
def bkg_4_results_filters(browser, app_config):
    """
    This method tests if the Sort By filter dropdown contains all
    the expected dropdown options
    """
    results_page = BookingResultsPage(browser, app_config)
    assert results_page.find_sort_by_dropdown_button() is not None
    results_page.click_sort_by_dropdown_button()
    data_id = [
            'popularity', 'upsort_bh', 'price', 'review_score_and_price',
            'class', 'class_asc', 'class_and_price', 'distance_from_search'
            ]
    for i in data_id:
        assert results_page.find_sort_by_dropdown_option(i) is not None

@mark.smoke
def bkg_5_results_property_ratings(browser, app_config):
    """
    This method selects the property ratings checkboxes if they aren't selected,
    and verifies if they were checked successfully.
    """
    results_page = BookingResultsPage(browser, app_config)
    stars = ['three', 'four', 'five']
    for i in stars:
        results_page.check_property_ratings_checkbox(i)
    for i in stars:
        assert results_page.find_property_ratings_checkbox(i).is_selected() == True
