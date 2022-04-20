def verify_rc(rc_no):
    import os
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    os.environ['PATH'] += r"C:\Users\Wonder\Gigasec_proj\gigamoni"
    driver = webdriver.Chrome()
    driver.get("https://search.cac.gov.ng/home")
    driver.implicitly_wait(20)
    search_bar = driver.find_element(by=By.CLASS_NAME, value='search-query')
    search_bar.send_keys(rc_no)
    
    search_btn = driver.find_element(by=By.CLASS_NAME, value="btn_search")
    search_btn.click()
    
    confirm_elem = driver.find_element(by=By.CLASS_NAME, value="strip_list")
    text = confirm_elem.text
    
    if (text.find(f"RC - {rc_no}") != -1):
        return True
    else:
        return False
