# coding=utf-8
import transaction
from tracim.tests import eq_
from tracim.tests import BaseTest
from tracim.models.auth import Permission


class TestPermissionModel(BaseTest):
    """
    Test for permission model
    """
    def test_unit__create__ok__nominal_case(self):
        self.session.flush()
        transaction.commit()

        name = 'my_permission'
        description = 'my_perm_description'
        permission = Permission()
        permission.permission_name = name
        permission.description = description

        self.session.add(permission)
        self.session.flush()
        transaction.commit()

        new_permission = self.session.query(Permission).filter(permission.permission_name == name).one()  # nopep8

        assert new_permission.permission_name == name
        assert new_permission.description == description
        assert new_permission.permission_id
        assert isinstance(new_permission.permission_id, int)
        # TODO - G.M -24-05-2018 - Do test for groups

    def test_unit__repr__ok__nominal_case(self):
        name = 'my_permission'
        description = 'my_perm_description'
        permission = Permission()
        permission.permission_name = name
        permission.description = description

        assert permission.__repr__() == "<Permission: name='my_permission'>"

    def test_unit__unicode__ok__nominal_case(self):
        name = 'my_permission'
        description = 'my_perm_description'
        permission = Permission()
        permission.permission_name = name
        permission.description = description

        assert permission.__unicode__() == name

