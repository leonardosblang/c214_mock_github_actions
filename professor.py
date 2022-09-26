import json

class Professor:
    def __init__(self, nome_do_professor, periodo, horario_de_atendimento):
        self.nome_do_professor = nome_do_professor
        self.periodo = periodo
        self.horario_de_atendimento = horario_de_atendimento


    def recebe_json(self, json_file):
        with open(json_file) as f:
            data = json.load(f)
            self.periodo = data['periodo']
            self.horario_de_atendimento = data['horario_De_Atendimento']
            self.nome_do_professor = data['nome_Do_Professor']
        return data

    def change_horario_de_atendimento(self, new_hours):
        self.horario_de_atendimento = new_hours

    def change_periodo(self, new_periodo):
        self.periodo = new_periodo

    def salario(self):
        return self.horario_de_atendimento * 100

    
print("isso é um arquivo.exe")
