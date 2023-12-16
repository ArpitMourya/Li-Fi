
# Li-Fi Receiver


### Making a Receiver Circuit for Visible Optical communication ###

Li-Fi (Light Fidelity) is a high-speed, secure, and unidirectional data communication technology that utilizes visible light as the medium for transmitting information. Unlike traditional radio frequency (RF) communication, Li-Fi employs LEDs to modulate the intensity of light, encoding data that can be decoded by a photodetector-based receiver. This technology offers several advantages over RF communication, including:
-	**Immune to electromagnetic interference (EMI)**
-	**Secure and data cannot be intercepted by eavesdroppers**
-	**High data transmission rates**
-	**Safe for human use**
 ## Li-Fi Receiver Circuit Design ## 
The Li-Fi receiver circuit consists of several components that work together to decode the light-modulated data and convert it into a usable format:
![WhatsApp Image 2023-11-24 at 13 56 48_6dcf607f](https://github.com/ArpitMourya/Li-Fi/assets/99241859/15f012f2-1200-403e-8af1-67a9329bc31d)

1.	Photodetector: The photodetector, typically a Light Dependent Resistor, converts the incoming light into an electrical signal. The photodiode's current output varies in proportion to the intensity of the incident light
2.	Transistor Amplifier: The transistor amplifier boosts the weak current signal from the photodetector to a level that can be effectively processed by the subsequent stages.
3.	Comparator IC: The comparator IC compares the amplified signal from the transistor amplifier to a reference voltage, generating a digital output (either high or low) based on the comparison.
4.	FTDI (USB-to-Serial Converter): The FTDI (USB-to-serial converter) translates the digital output from the comparator IC into a serial data stream that can be read by a computer.
5.	Python Script: A Python script using the pyserial library receives the serial data from the FTDI and decodes it into the original data format.


## Component Details ##
-	Photodetector: LDR (1M ohm)
-	Transistor: BC178 (PNP transistor)
-	Comparator IC: LM339 (comparator)
-	FTDI: FT232RL (USB-to-TTL serial converter)
-	Python Script: Custom script using pyserial library

![circuit](https://github.com/ArpitMourya/Li-Fi/assets/99241859/4e1e96b6-e204-4a7b-89e4-5a088d299060)
## Measurement values: ##
- Vref - 2.22V
- Vamp	1.4V - 2.5V
## Code for serial communication

There are to python code
- [dark_mode_gui.py](https://github.com/ArpitMourya/Li-Fi/blob/main/dark_mode_gui.py) is the complete GUI application with multiple type of file transfer options like audio, image etc.
- [main.py](https://github.com/ArpitMourya/Li-Fi/blob/main/dark_mode_gui.py) is a basic testing program which can be used to send text only.
## Future Advansments ##
Currently this setput can achive heighest baudrate up to baud 40.
but for more advansments photodiode should be used this can go up to 4 MBp/s with same code.

    
## Authors

- [@Arpit Mourya ](https://github.com/ArpitMourya)
- [@Yashdeep Kumrawat ](https://github.com/YashdeepKum)

