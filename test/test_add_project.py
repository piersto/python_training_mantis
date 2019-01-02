from model.project import Project
import pytest
import random
import string


def random_string(prefix, maxlen):
    # string will be chosen from letters, digits and 10 spaces -- ' '*10
    symbols = string.ascii_letters + string.digits + ' '*5
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    # will generate random string that starts with word 'Name' or 'Header etc and + some more random symbols
    Project(name=random_string('Name', (10)))
    ]


@pytest.mark.parametrize('project', testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    app.session.login('administrator', 'root')
    app.project.open_manage_projects_page()
    old_projects = app.project.get_project_list()
    app.project.add_project()
    app.project.fill_in_project_form(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=project.name) == sorted(new_projects, key=project.name)

