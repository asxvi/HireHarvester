from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import csv
from scrape import setupSel, transformData

# driver = webdriver.Chrome()
# driver.get('https://himalayas.app/jobs/software-engineering')

# page_source = driver.page_source
# soup = BeautifulSoup(page_source, "html.parser")
# # jobs_only = soup.find_all('article', class_='items-start')
# jobs_only = soup.find_all('div', class_='w-full flex-1')


# jobs = []
# for job in jobs_only:
#     # split into 3 primary div elements ending in '_html'
#     title_html = (job.find('a',  class_='text-xl'))
#     job_title = title_html.text if title_html else 'N/A'
#     job_link = ('https://himalayas.app' + title_html['href']) if title_html else 'N/A'

#     more_info_html = job.find('div', class_='mb-6')
#     job_company = more_info_html.find('a').text
#     salaryORemployees = more_info_html.find('p').text if more_info_html.find('p') else 'N/A'
    
#     job_company_size = 'N/A'
#     job_salary = 'N/A'
#     if 'N/A' not in salaryORemployees:
#         split = (salaryORemployees.split())
#         if 'salary' in split[0].lower():
#             job_salary = split[1]
#         elif 'employee' in split[0].lower():
#             job_company_size = split[2]

#     # create a unique id mapped to a link
#     jobs.append([job_title, job_company, job_salary, job_link, job_company_size])



# for job in jobs:
#     print(job)
#     print()


if __name__ == '__main__':
    driver = setupSel()
    data = transformData(driver)

    for d in data:
        print(d)
