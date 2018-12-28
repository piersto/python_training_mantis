from model.project import Project


def test_add_project(app):
    app.session.login('administrator', 'root')
    app.project.open_manage_projects_page()
    old_projects = app.project.get_project_list()
    app.project.add_project()
    project = Project(name='Name24')
    app.project.fill_in_project_form(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=project.name) == sorted(new_projects, key=project.name)

