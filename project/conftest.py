# coding=utf-8

import platform
import pytest

os_system = platform.system()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


def pytest_addoption(parser):
    parser.addoption("--contur", action="store", default="test",
                     help="name of test contur: test, preprod, prod")


@pytest.fixture
def contur(request):
    return request.config.getoption("--contur")


@pytest.fixture()
def api_testing(request):
    contur = request.config.getoption("--contur")
    if contur == "test":
        api_testing.API_URL_PREFICS = "superhero.qa-test.csssr.com"
        api_testing.API_CREDENTIALS = {}
        api_testing.API_TOKEN = ""
    elif contur == "preprod":
        api_testing.API_URL_PREFICS = ""
        api_testing.API_CREDENTIALS = {}
        api_testing.API_TOKEN = ""
    else:
        print("Неизвестный контур, используется контур по умолчанию - test")
    yield api_testing





