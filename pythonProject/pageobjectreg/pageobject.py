from selenium.webdriver.common.by import By


class registration1:
    myaccountlink = "My Account"
    registrationlink = "Register"
    enterfirstname = "input-firstname"
    enterlastname = "input-lastname"
    emailid = "input-email"
    password = "input-password"
    checkboxclick = "agree"
    submitbutton = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def clikmyaccountlink(self):
        self.driver.find_element(By.LINK_TEXT, self.myaccountlink).click()

    def clickonregisterlink(self):
        self.driver.find_element(By.LINK_TEXT, self.registrationlink).click()

    def inputfirstname(self, firstname):
        self.driver.find_element(By.ID, self.enterfirstname).send_keys(firstname)

    def inputlastname(self, lastname):
        self.driver.find_element(By.ID, self.enterlastname).send_keys(lastname)

    def enteremail(self, username):
        self.driver.find_element(By.ID, self.emailid).send_keys(username)

    def enterpassword(self, password):
        self.driver.find_element(By.ID, self.password).send_keys(password)

    def checkbox(self):
        self.driver.find_element(By.NAME, self.checkboxclick).click()

    def clickonsubmit(self):
        self.driver.find_element(By.XPATH, self.submitbutton).click()
