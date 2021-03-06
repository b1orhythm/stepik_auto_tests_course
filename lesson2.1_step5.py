from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
	link = "http://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x = browser.find_element_by_id("input_value").text
	y = calc(x)
	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)
	
	browser.find_element_by_css_selector("[for='robotCheckbox']").click()
	browser.find_element_by_css_selector("[for='robotsRule']").click()
	
	button = browser.find_element_by_css_selector("button.btn")
	button.click()


finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()