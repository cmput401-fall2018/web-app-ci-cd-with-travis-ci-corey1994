from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_home():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    elem = driver.find_element_by_id("name") 
    assert elem != None

    elem = driver.find_element_by_id("about") 
    assert elem != None

    elem = driver.find_element_by_id("education") 
    assert elem != None

    elem = driver.find_element_by_id("skills") 
    assert elem != None

    elem = driver.find_element_by_id("work") 
    assert elem != None

    elem = driver.find_element_by_id("contact") 
    assert elem != None

if __name__ == "__main__":
    test_home()
