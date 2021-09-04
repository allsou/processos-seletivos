import unittest

from entities.server import Server

UMAX_STANDARD = 1


class ServerTest(unittest.TestCase):

    def test_connect_user_successfully(self):
        server = Server(umax=UMAX_STANDARD)
        server.connect_user()
        self.assertEqual(server.current_users, 1)

    def test_disconnect_user_successfully(self):
        server = Server(umax=UMAX_STANDARD)
        server.disconnect_user()
        self.assertEqual(server.current_users, -1)

    def test_increase_time_alive_successfully(self):
        server = Server(umax=UMAX_STANDARD)
        server.increase_time_alive()
        self.assertEqual(server.time_alive, 1)
        self.assertEqual(server.tasks, [])

