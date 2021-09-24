from core.constants import WORKSPACE_PATH
import datetime
import logging
import os

LOG_DIR = os.path.join(WORKSPACE_PATH, "logs")

if not os.path.isdir(LOG_DIR):
    os.mkdir(LOG_DIR)

log_file = os.path.join(LOG_DIR, f"log-{datetime.datetime.now().date()}.log")
logging.basicConfig(filename=log_file, format="%(asctime)s %(message)s", filemode="a")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def info(msg: str):
    logger.info(msg)


def warning(msg: str):
    logger.warning(msg)


def error(msg: str):
    logger.error(msg)
