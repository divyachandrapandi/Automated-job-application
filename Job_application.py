from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# ----------------------------LOGIN INFO----------------------------------------#
EMAIL = YOUR EMAIL
PASS_KEY = PASSWORD

# ----------------------------URL----------------------------------------#
JOB_URL = LINKEDIN JOB URL WITH FILTER <JOB POSITION> AND <EASY APPLY>
LOGIN_URL = "https://www.linkedin.com/checkpoint/lg/sign-in-another-account"

# ----------------------------DRIVER SETUP----------------------------------------#
chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

# --------------------------LOGIN------------------------------------------#
driver.get(LOGIN_URL)
# Email keys
email_tag = driver.find_element(By.ID, "username")
email_tag.send_keys(EMAIL)
# Password Keys
pass_tag = driver.find_element(By.ID, "password")
pass_tag.send_keys(PASS_KEY)
# submit Keys
submit = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
submit.send_keys(Keys.ENTER)

# ----------------------------JOB SITE ----------------------------------------#
time.sleep(5)
driver.get(JOB_URL)

# # jobs are listed and send into for loop

jobs = driver.find_elements(By.CSS_SELECTOR,
                            'body > div.application-outlet > div.authentication-outlet > div.job-search-ext > '
                            'div.jobs-search-two-pane__wrapper > div > section.jobs-search__left-rail > div > div > '
                            'ul > li')
for job in jobs:
    job.click()
    time.sleep(2)

#    # find easy apply button and click it
    try:
        easy_apply_check = driver.find_element(By.CSS_SELECTOR, "div.mt5 > div.display-flex > div > div > button")
        print(easy_apply_check.text)
        easy_apply = driver.find_element(By.CSS_SELECTOR, "div.mt5 > div.display-flex > div > div > button")
        easy_apply.click()
        time.sleep(5)
        # if submit application is not found
        try:
            submit_application = driver.find_element(By.CSS_SELECTOR, "footer button")
            submit_application.click()
            time.sleep(2)
        # search for next button
        except NoSuchElementException:
            buttons = driver.find_elements(By.CSS_SELECTOR, "form > footer > div > button")
            next_button = buttons[1]
            next_button.click()
            time.sleep(2)
            # again no submit button
            try:
                submit_application = driver.find_element(By.CSS_SELECTOR, "footer button")
                submit_application.click()
            # close button and discard the application
            except NoSuchElementException:
                time.sleep(2)
                close_t = driver.find_element(By.CSS_SELECTOR,
                                              " div.jobs-easy-apply-modal > button > li > span.artdeco-button__text")
                close_t.click()
                discard = driver.find_element(By.CSS_SELECTOR,
                                              "div.artdeco-modal artdeco-modal--layer-confirmation > div > button > "
                                              "span.artdeco-button__text")
                continue # skip the application

    # if not easyapply found , skip application
    except NoSuchElementException:

        applied = driver.find_element(By.CSS_SELECTOR,
                                      "div.mt5 > div.display-flex >div > div > span.artdeco-inline-feedback__message")
        if applied.text.split(" ")[0] == "Applied":
            print("applied")
            continue

time.sleep(10)
driver.quit()
