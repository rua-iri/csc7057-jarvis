from number_parser import parse as n_parser
from gpiozero import TonalBuzzer, Button
from time import sleep as timer_sleep

#initialise the buzzer
buzzr = TonalBuzzer(19)
btn = Button(13)



#function to check that the input is valid
def check_timer_valid(timer_string):

    #list containing information to be returned about how long to run the timer
    timer_lst = [False, 0]

    #parse input for numbers and split data on each space
    timer_data = n_parser(timer_string).split(" ")

    #check that data is the correct length (2 or 4 elements)
    if len(timer_data)==2:
        #check that the number parsed is a valid integer
        try:
            timer_number = int(timer_data[0])
        except:
            return timer_lst

        #multiply timer_number by 60 if second word is minute
        if timer_data[1][0]=="m":
            timer_number *= 60

        timer_lst[0] = True
        timer_lst[1] = timer_number

    #if input has minutes and seconds
    elif len(timer_data)==4:
        try:
            #calculate total time in seconds
            timer_number = (int(timer_data[0])*60) + int(timer_data[2])
        except:
            return timer_lst

        timer_lst[0] = True
        timer_lst[1] = timer_number


    return timer_lst




#function to play an error tone if input is invalid
def play_error_tone():
    buzzr.play(220)
    timer_sleep(2)
    buzzr.stop()




#function to extract the length of time to set the timer for
def new_timer(timer_length):
    play_buzz = True

    #sleep for length of time
    timer_sleep(timer_length)

    #buzzer plays sound until button is pressed
    while play_buzz:
        #alternate between low and high frequencies
        buzzr.play(400)
        timer_sleep(0.5)
        buzzr.play(500)
        timer_sleep(0.5)

        if btn.is_pressed:
            play_buzz = False

    #turn off buzzer once loop has finished
    buzzr.stop()
