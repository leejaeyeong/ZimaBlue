from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('lang=ko_KR')

# Create a new cromedriver
driver = webdriver.Chrome('./chromedriver.exe',chrome_options=chrome_options)
#driver.implicitly_wait(3)

#full size
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080)
driver.get("http://220.68.79.34/EZ5500/SEAT/ROOMSTATUS.ASPX") # 열람실 현황 조회 


screenshot_name = 'reading_room_status.png'
driver.save_screenshot(screenshot_name)
driver.quit()

# webdriver는 Chrome ver >= 80 에서 동작한다.  
# https://chromedriver.chromium.org/downloads