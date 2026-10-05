# UDP Server
# Import modules relevant to your application development and socket programming.
# Worked in pair by Manraj Singh and Chahil

import socket

#Define the server IP and port addresses that the client connects to.
UDP_Server_IP = '192.168.1.124'
UDP_Server_PORT = 10000

#Create a server side UDP socket.
UDP_Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind the socket to the address and port.
UDP_Server_Socket.bind((UDP_Server_IP, UDP_Server_PORT))
print(f"UDP_Server listening for clients on {UDP_Server_IP}:{UDP_Server_PORT}")

try:
    # Infinite execution loop so the process stays up for continuous testing
    while True:
        #Receive data from the client.
        data, client_address = UDP_Server_Socket.recvfrom(2048)
        client_message = data.decode()
        capitalizedSentence = client_message.upper()
        print(f"Message received from {client_address}: {capitalizedSentence}")

        #Process the input and send a response.
        UDP_Server_Socket.sendto(capitalizedSentence.encode(), client_address)

except socket.timeout:
    print("Connection timed out")

except KeyboardInterrupt:
    print("UDP_Server Shutting Down...")

except ConnectionError:
    print("Connection Error")

finally:
    # Close the socket to release the port and system resources
    UDP_Server_Socket.close()
    print(f"UDP_Server is closed")
