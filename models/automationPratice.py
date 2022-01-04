
from fixtures.pageAcess import automationPratice as data
from models.basePage import BasePage

class AutomationPratice():
    def __init__(self, basePage: BasePage):
        self.control = basePage

    def go_url(self):
        self.control.navigation(data["url"])
            
    def click_button_sign(self):
        self.control.click_element("a[class='login']")

    def type_username_and_password(self):
        self.control.generateScreenShoot("#login_form", "method")
        self.control.type_text_element("input[id='email']", data["username"])
        self.control.type_text_element("input[id='passwd']", data["password"])

    def click_button_sign_acess(self):
        self.control.generateScreenShoot("#SubmitLogin", "name")
        self.control.click_element("#SubmitLogin")


    def text_after_login(self):
        text = self.control.get_text_element("//span[contains(text(), 'My personal information')]")
        return text
    
    def closeBrowser(self):
        self.control.closeAll()