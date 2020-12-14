import logging

LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'

class Logger:
    instance = None

    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            filename='/home/richard/Documents/risk-profile-python/logs/logs.py',
            format=LOG_FORMAT,
            filemode='w'
        )

    def get_instance(self):
        self.instance = logging.getLogger()
        return self.instance