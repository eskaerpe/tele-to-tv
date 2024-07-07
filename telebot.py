import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time



print("Bot berhasil dijalankan. Kalo ada error ss ke sul aja")

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

def open_tradingview(prices):
    username = os.getenv('USN')
    password = os.getenv('PW')
    code_2fa = prices[0]
    sLR_G2 = int(prices[1])
    sLR_G1 = int(prices[2])
    sLR_UM = int(prices[3])
    sMR_G2 = int(prices[4])
    sMR_G1 = int(prices[5])
    sMR_UM = int(prices[6])
    sHR_G2 = int(prices[7])
    sHR_G1 = int(prices[8])
    sHR_UM = int(prices[9])
    bHR_UM = int(prices[10])
    bHR_G1 = int(prices[11])
    bHR_G2 = int(prices[12])
    bMR_UM = int(prices[13])
    bMR_G1 = int(prices[14])
    bMR_G2 = int(prices[15])
    bLR_UM = int(prices[16])
    bLR_G1 = int(prices[17])
    bLR_G2 = int(prices[18])
    chromedriver_path = 'chromedriver.exe'

    service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")  # Set window size for headless mode

    driver = webdriver.Chrome(service=service, options=options)
    actions = ActionChains(driver)

    # Buka situs TradingView
    driver.get('https://www.tradingview.com/')

    # Tunggu tombol login muncul dan klik
    kepala_btn_xpath = '/html/body/div[3]/div[3]/div[2]/div[3]/button[2]'
    login_btn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, kepala_btn_xpath)))
    login_btn.click()
    time.sleep(2)

    # Tunggu tombol sign in muncul dan klik
    sign_in_btn_xpath = '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/button[1]/span/span/span/span[2]/span[1]'
    sign_in_btn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, sign_in_btn_xpath)))
    sign_in_btn.click()
    time.sleep(2)

    # Tunggu tombol email sign in muncul dan klik
    email_btn_xpath = '/html/body/div[9]/div/div/div[1]/div/div[2]/div[2]/div/div/button'
    email_btn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, email_btn_xpath)))
    email_btn.click()

    # Tunggu input email muncul dan isi
    input_email_xpath = '//*[@id="id_username"]'
    input_email = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, input_email_xpath)))
    input_email.send_keys(username)

    # Tunggu input password muncul dan isi
    input_pass_xpath = '//*[@id="id_password"]'
    input_pass = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, input_pass_xpath)))
    input_pass.send_keys(password)

    # Tunggu tombol terakhir sign in muncul dan klik
    last_sign_in_btn_xpath = '/html/body/div[9]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/button'
    last_sign_in_btn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, last_sign_in_btn_xpath)))
    last_sign_in_btn.click()

    # Tunggu input 2FA muncul dan isi
    input_2fa_xpath = '//*[@id="id_code"]'
    input_2fa = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, input_2fa_xpath)))
    input_2fa.send_keys(code_2fa)

    price_box_xpath = '//*[@id="overlap-manager-root"]/div/div/div[1]/form/div[1]/div/div[1]/fieldset/div[2]/div[3]/div/div[2]/span/span[1]/input'
    save_btn_xpath = '//*[@id="overlap-manager-root"]/div/div/div[1]/form/div[2]/div/div/button[2]'


#################################################################################################################################
    # ============ S-C3 ============= 
    sell_LR_G2_xpath = "//*[contains(text(), '[S-C3] SELL LR GROWTH 2 ')]/.."
    sell_LR_G2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, sell_LR_G2_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", sell_LR_G2)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(sell_LR_G2).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(sLR_G2)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

    # ============ S-C2 ============= 
    sell_LR_G1_xpath = "//*[contains(text(), '[S-C2] SELL LR GROWTH 1 ')]/.."
    sell_LR_G1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, sell_LR_G1_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", sell_LR_G1)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(sell_LR_G1).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(sLR_G1)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

    # ============ S-C1 ============= 
    sell_LR_UM_xpath = "//*[contains(text(), '[S-C1] SELL LR UMUM')]/.."
    sell_LR_UM = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, sell_LR_UM_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", sell_LR_UM)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(sell_LR_UM).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(sLR_UM)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

#################################################################################################################################

    # ============ S-B3 ============= 
    sell_MR_G2_xpath = "//*[contains(text(), '[S-B3] SELL MR GROWTH 2 ')]/.."
    sell_MR_G2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, sell_MR_G2_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", sell_MR_G2)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(sell_MR_G2).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(sMR_G2)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

    # ============ S-B2 ============= 
    sell_MR_G1_xpath = "//*[contains(text(), '[S-B2] SELL MR GROWTH 1 ')]/.."
    sell_MR_G1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, sell_MR_G1_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", sell_MR_G1)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(sell_MR_G1).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(sMR_G1)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

    # ============ S-B1 ============= 
    sell_MR_UM_xpath = "//*[contains(text(), '[S-B1] SELL MR UMUM')]/.."
    sell_MR_UM = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, sell_MR_UM_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", sell_MR_UM)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(sell_MR_UM).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(sMR_UM)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

#################################################################################################################################

    # ============ S-A3 ============= 
    sell_HR_G2_xpath = "//*[contains(text(), '[S-A3] SELL HR GROWTH 2 ')]/.."
    sell_HR_G2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, sell_HR_G2_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", sell_HR_G2)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(sell_HR_G2).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(sHR_G2)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

    # ============ S-A2 ============= 
    sell_HR_G1_xpath = "//*[contains(text(), '[S-A2] SELL HR GROWTH 1 ')]/.."
    sell_HR_G1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, sell_HR_G1_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", sell_HR_G1)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(sell_HR_G1).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(sHR_G1)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

    # ============ S-A1 ============= 
    sell_HR_UM_xpath = "//*[contains(text(), '[S-A1] SELL HR UMUM')]/.."
    sell_HR_UM = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, sell_HR_UM_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", sell_HR_UM)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(sell_HR_UM).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(sHR_UM)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

#################################################################################################################################

    # ============ B-C3 ============= 
    buy_HR_UM_xpath = "//*[contains(text(), '[B-C3] BUY HR UMUM')]/.."
    buy_HR_UM = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, buy_HR_UM_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", buy_HR_UM)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(buy_HR_UM).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(bHR_UM)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

    # ============ B-C2 ============= 
    buy_HR_G1_xpath = "//*[contains(text(), '[B-C2] BUY HR GROWTH 1')]/.."
    buy_HR_G1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, buy_HR_G1_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", buy_HR_G1)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(buy_HR_G1).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(bHR_G1)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

    # ============ B-C1 ============= 
    buy_HR_G2_xpath = "//*[contains(text(), '[B-C1] BUY HR GROWTH 2')]/.."
    buy_HR_G2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, buy_HR_G2_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", buy_HR_G2)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(buy_HR_G2).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(bHR_G2)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

#################################################################################################################################

    # ============ B-B1 ============= 
    buy_MR_UM_xpath = "//*[contains(text(), '[B-B3] BUY MR UMUM')]/.."
    buy_MR_UM = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, buy_MR_UM_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", buy_MR_UM)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(buy_MR_UM).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(bMR_UM)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

    # ============ B-B2 ============= 
    buy_MR_G1_xpath = "//*[contains(text(), '[B-B2] BUY MR GROWTH 1')]/.."
    buy_MR_G1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, buy_MR_G1_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", buy_MR_G1)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(buy_MR_G1).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(bMR_G1)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

    # ============ B-B3 ============= 
    buy_MR_G2_xpath = "//*[contains(text(), '[B-B1] BUY MR GROWTH 2')]/.."
    buy_MR_G2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, buy_MR_G2_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", buy_MR_G2)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(buy_MR_G2).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(bMR_G2)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

#################################################################################################################################
     
     # ============ B-A1 ============= 
    buy_LR_UM_xpath = "//*[contains(text(), '[B-A3] BUY LR UMUM')]/.."
    buy_LR_UM = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, buy_LR_UM_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", buy_LR_UM)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(buy_LR_UM).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(bLR_UM)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

    # ============ B-A2 ============= 
    buy_LR_G1_xpath = "//*[contains(text(), '[B-A2] BUY LR GROWTH 1')]/.."
    buy_LR_G1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, buy_LR_G1_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", buy_LR_G1)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(buy_LR_G1).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(bLR_G1)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm

    # ============ B-A3 ============= 
    buy_LR_G2_xpath = "//*[contains(text(), '[B-A1] BUY LR GROWTH 2')]/.."
    buy_LR_G2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, buy_LR_G2_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", buy_LR_G2)  # Scroll the element into view
    time.sleep(1)  # Wait for a short time to ensure the element is ready
    actions.double_click(buy_LR_G2).perform()  # Double click the element
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, price_box_xpath))).send_keys(bLR_G2)  # set the price
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath))).click()  # save the alarm
     
     
    print("done sir")

# Function to handle the /start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Maaf bot ini hanya untuk Owner dan Admin.")

# Function to handle the /help command
async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("Maaf bot ini hanya untuk Owner dan Admin.")

async def update_signal(update: Update, context: CallbackContext):
    print(context.args)
    if context.args[0] == "help":
        await update.message.reply_text("Gunakan format ini: /update_signal 2FA_code sLR_G2 sLR_G1 sLR_UM sMR_G2 sMR_G1 sMR_UM sHR_G2 sHR_G1 sHR_UM bHR_UM bHR_G1 bHR_G2 bMR_UM bMR_G1 bMR_G2 bLR_G2 bLR_UM bLR_UM bLR_G1 bLR_G2")
        return
    # prices = context.args()
    
    open_tradingview(context.args)


def main():
    # Initialize the Application with the bot token
    application = Application.builder().token(TOKEN).build()

    # Add handlers for the /start and /help commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))

    application.add_handler(CommandHandler("update_signal", update_signal))
    # Start polling for new messages
    application.run_polling()

if __name__ == '__main__':
    main()
