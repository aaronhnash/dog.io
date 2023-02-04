from voice_intro import speech_capture

commands = ["sit", "roll", "over", "come", "fetch"]

with open("output_stream.txt", "w") as text_out:
    text_out.write("")

while True:
    with open("output_stream.txt", "a") as text_out:
        command_found = False
        information = speech_capture()
        if information is not None:
            phrase = information.split(" ")

            for word in phrase:
                if word in commands:
                    text_out.write("Interpreting '" +word+  "' as a command!\n")
                    command_found = True
                    break
            if not command_found:
                text_out.write("Command not found in: " + phrase + "\n")
        else:
            text_out.write("Didn't hear anything.\n")