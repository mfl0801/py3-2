# -* coding:utf8 *-
#print "hello world"
import pymysql
db = pymysql.connect("192.168.112.181","root","qwe123!","test")
sql = "SELECT * FROM test "
print sql