# Booking - PyTest

## MAC Installation instructions

For MAC you can use Homebrew for the dependencies installation.

1. Install Brew: <https://brew.sh/>

    ~~~sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ~~~

2. Once installed, you can install Python by executing:

    ~~~sh
    brew install python@3.8 # python >= @3.8 and <= @3.11
    ~~~

3. Inside the folder execute:

    ~~~sh
    python3.8 -m venv env
    ~~~

    AND

    ~~~sh
    source env/bin/activate
    ~~~

4. Then, install the required packages using:

    ~~~sh
    pip install -r requirements.txt
    ~~~

5. Additionally, a WebDriver is needed to execute the tests:

    1. Download one of the following WebDrivers

        - For Chrome: [chromederiver](https://chromedriver.chromium.org/downloads)
        - For Firefox: [geckodriver](https://github.com/mozilla/geckodriver/releases)

    2. Unzip the WebDriver

    3. Add the WebDriver to the PATH

        ~~~sh
        # .bash_profile
        export PATH="path/to/webdriver:$PATH"
        ~~~

## Windows Installation instructions

1. Change directory into the booking-pytest folder

2. Inside the folder create virtual environment by executing once:

    ~~~sh
    virtualenv env
    ~~~

3. To activate the virtual environment run:

    ~~~sh
    ./env/Scripts/activate.ps1
    ~~~

4. Then, install the required packages using:

    ~~~sh
    pip install -r requirements.txt
    ~~~

### Update required packages

To update the required packages, make sure the virtual environment is activated, then update the packages using:

~~~sh
pip install -r requirements.txt --upgrade
~~~

### Update WebDriver

To update the WebDriver, do the step 5 of the Installation instructions. Once unzipped, replace the new WebDriver in the folder previously added to the PATH.

## Run Tests

To run the Test Cases, first make sure the virtual environment is activated and you are in the `booking` folder, use the following command:

~~~sh
pytest tests/path/to/file.py
~~~

### Options

The command line parameters are defined in the `booking/fixtures/booking_session.py` file.

**Accepted parameters:**

1. `--browser=chrome`: Accepted options (chrome, firefox).

    ~~~sh
    pytest --browser=chrome # Requires chromedriver and Google Chrome installed
    ~~~

    OR

    ~~~sh
    pytest --browser=firefox # Requires geckodriver and Firefox installed
    ~~~

2. `--gui`: Enable the Graphical User Interface mode for the browser.

    ~~~sh
    pytest --browser=chrome --gui # Opens Chrome browser with GUI
    ~~~

## Recommended VS Code extensions

- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker): Spelling checker for source code.
- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens): Supercharge Git within VS Code.
- [PyPI Assistant](https://marketplace.visualstudio.com/items?itemName=twixes.pypi-assistant): pip requirements files enhanced with up-to-date package information.
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python): IntelliSense (Pylance), Linting, Debugging, code formatting and more!
- [Trailing Spaces](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces): Highlight trailing spaces and delete them in a flash!
