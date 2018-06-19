
import pytest

from .. import create_app

@pytest.fixture
def client():
	app = create_app()