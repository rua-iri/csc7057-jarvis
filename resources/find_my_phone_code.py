from twilio.rest import Client

def call_phone():

    #authentication credentials for twilio
    acc_id = #account id here
    ath_key = #authentication key here

    #set up client
    client = Client(acc_id, ath_key)

    #call user's phone via twilio
    call = client.calls.create(
        twiml="<Response><Say>Phone has been found!</Say></Response>",
        to=#user's phone number here,
        from_=#account phone number here
    )





import find_my_phone









    elif "call me" in text:
    	jarvis_speak("Calling mobile phone")
    	find_my_phone.call_phone()








