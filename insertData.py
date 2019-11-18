import mysql.connector
from mysql.connector import errorcode
from os import listdir
from os.path import isfile, join

 
def insert():
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
        files = [f for f in listdir("data") if isfile(join("data", f))]
        count = 0
        print(files)
        for file in files:
            count += 1
            f = open("data/" + file,'r')
            out = open("data/out/" + str(count) + file,'w')
            while True:
                line = f.readline()
                if line == '':
                    break
                line = line.strip()
                item = line.split()
                if (item[0] == 'Date'):
                    pass
                else:
                    date1 = item[0].split('/')
                    M = date1[0]
                    D = date1[1]
                    Y =  date1[2]

                    date2 = item[3].split('/')
                    M = date2[0]
                    D = date2[1]
                    Y = date2[2]

                    if len(M) == 1:
                        M = '0' + M
                    if len(D) == 1:
                        D = '0' + D
                    
                    item[0] = Y + '-' + M + '-' + D
                    item[3] = Y + '-' + M + '-' + D

                
                    for i in range(len(item)):
                        if i == 2 or i == 5:
                            pass
                        else:
                            out.write(item[i] + ' ')
                    out.write('\n')

            #print(file)
        files = [f for f in listdir("data/out") if isfile(join("data/out", f))]
        for file in files:
            query = "LOAD DATA INFILE 'C:/Users/kuuch/OneDrive/ドキュメント/GitHub/databaseResearch/data/out/%s' INTO TABLE teledyne_instrument FIELDS TERMINATED BY ' '  LINES TERMINATED BY '\n' IGNORE 1 LINES;" % (file,)
            mycursor = cnx.cursor()
            mycursor.execute(query)
            cnx.commit()


            f.close() 
            out.close()   





def main():
    insert()

main()
