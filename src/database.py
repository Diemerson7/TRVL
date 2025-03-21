import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("trvl.db")
    return conexao 

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''create table if not exists usuarios
                   (email text primary key,nome text,senha text)''')
    
    cursor.execute('''create table if not exists projetos_de_viagem
                   (id integer primary key,id_usuario text,destino text,data_prevista text,
                   status text,imagem text,gastos real,dinheiro_guardado real)''')
    
    conexao.commit()

def criar_usuario(email, nome, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute('insert into usuarios(email, nome, senha) VALUES (?, ?, ?)',
                       (email, nome, senha))
        
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
def deletar_usuario(email):
        
    conexao = conectar_banco()
    cursor = conexao.cursor()
       
    try:
        # PREENCHA AQUI - QUAL O COMANDO DELETAR UM USUÁRIO
        cursor.execute('DELETE FROM usuarios WHERE email = ?',
                       (email, ))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
       
def criar_projeto(id_usuario,destino,data_prevista,status,imagem,gastos,dinheiro_guardado):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('''INSERT INTO projetos_de_viagem(id_usuario,destino,data_prevista,
                       status,imagem,gastos,dinheiro_guardado) values (?, ?, ? , ?, ?, ?, ?)'''
                       ,(id_usuario,destino,data_prevista,status,imagem,gastos,dinheiro_guardado))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()  

def buscar_viagens(id_usuario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    # PREENCHA AQUI, BUSCAR TODAS AS VIAGENS ordem: destino, data_prevista, status, imagem
    cursor.execute('''SELECT destino, data_prevista, status, imagem FROM projetos_de_viagem
                   WHERE id_usuario = ?''', (id_usuario,))
    viagens = cursor.fetchall()
    conexao.close()

    return viagens

def apagar_viagem (id_viagem):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('DELETE FROM projetos_de_viagem WHERE id = ?', id_viagem)
        
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()

def mostrar_id_viagens (id_email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM projetos_de_viagem WHERE id_usuario = ?', (id_email,))
        conexao.commit()
        viagens = cursor.fetchall()
        return viagens
    
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
def trocar_nome (nome, email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('Update usuarios SET nome = ?  WHERE email = ?', (nome, email,))
        conexao.commit()
        viagens = cursor.fetchall()
        return viagens
    
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
        
def trocar_senha (senha, email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('Update usuarios SET senha = ?  WHERE email = ?', (senha, email,))
        conexao.commit()
        viagens = cursor.fetchall()
        return viagens
    
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
def editar_viagem (destino, data_prevista, status, imagem, gastos, dinheiro_guardado, id_usuario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('Update projetos_de_viagem SET data_prevista = ?  WHERE id_usuario = ?', (destino, data_prevista, status, imagem, gastos, dinheiro_guardado, id_usuario ))
        conexao.commit()
        viagens = cursor.fetchall()
        return viagens
    
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()     
        

if __name__ == '__main__': 
    conexao = conectar_banco()
    criar_tabelas()
    id_viagens = mostrar_id_viagens("charuri@email.com")
    print(id_viagens)

    # apagar_viagem("1")
    
    # apagar_usuario ("Diemerson","charuri@email.com")
    
    # mudar_senha ("1243", "charuri@email.com")
    
    # apagar_viagem ("25/12/25", "charuri@email.com")
    
    editar_viagem ("EUA", "10/10/2026", "Em andamento", "?", "1.000", "2.000", "Diemerson")
    
    
    
    
    


    

           
        
 

    

    

