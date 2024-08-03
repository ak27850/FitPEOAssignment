
# Import all required libraries
# Project is implemented based on Python and Selenium
from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Provide the edge driver location stored at your machine,
# you need to replace this location
egdeDriver = Service(r"C:\Users\ak767\Downloads\Edgedriver\msedgedriver.exe")

driver = webdriver.Edge(service=egdeDriver)
print("Edge browser launched")


def appInitialization():

  #launch the Application
  driver.get("https://www.fitpeo.com/home")
  driver.maximize_window()
  driver.implicitly_wait(10000)

def navigateToCalculatePage():
  # Navigate to the Revenue Calulator tab
  driver.find_element(By.XPATH, "(//div[@class='satoshi MuiBox-root "
                                "css-1aspamu'])[5]").click()

def validateInputFromSlider():

  # Naviagate to lowere slider section so that it will have proper view of page
  inputTextBox = driver.find_element(
    By.XPATH, "//span[@class='MuiTypography-root MuiTypography-caption "
              "inter css-43plts']")

  # Action class for slider action
  actions = ActionChains(driver)
  actions.move_to_element(inputTextBox).perform()

  #xpath of the slider
  slider = driver.find_element(
    By.XPATH, "//span[@class='MuiSlider-thumb MuiSlider-thumbSizeMedium "
              "MuiSlider-thumbColorPrimary MuiSlider-thumb MuiSlider-thumbSizeMedium "
              "MuiSlider-thumbColorPrimary css-sy3s50']")

  # Get the size of slider
  slider_width = int(slider.get_property('offsetWidth'))

  # Move the slider to particular location as per expected value
  ActionChains(driver).click_and_hold(slider).move_by_offset(
    93, 0).release().perform()

  time.sleep(2)

def enterInputFieldWithExpectedValue():
  driver.find_element(
    By.XPATH,"//input[@class='MuiInputBase-input MuiOutlinedInput-input "
             "MuiInputBase-inputSizeSmall css-1o6z5ng']").clear()

  time.sleep(2)

  # Click on the input box and clear it by backspace key stroke

  inputElement = driver.find_element(By.XPATH, "//input[@type='number']")
  inputElement.send_keys(Keys.BACKSPACE)
  inputElement.send_keys(Keys.BACKSPACE)
  inputElement.send_keys(Keys.BACKSPACE)

  # Input the expected value
  inputElement.send_keys(560)
  time.sleep(3)

def clickExpectedCheckbox():
  actions = ActionChains(driver)

  # Click on all expected checkbox

  checBox1 = driver.find_element(
    By.XPATH, "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[1]")
  actions.move_to_element(checBox1).perform()
  checBox1.click()

  checBox2 = driver.find_element(By.XPATH, "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[2]")
  actions.move_to_element(checBox1).perform()
  checBox2.click()

  checBox3 = driver.find_element(By.XPATH, "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[3]")
  actions.move_to_element(checBox1).perform()
  checBox3.click()

  checBox4 = driver.find_element(By.XPATH, "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[8]")
  actions.move_to_element(checBox1).perform()
  checBox4.click()
  time.sleep(3)

def validateExpectedOutputAmount():

  # Take string  mentioned in Task
  string1 = ("Total Recurring Reimbursement for all Patients Per Month:"+ "\n" +"$75600")
  print(string1)

  #take string from using locators
  string2 = driver.find_element(
    By.XPATH, "(//p[@class='MuiTypography-root MuiTypography-body2 "
              "inter css-1xroguk'])[4]").text
  print(string2)

  if (string1 == string2):
    print("Both are Equal")
  else:
    print("Not Equal")
  time.sleep(4)

def closeBrowser():
  driver.close()

appInitialization()
navigateToCalculatePage()
validateInputFromSlider()
enterInputFieldWithExpectedValue()
clickExpectedCheckbox()
validateExpectedOutputAmount()
closeBrowser()



