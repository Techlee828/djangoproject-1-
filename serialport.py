import serial.tools.list_ports 
import csv
fileName = "sensordata.csv"

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList =[]

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("select Port : COM")

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x]) 

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        
        print(packet.decode('utf-8'))

while True: 
    time.sleep(.01)
    data = arduino.readline()
    saveFile.write(data)
    print (data)
## sensor data coming in, time too export this data into a csv file

filename="myFile.txt"
datafile=open(filename, 'a')

## this will store each line of data
seq = []
count = 1 ## row index

file = open(fileName, "w")

line = 0

while line <= samples:

        if print_label:
            if line==0:
                print("Printing Column headers")
            else:
                print("Line " + str(line) + " : writing...")   
        getData = str(ser.readline()) 
        data = getData[0:][:-2]
        print(data)

        file = open(filename, "a")

        file.write(data + "\n")

        line = line +1

