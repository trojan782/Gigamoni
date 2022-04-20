import os
from selenium import webdriver

os.environ['PATH'] += r"C:\Users\Wonder\Gigasec_proj\gigamoni"
driver = webdriver.Chrome()
driver.get("https://search.cac.gov.ng/home")
driver.implicitly_wait(8)
search_bar = driver.find_element_by_class_name("search-query")
search_bar.send_keys('gigasec')

search_btn = driver.find_element_by_class_name("btn_search")
search_btn.click()