import concurrent.futures
import time
from pahe import get_link,get_datas
from settings import Tools

logger=Tools.logger
driver=Tools.driver

def multip(url):
	e = get_datas(url)

	with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executer:
		executer.map(get_link,[e,url,True])
	
	t2=time.perf_counter()
	Tools.logger.info(f"Total time taken is {t2-t1} seconds")
	driver.quit()	

def loop(url):
	e= get_datas(url)
	for i in e:
		get_link(i,url,False)
	t2=time.perf_counter()
	Tools.logger.info(f"Total time taken is {t2-t1} seconds")
	driver.quit()

if __name__ == '__main__':
	url = str(input("Enter the pahe url: "))
	proc_type= 'seq'
	t1=time.perf_counter()
	if proc_type=='seq':
		loop(url)
	else:
		multip(url)
