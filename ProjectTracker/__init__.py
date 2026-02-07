import pymysql
pymysql.install_as_MySQLdb() #pymysql gamit kay way C++ Compiler.

#trick kay di mugana ako mysql
import MySQLdb
MySQLdb.version_info = (2, 2, 7, 'final', 0)
MySQLdb.__version__ = '2.2.7'