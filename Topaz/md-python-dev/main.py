from entities.server import Server
from entities.task import Task
from services.server_management import ServerManagement
from utils.data_interface import DataReader


def run_by_user_income():
    for user in range(ticks[tick]):
        is_new_server = False
        server = server_management.get_idle_server()
        if not server:
            print('Criando novo server')
            server = Server(umax=umax)
            is_new_server = True
        if not ticks[tick]:
            print('Sem usuários novos')
            continue
        server.connect_user()
        server.include_new_task(task=Task(initial_tick=tick, duration=ttask))
        if is_new_server:
            server_management.include_new_server(server=server)


if __name__ == "__main__":
    try:
        print('Iniciando balanceamento')
        data_reader = DataReader()
        data = data_reader.read_file('input.txt')
        output_file_name = 'output.txt'
        ttask = data[0]
        umax = data[1]
        ticks = data[2:]
        server_management = ServerManagement()
        for tick in range(0, len(ticks)):
            print(f'Tick {tick} | Quantidade de usuários {ticks[tick]}')
            server_management.increase_servers_time_alive()
            run_by_user_income()
            data_reader.append_to_write(line=server_management.get_users_by_servers())
        print('Terminando processamento')
        while server_management.servers:
            server_management.increase_servers_time_alive()
            data_reader.append_to_write(line=server_management.get_users_by_servers())
        print(f'Gasto {server_management.all_ticks}')
        data_reader.append_to_write(line=server_management.all_ticks)
        data_reader.write_file_line(file_name=output_file_name)
    except Exception as error:
        print(f'Problema não mapeado. Detalhes: {error}')
