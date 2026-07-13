import pytest

from core.assistant import Huginn


@pytest.fixture
def huginn():
    return Huginn()


def test_huginn_has_name(huginn):

    assert huginn.name == "Huginn"


def test_huginn_has_version(huginn):

    assert huginn.version == "0.1.0"

def test_huginn_can_receive_a_custom_name():

    huginn = Huginn(name="Odin")

    assert huginn.name == "Odin"

def test_huginn_has_empty_interests(huginn):

    assert huginn.interests == []

def test_huginn_can_add_interest(huginn):

    huginn.add_interest("Wakfu")
    huginn.add_interest("Hearthstone Battlegrounds")
    huginn.add_interest("Python")

    assert huginn.interests == [
    "Wakfu",
    "Hearthstone Battlegrounds",
    "Python"
]