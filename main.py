import asyncio
from playwright.async_api import async_playwright
from identifiers import *
from pahe import *
from settings import Tools

logger=Tools.logger

async def run(playwright,url):
	browser = await playwright.chromium.launch()
	context = await browser.new_context()
	num = await get_count(context,url)
 
	for i in range(0,num):
		new_page = await handle_tab(context,i,url)
		await new_page.locator(HUMAN_VERIFICATION).click()
		await new_page.click(GENERATE)
		second_link = await handle_second_tab(context,new_page)
		await second_link.locator(CONTINUE).click()
		logger.info(second_link.url)
		await second_link.close()
	await browser.close()

async def main():
	url = str(input("Enter the pahe url: "))
	async with async_playwright() as playwright:
		await run(playwright,url)
asyncio.run(main())