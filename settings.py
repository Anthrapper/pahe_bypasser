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
chrome_options.add_argument("--remote-debugging-port=9222")


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
	driver =webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',chrome_options=chrome_options)