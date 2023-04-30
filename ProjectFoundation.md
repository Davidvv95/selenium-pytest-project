# Project Foundation

## Markers

### Content of [pytest.ini](./booking/pytest.ini)

~~~ini
[pytest]
addopts = -m "not designreview" # Deselected by default

...

markers =
    smoke: Fundamental functionality Test Cases
    sanity: Complementary functionality Test Cases
    regression: All Regression Test Cases
    designreview: Deselected Test Cases due to a bad design
~~~

### Our Markers

**Note:** These markers are registered, you can see them using `pytest --markers`:

- `@pytest.mark.smoke`
- `@pytest.mark.sanity`
- `@pytest.mark.regression`
- `@pytest.mark.designreview`

## Run Tests

Inside `booking` folder, given the following Testing file:

~~~py
import pytest


@pytest.mark.smoke
def bkg_0_test_case():
    pass


@pytest.mark.sanity
def bkg_1_test_case():
    pass


@pytest.mark.regression
@pytest.mark.smoke
def bkg_2_test_case():
    pass


@pytest.mark.regression
@pytest.mark.sanity
def bkg_3_test_case():
    pass


@pytest.mark.designreview
@pytest.mark.smoke
def bkg_4_test_case():
    pass
~~~

### Select specific Test Case

You can run a specific Test Case using:

~~~sh
pytest tests/path/to/file.py::bkg_0_test_case
~~~

OR

Select multiple Test Cases using:

~~~sh
pytest \
    tests/path/to/file.py::bkg_1_test_case \
    tests/path/to/file.py::bkg_2_test_case \
    tests/path/to/file.py::bkg_3_test_case
~~~

### Select Test Cases by markers

You can run Test Cases by selecting a specific marker, given the following scenarios:

1. Run `smoke` Test Cases:

    ~~~sh
    pytest -m smoke # bkg_0 and bkg_2
    ~~~

2. Run `sanity` Test Cases

    ~~~sh
    pytest -m sanity # bkg_1 and bkg_3
    ~~~

3. Run `regression` Test Cases:

    ~~~sh
    pytest -m regression # bkg_2 and bkg_3
    ~~~

4. Run `sanity` and `regression` Test Cases:

    ~~~sh
    pytest -m "sanity and regression" # bkg_3
    ~~~

5. Run `smoke` but not `regression` Test Cases:

    ~~~sh
    pytest -m "not smoke and regression" # bkg_3
    ~~~

6. Run `smoke` or `sanity` but not `regression` Test Cases:

    ~~~sh
    pytest -m "not regression and smoke or sanity" # bkg_0 and bkg_1
    ~~~

**Note:** The Test Case `bkg_4_test_case` will be deselected in any of the scenarios above.

## Third Party libraries

### Content of [requirements.txt](./requirements.txt)

- [Faker](https://pypi.org/project/Faker/): Fake data generator
- [pytest](https://pypi.org/project/pytest/): Testing framework
- [pytest-html](https://pypi.org/project/pytest-html/): HTML report generator
- [pytest-rerunfailures](https://pypi.org/project/pytest-rerunfailures/): Re-run failed Test Cases
- [requests](https://pypi.org/project/requests/): HTTP package to interact with APIs
- [selenium](https://pypi.org/project/selenium/): Automate web browsers
