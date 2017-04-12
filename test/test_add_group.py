# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_group(self):
    self.app.login(username="admin", password="secret")
    self.app.create_group(Group(name="testr1", header="dsfsdsdf", footer="sdffsddf")
    self.app.logout()

