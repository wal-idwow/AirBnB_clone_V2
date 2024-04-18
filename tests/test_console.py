#!/usr/bin/python3

import unittest
from unittest.mock import patch
import os
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestCreateCommand(unittest.TestCase):
    """"""
    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db', 'FileStorege test')
    def setUp(self):
        self.command = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_state_with_name(self, mock_stdout):
        self.command.onecmd("create State name=\"California\"")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith("["))  # Assert that output starts with [
        self.assertTrue(output.endswith(")"))    # Assert that output ends with )
        self.assertIn("California", output)       # Assert that "California" is in the output

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_state_without_name(self, mock_stdout):
        self.command.onecmd("create State")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith("["))  # Assert that output starts with [
        self.assertTrue(output.endswith(")"))    # Assert that output ends with )
        self.assertNotIn("name", output)         # Assert that "name" is not in the output

if __name__ == '__main__':
    unittest.main()
