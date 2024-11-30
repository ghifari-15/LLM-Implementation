import mysql.connector as sql


# Fungsi untuk koneksi ke database
def connect_database():
    conn = sql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="chatbot"
    )
    return conn
    

def initialize_database():
    conn = connect_database()
    cursor = conn.cursor()
    query = '''
    create table if not exist chatbot
    id int auto_increment primary key not null,
    sender varchar(255) not null,
    data text not null,
    date_submitted datetime default current_timestamp not null
    );
'''
    cursor.execute(query)
    conn.commit()
    conn.close()



# Fungsi untuk membuat tabel jika belum ada
def initialize_database():
    """Membuat tabel jika belum ada."""
    conn = connect_database()
    cursor = conn.cursor()
    conn.commit()
    conn.close()


# Fungsi untuk menyimpan pesan ke dalam database
def save_data(sender, data):
    """Menyimpan data ke tabel chatbot."""
    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO chat_record (sender, data)
            VALUES (%s, %s)
        ''', (sender, data))
        conn.commit()
    except sql.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()  # Pastikan koneksi selalu ditutup
