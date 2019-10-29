import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('corrected_data_type.txt','r') as f:
    line = f.readline()
    for count in range(10):
        line = f.readline()
        line = line.strip()
        item = line.split()
        x.append(item[1])
        y.append(item[7])

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()


   # line = f.readlines()
    #x = [line.split()[1] for line in lines]
   # y = [line.split()[7] for line in lines]