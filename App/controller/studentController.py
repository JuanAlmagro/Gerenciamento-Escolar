from App.config.database import Database
from App.model.studentModel import Student
 
class StudentController:
 
    @classmethod
    def validateRequiredFields(cls, data):
 
        required_fields = ['nome', 'CPF', 'data_nasc', 'RA', 'RM']
        for field in required_fields:
            if not data.get(field):
                print(f"Erro: O campo '{field}' é obrigatório e não pode estar vazio.")
                return False
        return True
 
    @classmethod
    def createStudent(cls, data: dict):
        try:
            if not cls.validateRequiredFields(data):
                return False
           
 
            student = Student(
                nome=data.get("nome"),
                nome_social=data.get("nome_social"),
                CPF=data.get("CPF"),
                data_nasc=data.get("data_nasc"),
                RA=data.get("RA"),
                RM=data.get("RM"),
                observacao=data.get("observacao")
            )
           
            novo_id = Student.Create(student)
            if novo_id:
                return novo_id
            return False
           
        except Exception as e:
            print(f"Erro no controller ao tentar criar aluno: {e}")
            return False
 
    @classmethod
    def updateStudent(cls, id: int, data: dict):
        try:
            if not cls.validateRequiredFields(data):
                return False
 
            student = Student(
                id=id,
                nome=data.get("nome"),
                nome_social=data.get("nome_social"),
                CPF=data.get("CPF"),
                data_nasc=data.get("data_nasc"),
                RA=data.get("RA"),
                RM=data.get("RM"),
                observacao=data.get("observacao"),
                status=data.get("status", True)
            )
 
            result = Student.Update(student)
            return result
           
        except Exception as e:
            print(f"Erro no controller ao atualizar os dados do aluno: {e}")
            return False
 
    @classmethod
    def deleteStudent(cls, id: int):
        try:
            return Student.delete(id)
        except Exception as e:
            print(f"Erro no controller ao desativar aluno: {e}")
            return False
 
    @classmethod
    def activateStudent(cls, id: int):
        try:
            return Student.activate(id)
        except Exception as e:
            print(f"Erro no controller ao ativar aluno: {e}")
            return False
 
    @classmethod
    def getStudentById(cls, id: int):
        try:
            return Student.findById(id)
        except Exception as e:
            print(f"Erro no controller ao buscar aluno por ID: {e}")
            return None
 
    @classmethod
    def getAllStudents(cls):
        try:
            return Student.findAll()
        except Exception as e:
            print(f"Erro no controller ao listar todos os alunos: {e}")
            return []
 
    @classmethod
    def getActiveStudents(cls):
        try:
            return Student.findActive()
        except Exception as e:
            print(f"Erro no controller ao listar alunos ativos: {e}")
            return []
 
if __name__ == "__main__":
 
    aluno_teste = {
        "nome": "João Silva",
        "nome_social": "",
        "CPF": "12345678901",
        "data_nasc": "2010-05-15",
        "RA": "123456",
        "RM": "654321",
        "observacao": "Aluno novo"
    }
 