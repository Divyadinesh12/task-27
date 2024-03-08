"""
using data driven testing frameworkDDTF , page object model,explicit wait,expected conditions login into the portal using the username and password provided in the Excel file
"""


# own package
from Data import data
from Locators import Locators
from Methods import methods

# common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# Exception
from selenium.common.exceptions import NoSuchElementException
class Login:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def boot(self):
        """
        This method open the url and maximize window
        :return: None
        """
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def testLogin(self):
     """
     This method check login page is working correctly or not according to valid and invalid username and password
     :return: result
     """
     try:
        self.boot()
        # using loops for taking data like username and password from Excel file
        for row in range(2,7):
            # Username column = 2
            # password column = 3
            # result column = 7
            UserName = methods.WebMethods().readData(row, 2)
            PassWord = methods.WebMethods().readData(row, 3)
            methods.WebMethods().enterText(self.driver, Locators.WebLocator().UserNameLocator, UserName)
            methods.WebMethods().enterText(self.driver, Locators.WebLocator().PasswordLocator, PassWord)
            methods.WebMethods().clickButton(self.driver, Locators.WebLocator().SubmitButton)
            self.driver.implicitly_wait(10)
            print(self.driver.current_url)
            # if current url and dashboard url is equal then this block of code execute
            if self.driver.current_url == data.WebData().DashBoardUrl:
                print("successfully logged In")
                # logout
                methods.WebMethods().clickButton(self.driver, Locators.WebLocator().ImageLocator)
                methods.WebMethods().clickButton(self.driver, Locators.WebLocator().LogOutLocator)
                methods.WebMethods().writeData(row, 7, "PASSED")
            # if current url and dashboard url is not equal then this block of code  execute
            else:
                  print("Login Unsuccessful")
                  methods.WebMethods().writeData(row, 7, "FAILED")

     except NoSuchElementException as e:
       # if element not find in web page then this block of code execute
         print("Error:element is not present in webpage", e)
     finally:
         # finally block of code always execute
         # quit method close the browser
         self.driver.quit()




obj=Login()
obj.testLogin()