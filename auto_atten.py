from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
#opts.add_argument('--headless')

#credentials
iengage_url = 'https://iengage.coforgetech.com/'
emp_id = '80308'
password = 'Untangled5*'

#Xpaths of buttons and textboxes
login_xpath = '//*[@id="btnLogin"]'
username_xpath = '//*[@id="txtEmpCode"]'
password_xpath = '//*[@id="txtPassword"]'
submit_xpath = '//*[@id="imgBtnOK"]'
attendence_xpath = '//*[@id="Attendance"]'

browser = Firefox(firefox_options=opts)
browser.get(iengage_url)

browser.find_element_by_xpath(login_xpath).click()
browser.find_element_by_xpath(username_xpath).send_keys(emp_id)
browser.find_element_by_xpath(password_xpath).send_keys(password)
browser.find_element_by_xpath(submit_xpath).click()
browser.find_element_by_xpath(attendence_xpath).click()




