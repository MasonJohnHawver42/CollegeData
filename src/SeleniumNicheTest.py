from selenium import webdriver
import time
import random


def main():
    colleges = {}

    fileVariable = open("colleges.txt", "r")
    for line in fileVariable:
        PATH = "C:\Coding Programs\chromedriver.exe"
        driver = webdriver.Chrome(PATH)

        driver.get(line)
        print(driver.title)
        time.sleep(random.randint(3, 7))

        acceptance = driver.find_element_by_xpath("//*[@id='admissions']/div[2]/div[1]/div/div/div[2]").text
        if not acceptance[0].isnumeric():
            acceptance = driver.find_element_by_xpath("//*[@id='admissions']/div[2]/div[2]/div/div/div[2]").text
            act = driver.find_element_by_xpath("//*[@id='admissions']/div[2]/div[4]/div/div[2]/div[2]").text
            sat = driver.find_element_by_xpath("//*[@id='admissions']/div[2]/div[4]/div/div[1]/div[2]").text
        else:
            act = driver.find_element_by_xpath("//*[@id='admissions']/div[2]/div[3]/div/div[2]/div[2]").text
            sat = driver.find_element_by_xpath("//*[@id='admissions']/div[2]/div[3]/div/div[1]/div[2]").text
        net = driver.find_element_by_xpath("//*[@id='cost']/div[2]/div[1]/div/div[1]/div[2]").text
        spot = net.find("/")
        net = net[:spot]
        enrollment = driver.find_element_by_xpath("//*[@id='students']/div[2]/div[1]/div/div[1]/div[2]").text
        spot = enrollment.find("U")
        enrollment = enrollment[:spot]
        starting = driver.find_element_by_xpath("//*[@id='after']/div[2]/div[1]/div/div/div[2]").text
        spot = starting.find("/")
        starting = starting[:spot]
        name = driver.find_element_by_xpath("//*[@id='header']/div/div[2]/div[1]/h1").text
        print(name)

        print(acceptance)
        print(act)
        print(sat)
        print(net)
        print(enrollment)
        print(starting)

        colleges[name] = {}
        colleges[name]["act"] = act
        colleges[name]["sat"] = sat
        colleges[name]["acceptance"] = acceptance
        colleges[name]["net"] = net
        colleges[name]["starting"] = starting
        colleges[name]["enrollment"] = enrollment

        print(colleges)

        time.sleep(random.randint(5, 10))
        driver.close()
    fileVariable.close()


main()