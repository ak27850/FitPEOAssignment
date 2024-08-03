
#Imported all library Required
from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


#give the location of ms edge driver.exe file
s = Service(r"C:\Users\ak767\Downloads\Edgedriver\msedgedriver.exe")

driver = webdriver.Edge(service=s)
print("Edge browser opened")

#launch the Application
driver.get("https://www.fitpeo.com/home")
driver.maximize_window()
driver.implicitly_wait(10000)

#define function to run all steps
def fitpeo_calc():
  driver.find_element(By.XPATH, "(//div[@class='satoshi MuiBox-root css-1aspamu'])[5]").click()

  # naviagate to little bit down from slider to see proper view
  element1 = driver.find_element(By.XPATH, "//span[@class='MuiTypography-root MuiTypography-caption inter css-43plts']")
  #action class for slider action
  actions = ActionChains(driver)
  actions.move_to_element(element1).perform()
  slider = driver.find_element(By.XPATH, "//span[@class='MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary css-sy3s50']")
  #get the size of slider
  slider_width = int(slider.get_property('offsetWidth'))
  print(slider_width)
  #fir according to size of slider
  ActionChains(driver).click_and_hold(slider).move_by_offset(93, 0).release().perform()
  time.sleep(2)
  driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng']").clear()
  time.sleep(2)
  #click on input box and clear it
  input= driver.find_element(By.XPATH,"//input[@type='number']")
  input.send_keys(Keys.BACKSPACE)
  input.send_keys(Keys.BACKSPACE)
  input.send_keys(Keys.BACKSPACE)
  #input the number mentioned in task
  input.send_keys(560)
  time.sleep(3)
  #click on all checkbox
  checBox1 = driver.find_element(By.XPATH, "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[1]")
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
  #take string  mentioned in Taks
  string1 = ("Total Recurring Reimbursement for all Patients Per Month:"+ "\n" +"$75600")
  print(string1)
  #take string from using locators
  string2 = driver.find_element(By.XPATH, "(//p[@class='MuiTypography-root MuiTypography-body2 inter css-1xroguk'])[4]").text
  print(string2)
  if (string1 == string2):
    print("Both are Equal")
  else:
    print("Not Equal")
  time.sleep(4)
fitpeo_calc()



