servicePorts = {}

while True:
    service = input("Please enter a services name or type '0' to stop:")
    if service == "0":
        break
    port = input("Please enter a port number or type '0' to stop:")
    if port == "0":
        break

    servicePorts[service] = port

print(servicePorts)