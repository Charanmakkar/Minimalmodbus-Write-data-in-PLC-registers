import minimalmodbus as mm, serial, time

#Fuction to start communication
def setParameters(x,y,z):
    try:
        instrument = mm.Instrument(x , 1 , debug = False)
        instrument.serial.baudrate = y
        instrument.address = z
        instrument.serial.bytesize = 7
        instrument.serial.timeout  = 1
        instrument.serial.parity   = serial.PARITY_EVEN
        instrument.mode = mm.MODE_ASCII
        print(instrument)
        return instrument
    except:
        print("Device NOT coneected")

#function to write a bit (Discrete Inputs)
def writeBit(a,b):
    try:
        #Main functio to write value at a register
        data = instrument.write_bit(a,b)
        print(str(data))
        return data
    except IOError:
        print("Failed to read from instrument")

#calling a function to connect my laptop/raspberry Pi/PC etc with PLC
instrument = setParameters('COM3', 9600, 1)
#As communication gets successfull, ALL PARAMETER of connections are printed

#Calling function to write a value on a register
writeBit(2349, 1)
