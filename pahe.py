from settings import Tools
from identifiers import *

logger=Tools.logger

async def handle_tab(context,i,url):
	while True:
		page = await context.new_page()
		await page.goto(url)
		async with context.expect_page() as new_page_info:
			await page.locator(LINK_TYPE[0]).nth(i).click()
		new_page = await new_page_info.value
		await new_page.wait_for_load_state()
		if 'https://intercelestial.com/' in new_page.url:
			await page.close()
			break
		await new_page.close()
		await page.close()
	return new_page

async def handle_second_tab(context,page):
	async with context.expect_page() as second_page_info:
		await page.click(SHOW_LINK)
	new_page = await second_page_info.value
	await new_page.wait_for_load_state()
	await page.close()
	return new_page

async def get_count(context,url):
	page = await context.new_page()
	await page.goto(url)
	num =await page.locator(LINK_TYPE[0]).count()
	logger.info(f" found {num} links")
	await page.close()
	return num
