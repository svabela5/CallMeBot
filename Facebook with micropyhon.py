#follow the steps here https://www.callmebot.com/blog/free-api-facebook-messenger/ to see how to setup the API
import urequests

APIKEY = ''
initialise = False

def _parse_out(text):
    out = str(text)
    out = out.replace(' ','%20')
    out = out.replace(':','%3A')
    out = out.replace('/','%2F')
    out =  out.replace('\n','%0A')
    return out

def init(apikey):
    """This function needs to be run before running any other function. The only parameter that this function takes is the apikey which is given to you when you setup the api."""
    APIKEY = apikey
    initialise = True

def send_message(message):
    """THIS FUNCTION WILL NOT WORK UNLESS THE INTI FUNCTION HAS BEEN CALLED BEFORE. This is the function used to send messages. The message parameter is the parameter containing the message you want to send"""
    if not initialise:
        return
    url =  'https://api.callmebot.com/facebook/send.php?apikey=' + str(APIKEY) + '&text=' + str( _parse_out(message) )
    response = urequests.get( url )
    return (response.text)

