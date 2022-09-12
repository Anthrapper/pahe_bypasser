from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from identifiers import *
from settings import Tools

logger=Tools.logger

def get_link(e):
	driver=Tools.driver
	driver.get('https://pahe.li/the-girl-on-a-bulldozer-2022-web-hd-480p-720p/')
	texts= [y for x in [driver.find_elements('xpath',type) for type in LINK_TYPE] for y in x]
	texts[e].click()
	# if driver.current_url !='https://intercelestial.com/':
	# 	driver.close()
	# 	switch_to(find_all(Window())[0])
	# 	logger.debug("window changed")
	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, AGREE_BUTTON))).click()		
	except TimeoutException:
		logger.warning('No browser verification')

	driver.execute_script("document.getElementById('landing').submit();")
	WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, GENERATE))).click()
	WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, SHOW_LINK))).click()

	window_after = driver.window_handles[1]
	driver.switch_to.window(window_after)
	driver.execute_script("window.scrollTo(0,535.3499755859375)")
	try:
		WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, CONTINUE)))
		last=driver.find_element("link text",CONTINUE)
		driver.execute_script("arguments[0].click();", last)
	except TimeoutException:
		logger.warning('Failed in the last step')

	link=driver.current_url
	logger.info(link)
	driver.quit()
	return link

def get_datas(url):
	driver=Tools.driver
	driver.get(url)
	texts= [y for x in [driver.find_elements('xpath',type) for type in LINK_TYPE] for y in x]
	logger.info(f"{len(texts)} links detected")
	out=[x for x in range(len(texts))]
	return out