
def test_add_project(app):
    old_groups = app.group.get_group_list()
    app.group.create_group(Group(name='Name group', header='Group header', footer='Group footer'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)