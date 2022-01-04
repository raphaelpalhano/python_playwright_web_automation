from playwright.sync_api import Playwright

class BasePage():
    def __init__(self, play: Playwright, conditionScreen=False):
        self.browser = play.chromium.launch(headless=conditionScreen)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
         

    def navigation(self, url, time=0):
        self.page.goto(url)
        self.page.wait_for_timeout(time)
    
    def click_element(self, element):
        self.page.wait_for_selector(element)
        self.page.click(element)

    def get_text_element(self, element):
        self.page.wait_for_selector(element)
        return self.page.text_content(element)

    def get_atribute_element(self, element, attribute):
        self.page.wait_for_selector(element)
        return self.page.get_attribute(element, attribute, strict=False)

    
    def type_text_element(self, element, value):
        self.page.wait_for_selector(element)
        self.page.type(element, value)
    
    def generateScreenShoot(self, element, attribute):
        pathEvidence = f"evidences/images/{self.get_atribute_element(element, attribute)}.png"
        self.page.locator(element).screenshot(path=pathEvidence)

    def closeAll(self):
        self.browser.close()
        self.context.close()
        self.page.close()
    

