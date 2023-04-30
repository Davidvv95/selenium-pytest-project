from selenium.webdriver.common.keys import Keys
import platform


class Config:
    """
    This class contains the Configuration of the URL used during the tests,
    in addition returns the Ctrl key according to the OS
    """

    def __init__(self) -> None:
        """
        Initializes the base URL
        """
        self.base_url = f'https://www.booking.com'
        self.ctrl_os = Keys.COMMAND if platform.system() == 'Darwin' else Keys.CONTROL
