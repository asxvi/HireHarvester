from selenium import webdriver
from scrape import get_driver, get_jobs_on_page, scrape_all_pages
from argParse import parse_args, construct_url, slugify

if __name__ == '__main__':
    args = parse_args()
    arguments = {
        'role' : args.role,
        'location' : args.location,
        'experience' : args.experience,
        'type' : args.type,
        'pages' : args.pages
    }

    print(arguments)
    construct_url(**arguments) #unpack dictionary and pass as args

    # driver = webdriver.Chrome()
    query = 'https://himalayas.app/jobs/software-engineering'
    # jobs = scrape_all_pages(query)

    
    # for job in jobs:
    #     print(job)
    