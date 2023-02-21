from bd import get_connection


def insert_data(textid, date, author, source, collection, language):
    conexion = get_connection()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO documents(text_id, date, author, source, collection, language) VALUES (%s, %s, %s, %s, %s, %s)",
                       (textid, date, author, source, collection, language))
    conexion.commit()
    conexion.close()


def delete_data(textid):
    connexion = get_connection()
    with connexion.cursor() as cursor:
        cursor.execute("DELETE FROM documents WHERE text_id = %s", textid)
    connexion.commit()
    connexion.close




# Proves
# insert_data('2', '2', 'bsc', 'web', 'col2', 'en')
# delete_data('1')