
while True:
    with open("output_stream.txt", "a") as text_out:
        text_out.write("This is a test!\n")
        temp = "stuff"
        text_out.write("Test 2: " + temp +"\n")