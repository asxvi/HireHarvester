from selenium import webdriver
from scrape import scrape_all_pages, scrape_extended_info
from argParse import parse_args, construct_url
from logger import setup_logger
from writeData import clearCSV, writeToCSV

'''
    Parse compilation input
    construct equilavalent url
    scrape every job on each page
    --------------------------------
    todo: scrape each job's page for aditional data like: description, tool stack, experience, DEI initiatives`
'''

if __name__ == '__main__':
    logger = setup_logger()
    logger.info('BEGINNING Program...')
    args = parse_args()
    arguments = {
        'role' : args.role,
        'location' : args.location,
        'experience' : args.experience,
        'type' : args.type,
        'pages' : args.pages
    }
    logger.info(f'Search Parameters: {arguments}')
    driver = webdriver.Chrome()
    logger.info(f'Connected to driver: {driver}')

    URL = construct_url(**arguments) #unpack dictionary and pass as args
    
    jobs = []
    if arguments['pages']:  # this is always true bc pages default =1
        jobs = scrape_all_pages(driver, URL, arguments['pages'])

    '''hopefully can impplement more in depth scraping, but scared to waste time working with DOM when I can just read it myself once I have link'''
    # scrape_extended_info(driver, jobs)
    
    writeToCSV(jobs)

    logger.info('Terminated SUCCESSFULLY')