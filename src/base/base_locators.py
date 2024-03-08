from typing import Tuple


class BasePageLocators:
    @staticmethod
    def format_locator(
        locator: Tuple[str, str], *args, **kwargs
    ) -> Tuple[str, str]:
        by, value = locator
        formatted_value = value.format(*args, **kwargs)
        return by, formatted_value
