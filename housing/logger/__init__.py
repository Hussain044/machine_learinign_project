import logging
import datetime
import os

LOG_DIR = 'logs'

CURRENT_TIME_STAMP = f"{datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)
logging.basicConfig(filename=LOG_FILE_PATH, 
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')




