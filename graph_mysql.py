import mysql.connector
from mysql.connector import errorcode
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


time = []
so2 = []
trs = []
dates = []



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
    mycursor.execute("SELECT UTCTIME, SO2_PPB, TRS_PPB, DATE1 FROM teledyne_instrument limit 2000")
    myresult = mycursor.fetchall()

    for i in range(len(myresult)):
      if(str(myresult[i][3]) == str(myresult[i+1][3])):
        time.append(str(myresult[i][0]))
        so2.append(myresult[i][1])
        trs.append(myresult[i][2])
      else: 
        date_title = myresult[i][3]
        plt.plot(tm,s, label='SO2 PPB')
        plt.plot(tm,tr, label='TRS PPB') 
        for index, label in enumerate(ax.xaxis.get_ticklabels()):
            if index % 50 != 0:
                label.set_visible(False)
        plt.xticks(tm, tm, rotation='vertical')
        plt.xlabel('Time')
        plt.ylabel('PPB')
        plt.title(date_title)
        plt.savefig("images/" + str(date_title) + ".png")
        plt.legend()
        plt.clf()
        fig, ax = plt.subplots()       
        time.clear()
        so2.clear()
        trs.clear()
        



