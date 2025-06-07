import os
import csv
from datetime import datetime
from logger import setup_logger

logger = setup_logger()

# helper function to quickly remove all garbage/ outdated CSV's
def clearCSV():
    csv_files = [file for file in os.listdir() if file.endswith('.csv')]
    if not csv_files:
        print("No CSV files in directory")
        return
    
    for file in csv_files:
        print(file) 
    
    confirm = input("Do you want to remove all of these files for good? (y/n): ").lower()
    if confirm:
        for file in csv_files:
            os.remove(file)


def writeToCSV(jobs):
    currTime = datetime.now().strftime("%Y%m%d_%H:%M")
    file_exists = os.path.isfile(f"jobData_{currTime}.csv")
    with open(f'jobData_{currTime}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter= ",")

        if not file_exists:
            writer.writerow(["Role", "Company", "Salary", "Company Size", "full link"])
            logger.info("File not exist. Creating file and Header")
        writer.writerows(job for job in jobs)


if __name__ == "__main__":
    clearCSV()