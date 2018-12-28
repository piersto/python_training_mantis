# -*- coding: utf-8 -*-

from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def get_project_list(self):
        wd = self.app.wd
        projects = []
        for row in wd.find_elements_by_css_selector("tr.row-1, tr.row-2"):
            cells = row.find_elements_by_tag_name('td')
            name = cells[0].text
            #id = cells[0].find_element_by_name("selected[]").get_attribute('value')
            projects.append(Project(name=name))
        return projects

    def add_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def fill_in_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        self.submit_project_form()
        self.return_to_manage_projects_page()

    def submit_project_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def return_to_manage_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'Proceed')]").click()






























