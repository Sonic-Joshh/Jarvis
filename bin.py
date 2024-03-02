# import mysql.connector
# from mysql.connector import errorcode
# from database import cursor

# DB_NAME = 'user_data_db'
# TABLES = {}

# TABLES['log'] = (
#     "  CREATE TABLE `logs` ("
#     " `id` int(11) NOT NULL AUTO_INCREMENT,"
#     " `user` varchar(250) NOT NULL,"
#     " `role` varchar(250) NOT NULL,"
#     " `parts` varchar(250) NOT NULL,"
#     " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
#     " PRIMARY KEY(`id`)"
#     ") ENGINE=InnoDB"
# )

# def create_db():
#     cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
#     print(f"created")

# def create_tables():
#     cursor.execute("USE {}".format(DB_NAME))

#     for table_name in TABLES:
#         table_description = TABLES[table_name]
#         try:
#             print(f"Creating table {table_name}", end=" ")
#             cursor.execute(table_description)
#         except mysql.connector.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print('already exists')
#             else:
#                 print(err.msg)

# create_db() 
# create_tables()

import database as db
db.delete_logs('admin')

