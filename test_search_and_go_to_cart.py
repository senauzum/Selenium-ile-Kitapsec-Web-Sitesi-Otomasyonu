from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from time import sleep
chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
video_url="https://www.kitapsec.com/"
driver.get(video_url)

wait = WebDriverWait(driver, 15)

print(f"Bulunduğunuz sayfanın linki:{driver.current_url}")
print(f"Sayfa Başlığı:{driver.title}")
driver.maximize_window()
sleep(3)
 
search_box=driver.find_element(By.ID,"yeniAramaInput")
search_box.send_keys("Kürk Mantolu Madonna")
sleep(1)
driver.find_element(By.XPATH,'//*[@id="SearchNewForm1"]/a').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@id="42699"]/a[2]/span').click()
sleep(1)
driver.execute_script("window.scrollBy(0,250)")
sleep(2)
driver.find_element(By.XPATH,'//*[@id="https://www.kitapsec.com/Products/Kurk-Mantolu-Madonna-Yapi-Kredi-Yayinlari-42699.html"]/div[1]/div[2]/div[4]/a[2]').click()
sleep(1)

wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.sweet-overlay")))

wait.until(EC.element_to_be_clickable((By.ID, "sptHdCountText"))).click()


sleep(2)
driver.quit()