import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import subprocess
from time import sleep as lcd_sleep



lcd_columns = 16
lcd_rows = 2

# Pin Configuration to connect the GPIO pins to the lcd screen:
lcd_rs = lcd_rs = digitalio.DigitalInOut(board.D7)
lcd_en = digitalio.DigitalInOut(board.D8)
lcd_d7 = digitalio.DigitalInOut(board.D18)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

def write_new_message(lcd_text):
    lcd.clear()
    lcd.message = lcd_text



#function to clear the screen
def clear_screen():
    lcd.clear()


#function for displaying the ip address on the screen
def display_ip():
    lcd.clear()

    #determine the ip address using a bash command
    ip_list = subprocess.check_output(["ip", "add"]).decode()
    start_ip = ip_list.find("inet 192") + 5
    end_ip = ip_list.find("/24")
    ip_address = ip_list[start_ip:end_ip]
    write_new_message(ip_address)
    lcd_sleep(20)
    lcd.clear()

