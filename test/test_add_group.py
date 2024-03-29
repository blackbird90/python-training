# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="testr1", header="dsfsdsdf", footer="sdffsddf"))
    app.session.logout()

