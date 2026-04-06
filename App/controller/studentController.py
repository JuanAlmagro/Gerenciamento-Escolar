from App.model.studentModel import Student
from datetime import datetime
class StudentController:
 
    @classmethod
    def validateRequiredFields(cls, data):
 
        campos_necessarios = ['nome', 'CPF', 'data_nasc', 'RA', 'RM']
        for campo in campos_necessarios:
            if not data.get(campo):
                print(f"Erro: O campo '{campo}' é obrigatório e não pode estar vazio.")
                return False
        return True
 
    @classmethod
    def  create(cls, data: dict):
        try:
            data_nasc=data.get("data_nasc")
            data_nasc= datetime.strptime(data_nasc, "%d/%m/%Y")
            if not cls.validateRequiredFields(data):
                return False
           
 
            student = Student(
                nome=data.get("nome"),
                nome_social=data.get("nome_social"),
                CPF=data.get("CPF"),
                data_nasc=data_nasc,
                RA=data.get("RA"),
                RM=data.get("RM"),
                obs=data.get("observacao"),
            )
           
            novo_id = Student.Create(student)
            if novo_id:
                return novo_id
            return False
           
        except Exception as e:
            print(f"Erro no controller ao tentar criar aluno: {e}")
            return False
 
    @classmethod
    def update(cls, id: int, data: dict):
        try:

            data_nasc=data.get("data_nasc")
            data_nasc= datetime.strptime(data_nasc, "%d/%m/%Y")
            

        
            student = Student(
                id=id,
                nome=data.get("nome"),
                nome_social=data.get("nome_social"),
                CPF=data.get("CPF"),
                data_nasc=data_nasc,
                RA=data.get("RA"),
                RM=data.get("RM"),
                obs=data.get("observacao"),
                status=data.get("status", True)
            )
 
            result = Student.Update(student)
            return result
           
        except Exception as e:
            print(f"Erro ao atualizar os dados do aluno: {e}")
            return False
        
    @classmethod
    def upone (cls , stud:any):
        try:
            stud = Student.findById(stud["id"])
            if not stud:
                raise ValueError("studante não encontrado")

            

                          
            result = Student.Update(stud)
            return result
        except Exception as e:
            print(f'Não foi possivel atualizar o usuario \n{e}, {Student.showInfo(stud)}')

 
    @classmethod
    def delete(cls, id: int):
        try:
            return Student.delete(id)
        except Exception as e:
            print(f"Erro no controller ao desativar aluno: {e}")
            return False
 
    @classmethod
    def activate(cls, id: int):
        try:
            return Student.activate(id)
        except Exception as e:
            print(f"Erro ao ativar aluno: {e}")
            return False
 
    @classmethod
    def getById(cls, id: int):
        try:
            return Student.findById(id)
        except Exception as e:
            print(f"Erro ao buscar aluno por ID: {e}")
            return None
 
    @classmethod
    def getAll(cls):
        try:
            return Student.findAll()
        except Exception as e:
            print(f"Erro ao listar todos os alunos: {e}")
            return []
 
    @classmethod
    def getActive(cls):
        try:
            return Student.findActive()
        except Exception as e:
            print(f"Erro ao listar todos os alunos: {e}")
            return []
 
if __name__ == "__main__":
 
    user = {
        "id" : 1,
        "observacao": "TDAH",

    } 
    #StudentController.create(aluno_teste)
    StudentController.upone(user)

    
    
 
