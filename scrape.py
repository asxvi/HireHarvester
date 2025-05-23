from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def get_driver() -> webdriver:
    return webdriver.Chrome()

    
def get_jobs_on_page(driver, url):
    driver.get(url)
    time.sleep(2)
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    jobs_only = soup.find_all('div', class_='w-full flex-1')


    jobs = []
    for job in jobs_only:
        # split into 3 primary div elements ending in '_html'
        title_html = (job.find('a',  class_='text-xl'))
        job_title = title_html.text if title_html else 'N/A'
        job_link = ('https://himalayas.app' + title_html['href']) if title_html else 'N/A'

        more_info_html = job.find('div', class_='mb-6')
        job_company = more_info_html.find('a').text
        salaryORemployees = more_info_html.find('p').text if more_info_html.find('p') else 'N/A'
        
        job_company_size = 'N/A'
        job_salary = 'N/A'
        if 'N/A' not in salaryORemployees:
            split = (salaryORemployees.split())
            if 'salary' in split[0].lower():
                job_salary = split[1]
            elif 'employee' in split[0].lower():
                job_company_size = split[2]

        # create a unique id mapped to a link
        jobs.append([job_title, job_company, job_salary, job_link, job_company_size])

    return jobs


# paginate all results
def scrape_all_pages(query):
    driver = get_driver()

    page = 1
    all_jobs = []
    while True:
        print(f"Scraping page {page}")
        url = f"{query}?page={page}"
        jobs = get_jobs_on_page(driver, url)

        if(page >= 6):
            break

        if not jobs:
            print("No more jobs found. Exiting.")
            break
        
        page+=1
        all_jobs.extend(jobs)
    
    driver.quit()
    return all_jobs