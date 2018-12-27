from model.project import Project


def test_add_project(app):
    app.session.login()
    app.project.open_manage_projects_page()
    old_projects = app.project.get_project_list()
    app.project.add_project()
    app.contact.fill_in_project_form(Project(name='Name'))
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)

