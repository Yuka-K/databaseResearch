#!/usr/bin/python

import matplotlib

fp = open("teledyne-Instrument-CONCENTRATIONS-08282019.txt", "r")

x = []
y = []
fp.readline()
while True:
    line = fp.readline()
    if line == "":
        break
    line = line.strip()
    word = line.split()

    x = str(word[3])
    y = float(word[7])
    
    for i in x:
        (h, m, s) = i.split(':')
        x[i] = int(h) * 3600 + int(m) * 60 + int(s)

    plt.plot(x,y)
    plt.show()

fp.close()



