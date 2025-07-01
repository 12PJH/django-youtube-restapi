from django.test import SimpleTestCase
from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OperationalError

class CommandTests(SimpleTestCase):

    @patch('django.db.utils.ConnectionHandler.__getitem__')
    def test_wait_for_db_ready(self, patched_getitem):
        patched_getitem.return_value = True

        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 1)

    @patch('time.sleep')
    @patch('django.db.utils.ConnectionHandler.__getitem__')
    def test_wait_for_db_delay(self, patched_getitem, patched_sleep):
        patched_getitem.side_effect = [Psycopg2OperationalError(),  # 인스턴스로 변경
                *[OperationalError() for _ in range(5)], True]

        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 7)