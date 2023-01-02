import asyncio
from playwright.async_api import async_playwright
from identifiers import *
from pahe import get_data, handle_second_tab
from settings import Tools

logger=Tools.logger

async def run(playwright,url):
	browser = await playwright.chromium.launch()
	context = await browser.new_context()
	links = await get_data(context,url)
	for i in range(len(links)):
		new_page = await context.new_page()
		await new_page.goto(links[i]['href'])
		try:
			await new_page.locator(COOKIES_BUTTON).click()
		except:
			pass
		await new_page.locator(HUMAN_VERIFICATION).click()
		await new_page.click(GENERATE)
		final_link = await handle_second_tab(context,new_page)
		logger.info(final_link)
		# for getting cookies pop up
		await context.clear_cookies()
	await browser.close()

async def main():
	url = str(input("Enter the pahe url: "))
	async with async_playwright() as playwright:
		await run(playwright,url)
asyncio.run(main())