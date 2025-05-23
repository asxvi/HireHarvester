from selenium import webdriver
from scrape import get_driver, get_jobs_on_page, scrape_all_pages

if __name__ == '__main__':
    driver = webdriver.Chrome()
    query = 'https://himalayas.app/jobs/software-engineering'
    jobs = scrape_all_pages(query)


    for job in jobs:
        print(job)
    