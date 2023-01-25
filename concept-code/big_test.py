from voice_intro import speech_capture

commands = ["sit", "roll", "over", "come", "fetch"]



while True:
    information = speech_capture()
    if information is not None:
        phrase = information.split(" ")

        for word in phrase:
            if word in commands:
                print(f"Interpreting {word} as a command!")
                break
            else:
                print("Command not found, continuing...")            
    




