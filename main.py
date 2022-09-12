import concurrent.futures
import time
from pahe import get_link,get_datas
from settings import Tools
from helium import *

logger=Tools.logger
driver=Tools.driver

def multip():
	e = get_datas('https://pahe.li/the-girl-on-a-bulldozer-2022-web-hd-480p-720p/')
	logger.info(e)
	logger.info(f"{len(e)} links detected")

	with concurrent.futures.ProcessPoolExecutor() as executer:
		executer.map(get_link,e)
		
	t2=time.perf_counter()
	Tools.logger.info(f"Total time taken is {t2-t1} seconds")
	driver.quit()	
		
if __name__ == '__main__':
	t1=time.perf_counter()
	multip()