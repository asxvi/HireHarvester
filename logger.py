import logging

logger = logging.getLogger()

def setup_logger():
    logging.basicConfig(
    filename= "scraper.log", 
    encoding="utf-8",
    filemode="a",
    style="{",
    format="{asctime} - {levelname} - {message}",
    datefmt= "%m/%d/%Y %I:%M:%S %p",
    level= logging.INFO
    )
    return logger
