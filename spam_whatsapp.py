from selenium import webdriver
from time import sleep


class color : 
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

print(color.GREEN + "[0]" + color.WHITE + " create by " + color.RED + "SADEGH.PETROS & MOHAMMAD.ZAREI\n")

input("ENTER >>> ")

# driver.find_element_by_xpath("//span[contains(text, '')]").click()
# sleep(5)


name = input("Name target >>> ")
text = input("matn >>> ")
time = int(input("adad >>> "))

input("ENTER TO START >>> ")

for i in range(time):
    ex = driver.find_element_by_xpath("//span[@title ='{}']".format(name))
    ex.click
    # sleep(1)
    driver.find_elements_by_class_name('_2_1wd ')[1].send_keys(text, i)
    # sleep(0)
    driver.find_elements_by_class_name('_1E0Oz')[0].click()
