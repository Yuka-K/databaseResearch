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

    
    count = 0
    for i in range(len(myresult)-1):
      time.append([])
      so2.append([])
      trs.append([])
      if(myresult[i][3] == myresult[i+1][3] and myresult[i+1][3]):
        print(str(myresult[i][0]))
        time[count].append(str(myresult[i][0]))
        so2[count].append(myresult[i][1])
        trs[count].append(myresult[i][2])
      else: 
        time[count].append(str(myresult[i][0]))
        so2[count].append(myresult[i][1])
        trs[count].append(myresult[i][2])
        count += 1
        dates.append(myresult[i][3])
    time.append([])
    so2.append([])
    trs.append([])
    time[count].append(str(myresult[len(myresult)-1][0]))
    so2[count].append(myresult[len(myresult)-1][1])
    trs[count].append(myresult[len(myresult)-1][2])
    #for i in range(len(time)):
      #print(len(time[i]))

  
    tm = []
    s = []
    tr = []
    plt.clf()
    for i in range(len(time)):
      date_title = dates[i]
      for j in range(len(time[i])):
        fig, ax = plt.subplots()
        tm.append(time[i][j])
        s.append(so2[i][j])
        tr.append(trs[i][j])
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
      tm.clear()
      so2.clear()
      trs.clear()

