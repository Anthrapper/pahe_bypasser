import logging.config


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
