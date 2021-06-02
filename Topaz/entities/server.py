import uuid

from entities.task import Task


class Server:
    def __init__(self, umax: int):
        self.id = uuid.uuid1()
        self.user_max = umax
        self.current_users = 0
        self.time_alive = 0
        self.tasks_executed = 0
        self.tasks = []

    def __eq__(self, other):
        if isinstance(other, Server):
            return self.id == other.id
        return False

    def connect_user(self):
        print('Conectando usuário')
        self.current_users = self.current_users + 1

    def disconnect_user(self):
        print('Desconectando usuário')
        self.current_users = self.current_users - 1

    def increase_time_alive(self):
        print(f'Adicionando tempo de vida ao servidor {self.id}')
        self.time_alive = self.time_alive + 1
        for task in list(self.tasks):
            task.decrease_duration()
            if task.duration == 0:
                print('Removendo tarefa')
                self.tasks.remove(task)
                self.tasks_executed = self.tasks_executed + 1
                self.disconnect_user()

    def include_new_task(self, task: Task):
        print('Adicionando nova tarefa')
        self.tasks.append(task)
