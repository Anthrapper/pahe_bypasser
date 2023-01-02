from bs4 import BeautifulSoup
from settings import Tools
from identifiers import *
import base64
import re

link_regex = r"location\.href\s*=\s*atob\('(.*?)'\)"
logger=Tools.logger

async def handle_second_tab(context,page):
	async with context.expect_page() as second_page_info:
		await page.click(SHOW_LINK)
	new_page = await second_page_info.value
	await page.close()
	await new_page.wait_for_load_state()
	content=await new_page.content()
	await new_page.close()
	return await get_link(content)

async def get_data(context,url):
	page = await context.new_page()
	await page.goto(url)
	soup = BeautifulSoup(await page.content(), 'html.parser')
	links = soup.find_all('a', class_=LINK_TYPE)
	logger.debug(links)
	await page.close()
	return links

async def get_link(content):
	try:
		link = re.search(link_regex, content).group(1)
		link = base64.b64decode(link).decode('utf-8')
	except (AttributeError, TypeError):
		link = None
	return link