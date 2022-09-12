from selenium.webdriver.chrome.options import Options
import logging.config
from selenium import webdriver


chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--headless")


logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s [%(levelname)s] %(message)s",
	handlers=[
		logging.FileHandler("logs.log"),
		logging.StreamHandler()
	]
)

class Tools(object):
	logger = logging.getLogger(__name__)
	driver =webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chrome_options)