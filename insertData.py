import mysql.connector
from mysql.connector import errorcode
from os import listdir, sep, remove
from shutil import rmtree
from os.path import isfile, join
from glob import glob
 
def convert():
        files = glob("data/**/*.txt")
        #files = [f for f in listdir("data") if isfile(join("data", f))]
        for file in files:
            arr = []
            f = open(file,'r+')
            print(file)   
            #out = open("data/out/" + str(count) + file,'w')
            while True:
                line = f.readline()
                if line == '':
                    break
                line = line.strip()
                item = line.split()
                if (item[0] == 'Date'):
                    pass
                elif (item[2] == 'AM,' or item[2] == 'PM,'):
                    
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
                    if (item[2] == 'PM,'):
                        temp = item[1].split(":")
                        hour = int(temp[0])
                        minute = temp[1]
                        sec = temp[2]
                        if(hour != 12):
                            hour = hour + 12
                        item[1] = str(hour) + ':' + minute + ":" + sec

                    if (item[5] == 'PM,'):
                        temp = item[4].split(":")
                        hour = int(temp[0])
                        minute = temp[1]
                        sec = temp[2]
                        if(hour != 12):
                            hour = hour + 12
                        item[4] = str(hour) + ':' + minute + ":" + sec
                    if (item[2] == 'AM,'):
                        temp = item[1].split(":")
                        hour = int(temp[0])
                        minute = temp[1]
                        sec = temp[2]
                        if(hour == 12):
                            hour = hour + 12
                        item[1] = str(hour) + ':' + minute + ":" + sec
                    if (item[5] == 'AM,'):
                        temp = item[4].split(":")
                        hour = int(temp[0])
                        minute = temp[1]
                        sec = temp[2]
                        if(hour == 12):
                            hour = hour + 12
                        item[4] = str(hour) + ':' + minute + ":" + sec
                    item.pop(2)
                    item.pop(4)

                else:
                    date1 = item[0].split('/')
                    M = date1[0]
                    D = date1[1]
                    Y = date1[2]

                    date2 = item[2].split('/')
                    M = date2[0]
                    D = date2[1]
                    Y = date2[2]

                    if len(M) == 1:
                        M = '0' + M
                    if len(D) == 1:
                        D = '0' + D
                    
                    item[0] = Y + '-' + M + '-' + D
                    item[2] = Y + '-' + M + '-' + D

                if(item[0] == 'Date'):
                    pass
                else: 
                    for i in range(len(item)):
                        if("," in item[i]):
                            item[i] = item[i].replace(",", "")

                    str1 = ' '.join([str(elem) for elem in item])
                    arr.append(str1)
            #for i in arr:
               # print(i)
            f.seek(0)
            for i in arr:
                f.write(i)
                f.write('\n')
            f.truncate()
                
                       
            f.close() 
            #out.close()   


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
        files = glob("data/**/*.txt")
        for file in files:
            newPath = file.replace(sep, '/')
            query = "LOAD DATA INFILE 'C:/Users/kuuch/OneDrive/ドキュメント/GitHub/databaseResearch/%s' INTO TABLE teledyne_instrument FIELDS TERMINATED BY ' '  LINES TERMINATED BY '\n' IGNORE 1 LINES;" % (newPath,)
            mycursor = cnx.cursor()

            mycursor.execute(query)
            cnx.commit()   
            remove(file)

def main():
    convert()
    insert()
    rmtree("data/*/", ignore_errors=True)

main()
 
 