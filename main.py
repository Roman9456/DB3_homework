import psycopg2

# Database configuration
database_config = {
    'host': 'localhost',#Or your personal host
    'database': 'clients',
    'user': '',#your user name for work with DB
    'password': '' #your password for work with DB
}

# Create DB func
def create_database():
    conn = psycopg2.connect(**database_config)
    conn.autocommit = True
    c = conn.cursor()
    c.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'clients'")
    database_exists = c.fetchone()
    if not database_exists:
        c.execute("CREATE DATABASE clients")
        print("База данных 'clients' успешно создана.")
    else:
        print("База данных 'clients' уже существует.")
    conn.close()

# Create tables func
def create_tables():
    conn = psycopg2.connect(**database_config)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clients
                 (id SERIAL PRIMARY KEY,
                 first_name TEXT,
                 last_name TEXT,
                 email TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS phones
                 (id SERIAL PRIMARY KEY,
                 client_id INTEGER REFERENCES clients(id) ON DELETE CASCADE,
                 phone_number TEXT)''')
    conn.commit()
    conn.close()
    print("Таблицы успешно созданы.")

# Add new client func
def add_client(first_name, last_name, email):
    conn = psycopg2.connect(**database_config)
    c = conn.cursor()
    c.execute("INSERT INTO clients (first_name, last_name, email) VALUES (%s, %s, %s)",
              (first_name, last_name, email))
    conn.commit()
    conn.close()
    print("Клиент успешно добавлен.")

# Add phone number for existing client func
def add_phone(client_id, phone_number):
    conn = psycopg2.connect(**database_config)
    c = conn.cursor()
    # Check if client exists
    c.execute("SELECT * FROM clients WHERE id=%s", (client_id,))
    client = c.fetchone()
    if client:
        c.execute("INSERT INTO phones (client_id, phone_number) VALUES (%s, %s)",
                  (client_id, phone_number))
        conn.commit()
        print("Телефон успешно добавлен для клиента.")
    else:
        print("Клиент с указанным ID не существует.")
    conn.close()

# Change data of client func
def update_client(client_id, first_name=None, last_name=None, email=None):
    conn = psycopg2.connect(**database_config)
    c = conn.cursor()
    if first_name:
        c.execute("UPDATE clients SET first_name=%s WHERE id=%s", (first_name, client_id))
    if last_name:
        c.execute("UPDATE clients SET last_name=%s WHERE id=%s", (last_name, client_id))
    if email:
        c.execute("UPDATE clients SET email=%s WHERE id=%s", (email, client_id))
    conn.commit()
    conn.close()
    print("Данные клиента успешно обновлены.")

# Delete phone numbers for existing client func
def delete_phones(client_id):
    conn = psycopg2.connect(**database_config)
    c = conn.cursor()
    c.execute("DELETE FROM phones WHERE client_id=%s", (client_id,))
    conn.commit()
    conn.close()
    print("Телефоны успешно удалены для клиента.")

# Delete client func
def delete_client(client_id):
    conn = psycopg2.connect(**database_config)
    c = conn.cursor()
    delete_phones(client_id)
    c.execute("DELETE FROM clients WHERE id=%s", (client_id,))
    conn.commit()
    conn.close()
    print("Клиент успешно удален.")

# Searching func (Name, phone, email)
def find_clients(search_term):
    conn = psycopg2.connect(**database_config)
    c = conn.cursor()
    c.execute("SELECT * FROM clients WHERE first_name=%s OR last_name=%s OR email=%s",
              (search_term, search_term, search_term))
    result = c.fetchall()
    if result:
        for row in result:
            print("ID:", row[0])
            print("Имя:", row[1])
            print("Фамилия:", row[2])
            print("Email:", row[3])
            print("Телефоны:")
            c.execute("SELECT * FROM phones WHERE client_id=%s", (row[0],))
            phones = c.fetchall()
            if phones:
                for phone in phones:
                    print(phone[2])
            else:
                print("Нет телефонов.")
            print("----------")
    else:
        print("Клиенты не найдены.")
    conn.close()

# Create a database (if it doesn't exist)
create_database()

# Creating a database structure (tables)
create_tables()

# An example of using functions
add_client("Иван", "Иванов", "ivan@example.com")
add_client("Петр", "Петров", "petr@example.com")

add_phone(1, "+123456789")
add_phone(1, "+987654321")

update_client(1, last_name="Сидоров")

find_clients("Иван")
