class WebLocator:
    """
       This class is used to contain all the locators that are required to perform the testing for the orange HRM
    """
    def __init__(self):
       self.UserNameLocator = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
       self.PasswordLocator = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
       self.SubmitButton = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
       self.ImageLocator = " /html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/img "
       self.LogOutLocator = " /html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a "