import configparser
# import mysql.connector
# from mysql.connector import Error


def Config():
    config = configparser.ConfigParser()
    config.read('utilities/config.ini')
    return config


# def getPassword():
#     return '111'
#
#
#
#
# # To pass the payload using database
# connect_config = {
#     'user': getConfig()['SQL']['user'],
#     'password': getConfig()['SQL']['password'],
#     'host': getConfig()['SQL']['host'],
#     'database': getConfig()['SQL']['database']
# }
#
#
# def getConnection():
#     try:
#         conn = mysql.connector.connect(**connect_config)
#         if conn.is_connected():
#             print("Connection Successful")
#             return conn  # returning conn object
#     except Error as e:
#         print(e)
#
#
# def getQuery(query):
#     conn = getConnection()
#     cursor = conn.cursor()
#     cursor.execute(query)
#     row = cursor.fetchone()
#     conn.close()
#     return row
