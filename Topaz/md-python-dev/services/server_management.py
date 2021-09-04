from entities.server import Server


class ServerManagement:
    def __init__(self):
        self.quantity_used = 0
        self.all_ticks = 0
        self.servers = []

    def get_idle_server(self) -> Server:
        print('Pegando servidores ociosos')
        for server in self.servers:
            if server.current_users < server.user_max:
                return server

    def include_new_server(self, server: Server):
        self.servers.append(server)
        self.quantity_used = self.quantity_used + 1

    def increase_servers_time_alive(self):
        print('Adicionando tempo de vida aos servidores')
        for server in list(self.servers):
            server.increase_time_alive()
            if server.current_users == 0:
                print('Removendo servidor')
                self.all_ticks = self.all_ticks + server.time_alive
                self.servers.remove(server)

    def get_users_by_servers(self):
        users = []
        for server in self.servers:
            users.append(server.current_users)
        return str(users)
