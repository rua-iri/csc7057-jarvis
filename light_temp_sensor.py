import time
import serial
from gpiozero import LED, Motor


try:
    #open the configuration file and store data to variables
    with open("./config/voiceconfig.csv", "r") as config_file:
        config_data = config_file.readline().split(",")
        temp_lmt = float(config_data[4])

        #light_lmt must be multiplied by 10
        light_lmt = int(config_data[5]) * 10

except:
    #set variables to default values if there is an error
    temp_lmt = 25.0
    light_lmt = 100



#setup connection with arduino
try:
    ard_ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
except:
    print("Error: Arduino not connected to /dev/ttyACM0")


#the group of yellow LEDs
bright_led = LED(26)

#instantiate the motor
mtr = Motor(20, 21, 16)

def read_sensors():
    ard_ser.reset_input_buffer()

    while True:

        #read a line from the serial connection
        serial_data = ard_ser.readline().decode("ascii").rstrip().split(",")

        #check that both values have been read correctly
        while len(serial_data)<2:
            serial_data = ard_ser.readline().decode("ascii").rstrip().split(",")

        #extract the two variables
        temp, light = serial_data
        #convert each value from string to numerical value
        temp = float(temp)
        light = int(light)

        #determine the behaviour of the light and fan based on these values
        if temp > temp_lmt:
            mtr.value = 0.4
        else:
            mtr.value = 0

        #turn on led if light level is below limit
        if light < light_lmt:
            bright_led.on()
        else:
            bright_led.off()

        #reset the input buffer from the arduino
        ard_ser.reset_input_buffer()

        time.sleep(0.1)
