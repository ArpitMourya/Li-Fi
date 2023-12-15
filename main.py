#port
#baudrate
#bytesize
#timeout
#stopbits
import time
import serial
import keyboard

ser = serial.Serial(port="COM3", baudrate=300, bytesize=8, timeout=1,
                    stopbits=serial.STOPBITS_ONE)
no = 0
while True:
    ser.write(f" Li-Fi no.{no}".encode('Ascii'))
    # ser.write(f"This is the message {no}\r\n".encode('Ascii'))
    receive = ser.read()
    receive = ser.readline()
    print(receive.decode('Ascii'))
    time.sleep(1)
    if keyboard.is_pressed('q'):
        print("User need to Quit the application")
        break
    no+=1
ser.close()






