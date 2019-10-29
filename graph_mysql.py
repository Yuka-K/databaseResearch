import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(host='localhost',
                                user='root',
                                database='database_research')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    mycursor = cnx.cursor()

    mycursor.execute("SELECT * FROM teledyne_instrument")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)