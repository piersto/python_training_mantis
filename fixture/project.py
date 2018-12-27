# -*- coding: utf-8 -*-

from model.project import Project

class ProjectHelper:
    from selenium.webdriver.support.select import Select

    def __init__(self, app):
        self.app = app

    def submit_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def fill_in_contact_form(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        self.fill_contact_form(contact)
        self.specify_drop_downs(contact)
        self.submit_contact_form()
        self.app.return_on_home_page()

    def specify_drop_downs(self, contact):
        wd = self.app.wd
        self.select_in_drop_down('bday', contact.birthday)
        self.select_in_drop_down('bmonth', contact.birth_month)

    def select_in_drop_down(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('middlename', contact.middlename)
        self.change_field_value('lastname', contact.lastname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # click modification button
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # specify new data
        self.fill_contact_form(new_contact_data)
        self.specify_drop_downs(new_contact_data)
        # click update button
        wd.find_element_by_name("update").click()
        # return to home page
        self.app.return_on_home_page()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for row in wd.find_elements_by_name("entry"):
            cells = row.find_elements_by_tag_name('td')
            firstname = cells[1].text
            lastname = cells[2].text
            id = cells[0].find_element_by_name("selected[]").get_attribute('value')
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts

    def open_manage_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_manage_projects_page()
        projects = []
        for row in wd.find_elements_by_name("row-1"):
            cells = row.find_elements_by_tag_name('td')
            name = cells[0].text
            id = cells[0].find_element_by_name("selected[]").get_attribute('value')
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts































