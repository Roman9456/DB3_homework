# Client Database Management

## English

### Description
This project is a part of a client database management system. It includes functions to create and manage a PostgreSQL database, including creating tables, adding new clients, adding phone numbers for existing clients, updating client information, and deleting phone numbers and clients.

### Features
- create_database(): Creates a new database named 'clients' if it doesn't already exist.
- create_tables(): Creates two tables: 'clients' and 'phones'. The 'phones' table has a foreign key relationship with the 'clients' table.
- add_client(first_name, last_name, email): Adds a new client to the 'clients' table.
- add_phone(client_id, phone_number): Adds a phone number for an existing client in the 'phones' table.
- update_client(client_id, first_name=None, last_name=None, email=None): Updates the information for an existing client in the 'clients' table.
- delete_phones(client_id): Deletes all phone numbers for an existing client in the 'phones' table.
- delete_client(client_id): Deletes a client from the 'clients' table and all associated phone numbers from the 'phones' table.

### Usage
1. Configure the database_config dictionary with your PostgreSQL connection details.
2. Call the create_database() function to create the 'clients' database if it doesn't already exist.
3. Call the create_tables() function to create the 'clients' and 'phones' tables.
4. Use the provided functions to manage clients and their phone numbers.

## Russian

### Описание
Этот проект является частью системы управления базой данных клиентов. Он включает в себя функции для создания и управления базой данных PostgreSQL, в том числе для создания таблиц, добавления новых клиентов, добавления номеров телефонов для существующих клиентов, обновления информации о клиентах и удаления номеров телефонов и клиентов.

### Возможности
- create_database(): Создает новую базу данных с именем 'clients', если она еще не существует.
- create_tables(): Создает две таблицы: 'clients' и 'phones'. Таблица 'phones' имеет связь внешнего ключа с таблицей 'clients'.
- add_client(first_name, last_name, email): Добавляет нового клиента в таблицу 'clients'.
- add_phone(client_id, phone_number): Добавляет номер телефона для существующего клиента в таблицу 'phones'.
- update_client(client_id, first_name=None, last_name=None, email=None): Обновляет информацию для существующего клиента в таблице 'clients'.
- delete_phones(client_id): Удаляет все номера телефонов для существующего клиента в таблице 'phones'.
- delete_client(client_id): Удаляет клиента из таблицы 'clients' и все связанные номера телефонов из таблицы 'phones'.

### Использование
1. Настройте словарь database_config со своими параметрами подключения к PostgreSQL.
2. Вызовите функцию create_database(), чтобы создать базу данных 'clients', если она еще не существует.
3. Вызовите функцию create_tables(), чтобы создать таблицы 'clients' и 'phones'.
4. Используйте предоставленные функции для управления клиентами и их номерами телефонов.
