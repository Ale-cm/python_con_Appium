from appium import webdriver

desired_cap = {
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "a21s",
  "automationName": "UiAutomator1",
  "appPackage": "com.sec.android.app.popupcalculator",
  "appActivity": ".Calculator t1508"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
#suma de dos numeros
driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_keypad_btn_07").click()
driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_keypad_btn_add").click()
driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_keypad_btn_08").click()
driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal").click()
