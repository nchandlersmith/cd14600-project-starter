from logger.logger import Logger

import unittest

class TestLogger(unittest.TestCase):
    def test_logger_formats_the_message(self):
        result = Logger.log("something happened")
        self.assertEqual(result, "[LOG] something happened")
        