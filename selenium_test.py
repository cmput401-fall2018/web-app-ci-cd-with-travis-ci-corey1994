from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_home():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    name = driver.find_element_by_id("name") 
    assert name != None

    about = driver.find_element_by_id("about") 
    assert about != None

    education = driver.find_element_by_id("education") 
    assert education != None

    skills = driver.find_element_by_id("skills") 
    assert skills != None

    work = driver.find_element_by_id("work") 
    assert work != None

    contact = driver.find_element_by_id("contact") 
    assert contact != None

if __name__ == "__main__":
    test_home()
