from selenium import webdriver
from scrape import scrape_all_pages
from argParse import parse_args, construct_url


'''
    Parse compilation input
    construct equilavalent url
    scrape every job on each page
    --------------------------------
    todo: scrape each job's page for aditional data like: description, tool stack, experience, DEI initiatives`
'''

if __name__ == '__main__':
    args = parse_args()
    arguments = {
        'role' : args.role,
        'location' : args.location,
        'experience' : args.experience,
        'type' : args.type,
        'pages' : args.pages
    }

    driver = webdriver.Chrome()
    URL = construct_url(**arguments) #unpack dictionary and pass as args
    jobs = []
    if arguments['pages']:
        jobs = scrape_all_pages(URL, arguments['pages'])

    for job in jobs:
        print(job)
