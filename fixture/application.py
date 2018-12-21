# -*- coding: utf-8 -*-

from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.orm import ORMFixture


class Application:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" %browser)
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.orm = ORMFixture

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_login_page(self):
        wd = self.wd
        if not (len(wd.find_elements_by_xpath("//form[@id='LoginForm']/input[3]")) > 0):
            wd.get(self.base_url)

    def go_back_to_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Address Book'])[1]/following::a[2]").click()

    def destroy(self):
        self.wd.quit()