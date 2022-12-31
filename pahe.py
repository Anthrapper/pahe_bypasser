from bs4 import BeautifulSoup
from settings import Tools
from identifiers import *

logger=Tools.logger

async def handle_second_tab(context,page):
	async with context.expect_page() as second_page_info:
		await page.click(SHOW_LINK)
	new_page = await second_page_info.value
	await new_page.wait_for_load_state()
	await page.close()
	return new_page

async def get_data(context,url):
	page = await context.new_page()
	await page.goto(url)
	soup = BeautifulSoup(await page.content(), 'html.parser')
	links = soup.find_all('a', class_=LINK_TYPE)
	logger.debug(links)
	await page.close()
	return links
