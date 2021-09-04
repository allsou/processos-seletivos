class DataReader:
    def __init__(self):
        self.lines = []

    @staticmethod
    def read_file(file_name: str) -> list:
        print(f'Lendo arquivo {file_name}')
        try:
            with open(f'data_source/{file_name}') as file:
                file_set = [int(line) for line in file.readlines()]
                file.close()
            return file_set
        except Exception as error:
            print(f'Problemas ao realizar leitura: {error}')

    def append_to_write(self, line: str):
        line = str(line).replace("[", "")
        line = str(line).replace("]", "")
        line = str(line).replace(" ", "")
        self.lines.append(line)

    def write_file_line(self, file_name: str):
        print(f'Escrevendo arquivo {file_name}')
        creating_file = open(f'data_source/{file_name}', 'w')
        creating_file.close()
        with open(f'data_source/{file_name}', 'a') as file:
            line_amount = len(self.lines)
            for index in range(line_amount):
                line = self.lines[index]
                if not line:
                    line = 0
                if line_amount - 1 == index:
                    file.write(line)
                    break
                file.write(f'{line}\n')
        file.close()
