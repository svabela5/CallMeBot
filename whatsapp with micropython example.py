#copy the contents of this file https://github.com/svabela5/CallMeBot/blob/main/Whatsapp%20with%20micropython into a blank file.
#Name that file 'whatsapp.py' and upload it to your device
#This example is for the raspberry pi pico w
#ensure that the board is connected to the internet
import whatsapp

whatsapp.init("INSERT PHONE HERE","INSERT APIKEY HERE")
whatsapp.send_message("YOUR MESSAGE HERE")