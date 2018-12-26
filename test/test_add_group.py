# -*- coding: utf-8 -*-

from model.project import Project


def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Project.id_or_max) == sorted(new_groups, key=Project.id_or_max)

