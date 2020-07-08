from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):
    """ Mocking is a great technique in software engineering that make it easy
        to clone behaviour of for example db calls that takes time or that could fail
        and it allows us to minimize tests time in the automation tests and also eliminate uncertainty of a systems.
    """
    pass

    def test_wait_for_db_ready(self):
        """ Test Waiting for db to be available """
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:  # mock the connection
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """ Test Waiting for db """
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:  # mock the connection
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
