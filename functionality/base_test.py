import pathlib
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from random_user_agent.params import SoftwareName, OperatingSystem
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # software_names = [SoftwareName.CHROME.value]
        # operating_systems = [OperatingSystem.WINDOWS.value,
        #                      OperatingSystem.LINUX.value]
        # user_agent_rotator = UserAgent(software_names=software_names,
        #                                operating_systems=operating_systems,
        #                                limit=5)
        # user_agent = user_agent_rotator.get_random_user_agent()
        # options.add_argument("--start-fullscreen")
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-notifications")
        # options.add_argument(f"user-agent={user_agent}")
        # self.driver = webdriver.Chrome(executable_path=pathlib.Path(__file__).parent / "../browser/chromedriver", options=options)

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.maximize_window()
        self.driver.get("http://13.232.13.200/login.php")
        # self.driver.set_page_load_timeout(3000)

    def tearDown(self):
        self.driver.close()

