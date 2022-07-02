try:
    with open("txt.txt", "r") as text:
        text.write("Test")

except Exception:
    print("Unsupported Operation, cannot write in read mode.")