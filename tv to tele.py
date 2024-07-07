from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

chromedriver_path = 'chromedriver.exe'


code_2fa = input("Masukkan kode 2FA: ")
username = 'yijiwijej@sokpe.com'
password = '@Imortal123!!'

# Mengatur Chrome WebDriver dengan opsi tambahan untuk mematikan notifikasi
service = Service(chromedriver_path)
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=service, options=options)
actions = ActionChains(driver)

# Buka situs TradingView
driver.get('https://www.tradingview.com/')

# Tunggu tombol login muncul dan klik
kepala_btn_xpath = '/html/body/div[3]/div[3]/div[2]/div[3]/button[2]'
login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, kepala_btn_xpath)))
login_btn.click()
time.sleep(2)

# Tunggu tombol sign in muncul dan klik
sign_in_btn_xpath = '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/button[1]/span/span/span/span[2]/span[1]'
sign_in_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, sign_in_btn_xpath)))
sign_in_btn.click()
time.sleep(2)

# Tunggu tombol email sign in muncul dan klik
email_btn_xpath = '/html/body/div[9]/div/div/div[1]/div/div[2]/div[2]/div/div/button'
email_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, email_btn_xpath)))
email_btn.click()

# Tunggu input email muncul dan isi
input_email_xpath = '//*[@id="id_username"]'
input_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_email_xpath)))
input_email.send_keys(username)

# Tunggu input password muncul dan isi
input_pass_xpath = '//*[@id="id_password"]'
input_pass = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_pass_xpath)))
input_pass.send_keys(password)

# Tunggu tombol terakhir sign in muncul dan klik
last_sign_in_btn_xpath = '/html/body/div[9]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/button'
last_sign_in_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, last_sign_in_btn_xpath)))
last_sign_in_btn.click()

# Tunggu input 2FA muncul dan isi
input_2fa_xpath = '//*[@id="id_code"]'
input_2fa = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_2fa_xpath)))
input_2fa.send_keys(code_2fa)

price_box_xpath = '//*[@id="overlap-manager-root"]/div/div/div[1]/form/div[1]/div/div[1]/fieldset/div[2]/div[3]/div/div[2]/span/span[1]/input'
save_btn_xpath = '//*[@id="overlap-manager-root"]/div/div/div[1]/form/div[2]/div/div/button[2]'



#================SELL AREA===============================
# S-C3
element_xpath = "//*[contains(text(), '[S-C3] SELL LR GROWTH 2 ')]/.."
alarm_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
driver.execute_script("arguments[0].scrollIntoView(true);", alarm_element) # Scroll the element into view
time.sleep(1) # Wait for a short time to ensure the element is ready
actions.double_click(alarm_element).perform() # Double click the element
time.sleep(1)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys("555") # set the price
time.sleep(1)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click() # save the alarm





# # S-C2
# sell_LR_G1_xpath = "//*[contains(text(), '[S-C2] SELL LR GROWTH 1 ')]/.."
# sell_LR_G1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, sell_LR_G1_xpath)))
# driver.execute_script("arguments[0].scrollIntoView(true);", sell_LR_G1) # Scroll the element into view
# time.sleep(1) # Wait for a short time to ensure the element is ready
# actions.double_click(sell_LR_G1).perform() # Double click the element





input("Press Enter to close the browser...")