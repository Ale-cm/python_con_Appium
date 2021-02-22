
from appium import webdriver

desired_cap= {
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "a21s",
  "automationName": "UiAutomator2",
  "appPackage": "com.sec.android.app.clockpackage",
  "appActivity": ".ClockPackage t1585"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
#Activar alarma
driver.find_element_by_id("com.sec.android.app.clockpackage:id/alarm_onoff_switch").click()


