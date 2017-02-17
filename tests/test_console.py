#!/usr/bin/python3
"""
This is the 'test_console' module.

test_console uses unittest to test the 'console' module.
All credit for this module goes to Danton Rodriguez
(https://github.com/p0516357)
"""
import sys
import unittest
from test import support
from test.support import captured_stdout, captured_stderr
from unittest.mock import create_autospec
from console import hbnb
from io import StringIO


class TestConsole(unittest.TestCase):
    """Test console class"""
    no_instance = "** no instance found **\n"
    no_class = "** class doesn't exist **\n"
    missing_class = "** class name missing **\n"
    missing_id = "** instance id missing **\n"

    def setUp(self):
        """setup method for Console Test Class"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.mock_stderr = create_autospec(sys.stderr)

    def create(self, server=None):
        """create method is a helper function for test class"""
        return hbnb(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_exit(self):
        """exit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))

    def test_EOF(self):
        """exit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("EOF"))

    def test_create_err(self):
        """test method for do_create method errors"""
        cli = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            expected = "** class name missing **\n"
            self.assertFalse(cli.onecmd("create"))
            self.assertEqual(expected, stdout.getvalue())

        with captured_stdout() as stdout, captured_stderr() as stderr:
            expected = "** class doesn't exist **\n"
            self.assertFalse(cli.onecmd("create airplanes"))
            self.assertEqual(expected, stdout.getvalue())

    def test_show_error(self):
        """test method for do_show method errors"""
        cli = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("show"))
            self.assertEqual(TestConsole.missing_class, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("show Korea"))
            self.assertEqual(TestConsole.no_class, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("show BaseModel AA"))
            self.assertEqual(TestConsole.no_instance, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("show BaseModel"))
            self.assertEqual(TestConsole.missing_id, stdout.getvalue())

    def test_destroy_error(self):
        """test method for do_destroy method errors"""
        cli = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("destroy"))
            self.assertEqual(TestConsole.missing_class, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("destroy Korea"))
            self.assertEqual(TestConsole.no_class, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("destroy BaseModel AA"))
            self.assertEqual(TestConsole.no_instance, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("destroy BaseModel"))
            self.assertEqual(TestConsole.missing_id, stdout.getvalue())

    def test_all_error(self):
        """test method for do_all method errors"""
        cli = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("all PeterPans"))
            self.assertEqual(TestConsole.no_class, stdout.getvalue())

    def test_update_error(self):
        """test method for do_update method errors"""
        cli = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("update"))
            self.assertEqual(TestConsole.missing_class, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd("update News"))
            self.assertEqual(TestConsole.no_class, stdout.getvalue())

    def test_empty(self):
        """test method for empty line"""
        cli = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(cli.onecmd(""))
            self.assertEqual("", stdout.getvalue())

    def test_help(self):
        """test method for help output"""
        cli = self.create()
        expected = "EOF  all  create  destroy  help  quit  show  update\n\n"
        self.assertFalse(cli.onecmd("help"))
        self.mock_stdout.flush.called
        self.assertEqual(expected, self._last_write(2))
        self.mock_stdout.reset_mock()

    def _last_write(self, nr=None):
        """:return: last `n` output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0],
                           self.mock_stdout.write.call_args_list[-nr:]))
