import pytest

from core.assistant import Huginn


@pytest.fixture
def huginn():
    return Huginn()


def test_huginn_has_name(huginn):

    assert huginn.name == "Huginn"


def test_huginn_has_version(huginn):

    assert huginn.version == "0.1.0"