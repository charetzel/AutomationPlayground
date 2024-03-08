import pytest


class BaseCase:
    driver = None
    config = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, config):
        # Setup driver
        self.driver = driver
        self.config = config
