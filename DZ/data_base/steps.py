from behave import given, when, then
from data_base.sqlite_db_test import *

@given('I have db name = tour.db')
def step(context, x='tour.db'):
    context.x = sqlite_db.sql_start(x)

@when('I open db')
def step(context):
    with pytest.raises(TypeError):
        sqlite_db.sql_start(context.x)

@given('I expect to get 1 == result[0]')
def step(context, result):
    base = sqlite_db.sql_start(':memory:')
    result = base.execute('SELECT count(name) FROM sqlite_master WHERE type=\'table\' AND name=\'menu\';').fetchone()
    assert 1 == result[0]