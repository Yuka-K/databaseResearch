out = open('corrected_data_type.txt','w')
f = open('teledyne-Instrument-CONCENTRATIONS-08282019.txt','r')
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
        Y = '20' + date1[2]

        date2 = item[2].split('/')
        M = date2[0]
        D = date2[1]
        Y = '20' + date2[2]

        if len(M) == 1:
            M = '0' + M
        if len(D) == 1:
            D = '0' + D
        
        item[0] = Y + '-' + M + '-' + D
        item[2] = Y + '-' + M + '-' + D

    for i in range(len(item)):
        out.write(item[i] + ' ')
    out.write('\n')

out.close()
f.close()    
