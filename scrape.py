from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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
        jobs.append([job_title, job_company, job_salary, job_company_size, job_link])

    return jobs

# paginate all results
def scrape_all_pages(driver, query, stopAt:int = None):
    # driver = get_driver()

    page = 1
    all_jobs = []
    exitFlag = False
    while True:
        print(f"Scraping page {page}")
        url = f"{query}&page={page}"
        jobs = get_jobs_on_page(driver, url)

        # user defined stop
        if(stopAt and page >= stopAt):
            print(f"Stopping search after {stopAt} pages.")
            exitFlag = True
            # break

        if not jobs:
            print("No more jobs found. Exiting Gracefully.")
            exitFlag = True
            # break
        
        page+=1
        all_jobs.extend(jobs)
        
        if(exitFlag):
            break
    # driver.quit()
    return all_jobs

# gather more info from each jobs specific link
def scrape_extended_info(driver, data):    
    rv_data = []

    for curr in data:
        print(curr)
        currUrl = curr[4] 
        driver.get(currUrl)
        
        # create temp driver to fetch the link bc website uses their local path in href link to job
        tempDriver = webdriver.Chrome()
        tempDriver.get(currUrl)
        tempDriver.find_element(By.CSS_SELECTOR, '.inline-flex.gap-x-2').click()
        WebDriverWait(tempDriver, 10).until(lambda d: len(d.window_handles) > 1)
        tempDriver.switch_to.window(tempDriver.window_handles[1])
        print("Redirected to:", tempDriver.current_url)
        


        soup = BeautifulSoup(driver.page_source, "html.parser")
        mainDiv = soup.find('div', class_='flex flex-col gap-x-16 xl:flex-row')
        leftSection = mainDiv.contents[0]
        rightSection = mainDiv.contents[1]
        # job_application_link = rightSection.find('a', class_='inline-flex')

        break
