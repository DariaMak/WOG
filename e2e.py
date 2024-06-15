from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
    

def test_scores_service(URL: str):
    driver = webdriver.Chrome()
    driver.get(URL)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'score')))
        score_element = driver.find_element(By.ID,'score')
        score = int(score_element.text)
        return 1 <= score <=1000
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    # finally:
        # driver.quit()
    

def main_function():
    URL = "http://192.168.1.129:80"
    result = test_scores_service(URL)
    if result:
        return -1
    else:
        return 0


main_function()
