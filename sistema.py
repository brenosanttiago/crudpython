from PyQt5 import uic, QtWidgets
import mysql.connector


app = QtWidgets.QApplication([])

suc = uic.loadUi("sucesso.ui")
lis = uic.loadUi("lista.ui")
f = uic.loadUi("cadastro.ui")
f.show()

conexao = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = '',
database = 'db_voluntario'
)


def limpar():
    f.le_nome.setText("")
    f.le_idade.setText("")
    f.le_telefone.setText("")
    

def cadastrar():
    nome = f.le_nome.text()
    idade = f.le_idade.text()
    telefone = f.le_telefone.text()
    sexo = ''

    if f.rb_masculino.isChecked():
        sexo = 'Masculino'
    elif f.rb_feminino.isChecked():
        sexo = 'Feminino'
    
    turno = f.cb_selecionar.currentText()

    cursor = conexao.cursor()
    sql = "insert into tb_voluntario (nome, idade, telefone, sexo, turno) values (%s, %s, %s, %s, %s)"
    entrada = (str(nome),str(idade),str(telefone), str(sexo), str(turno))
    cursor.execute(sql, entrada)
    conexao.commit()
    limpar()
    
    suc.show()


def listar():
    lis.show()
    lis.list_nome.clear()
    lis.list_idade.clear()
    lis.list_telefone.clear()

    cursor = conexao.cursor()
    sql = "select * from tb_voluntario"
    cursor.execute(sql)
    registros = cursor.fetchall()
    for linha in registros:
        lis.list_nome.addItem(str(linha[1]))
        lis.list_idade.addItem(str(linha[2]))
        lis.list_telefone.addItem(str(linha[3]))
        lis.list_sexo.addItem(str(linha[4]))
        lis.list_turno.addItem(str(linha[5]))
    conexao.commit()

        
    
f.pb_cadastrar.clicked.connect(cadastrar)
f.pb_limpar.clicked.connect(limpar)
f.pb_ver.clicked.connect(listar)



app.exec()
