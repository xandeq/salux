import psycopg2
from psycopg2.extras import execute_batch

def registrar_eventos(eventos):
    conexao_bd = "dbname=test user=postgres password=secret"
    
    with psycopg2.connect(conexao_bd) as conexao:
        with conexao.cursor() as cursor:
            comando = "INSERT INTO logs (timestamp, level, message) VALUES (%s, %s, %s)"
            dados = [(evento['timestamp'], evento['level'], evento['message']) for evento in eventos]
            execute_batch(cursor, comando, dados)
