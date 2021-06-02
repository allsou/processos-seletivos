import unittest

from entities.server import Server
from services.server_management import ServerManagement

UMAX_STANDARD = 1


class ServerManagementTest(unittest.TestCase):

    def test_get_idle_server_successfully(self):
        management = ServerManagement()
        server = Server(umax=UMAX_STANDARD)
        management.include_new_server(server=server)
        idle_server = management.get_idle_server()
        self.assertEqual(server, idle_server)

    def test_get_idle_server_failure_return_none(self):
        management = ServerManagement()
        self.assertIsNone(management.get_idle_server())

    def test_include_new_server_successfully(self):
        management = ServerManagement()
        server = Server(umax=UMAX_STANDARD)
        management.include_new_server(server)
        self.assertEqual(len(management.servers), 1)

    def test_increase_servers_time_alive_successfully(self):
        management = ServerManagement()
        server = Server(umax=UMAX_STANDARD)
        management.include_new_server(server)
        management.increase_servers_time_alive()
        self.assertEqual(management.all_ticks, 1)
        self.assertEqual(len(management.servers), 0)

    def test_get_users_by_servers_successfully(self):
        management = ServerManagement()
        server = Server(umax=UMAX_STANDARD)
        management.include_new_server(server)
        self.assertEqual(management.get_users_by_servers(), '[0]')
