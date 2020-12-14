from unittest.mock import MagicMock

logger = MagicMock(return_value=None)

def mock_function(self):
    return

logger.info = mock_function