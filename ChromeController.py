from selenium import webdriver


class ChromeController(object):
    PATH="C:\Program Files (x86)\ChromeDriver\chromedriver.exe"


    def initWindow(self):
        self.driver = webdriver.Chrome(self.PATH)

    def openYt(self):
        self.driver.get("https://www.youtube.com/")

    def closeCurrentTab(self):
        window_name=self.driver.window_handles[0]
        self.driver.switch_to.window(window_name=window_name)
        self.driver.close()

    def switchTab(self):
        p = self.driver.current_window_handle
        chwd = self.driver.window_handles
        for w in chwd:
            if (w != p):
                self.driver.switch_to.window(w)

    def newWindow(self):
        self.driver.execute_script('''window.open("http://google.pl","_blank");''')