import uuid


class Task:
    def __init__(self, initial_tick: int, duration: int):
        self.id = uuid.uuid1()
        self.__initial_tick = initial_tick
        self.duration = duration

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.id == other.id
        return False

    def decrease_duration(self):
        print('Diminuindo duração de task')
        self.duration = self.duration - 1
