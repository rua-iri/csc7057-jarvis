from gpiozero import LED
import time

#store each led in a list
led_list = [LED(4), LED(17), LED(27), LED(22), LED(10)]

led_loop = True



def led_sequence():
    global led_loop
    #start the counter at 0
    led_cntr = 0
    #True means that leds light up in ascending order
    led_direction = True

    while led_loop:
        if led_direction:
            if led_cntr>0:
                led_list[led_cntr-1].off()

            #turn on the current led in the list
            led_list[led_cntr].on()
            #change direction if last led is lit up
            if led_cntr==len(led_list)-1:
                led_direction = False
                led_cntr -= 1
            else:
                led_cntr += 1

        else:
            if led_cntr<len(led_list)-1:
                led_list[led_cntr+1].off()

            #turn on the current led in the list
            led_list[led_cntr].on()
            #change direction if first led is lit up
            if led_cntr==0:
                led_direction = True
                led_cntr += 1
            else:
                led_cntr -= 1

        time.sleep(0.25)

    led_loop = True
    #check that all leds are off
    for led in led_list:
        led.off()
