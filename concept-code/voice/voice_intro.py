import speech_recognition as sr
#import pyttsx3

def speech_capture():

    # Initialize the recognizer
    r = sr.Recognizer()
    r.energy_threshold = 400; #1000 works well in noisy room
    r.dynamic_energy_threshold = False

    # Loop infinitely for user to> 
    # speak

    while(1):

        # Exception handling to handle
        # exceptions at the runtime
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source2:
                
                print("listening...")
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                #listens for the user's input
                print("\n\nwill i hear anything?\n\n")
                audio2 = r.listen(source2, 5, 2)

                print("i must have heard something here!")
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print("information:", MyText)
                return MyText

        except:
            #print("returning nothing")
            return None