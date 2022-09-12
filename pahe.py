import time
from helium import *
from identifiers import *
from settings import Tools

logger=Tools.logger

def get_link(e):
	driver=get_driver()
	go_to('https://pahe.li/the-girl-on-a-bulldozer-2022-web-hd-480p-720p/')
	click(e)
	if driver.current_url !='https://intercelestial.com/':
		driver.close()
		switch_to(find_all(Window())[0])
		logger.debug("changed window")

	wait_until(Text(AGREE_BUTTON).exists,10)
	if Text(AGREE_BUTTON).exists():
		click(Text(AGREE_BUTTON))
		logger.debug("clicked on agree button")
	else:
		logger.warning('no agree button found')

	driver.execute_script("document.getElementById('landing').submit();")

	wait_until(S(GENERATE).exists,30)
	if S(GENERATE).exists():
		click(S(GENERATE))
		logger.debug("clicked on generate button")
	else:
		logger.warning('Not clicked on GENERATE')

	wait_until(S(SHOW_LINK).exists,30)
	if S(SHOW_LINK).exists():
		click(S(SHOW_LINK))
		logger.debug("clicked on download button")
	else:
		logger.warning('Not clicked on DOWNLOAD')

	wait_until(Link(CONTINUE).exists,30)
	final_link=''
	try:
		link=driver.find_element_by_link_text("Continue")
		driver.execute_script("arguments[0].click();", link)
		final_link= driver.current_url
		logger.info(final_link)
	except:
		logger.warning('Not clicked on CONTINUE')
	kill_browser()
	return final_link

def get_datas(url):
	
	go_to(url)
	e= [y.value for x in [find_all(Text(type)) for type in LINK_TYPE if Text(type).exists()] for y in x]
	logger.info(e)
	return e