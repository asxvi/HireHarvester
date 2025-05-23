import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time



options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")


driver = uc.Chrome(options=options)
driver.get("https://www.indeed.com/jobs?q=data+engineer")
# driver.find_element(By.ID, 'fcckey_filter_button').click()


# driver.get("https://pixelscan.net/fingerprint-check")

time.sleep(30)  # or input("Press Enter to exit...")
    

