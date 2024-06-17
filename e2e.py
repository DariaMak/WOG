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
        assert 1 <= score <= 1000, f"Score {score} is out of range [1, 1000]"
    except Exception as e:
        print(f"An error occurred: {e}")
        assert False, f"Test failed due to error: {e}"
    # finally:
        # driver.quit()
    

def main_function():
    URL = "http://192.168.1.129:80"
    test_scores_service(URL)


main_function()
