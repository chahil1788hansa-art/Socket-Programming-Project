# UDP Client
# Worked in a pair by Manraj Singh & Chahil Chahil
import socket

UDP_Server_Host = '127.0.0.1'
UDP_Server_Port = 10000

UDP_Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_Client_Socket.settimeout(5)

print(f"UDP Client initialized. Connected to placeholder state for {UDP_Server_Host}:{UDP_Server_Port}")

while True:
    UDP_Client_message = input("\nEnter your message here or 'exit' to end: ").strip()

    if not UDP_Client_message:
        print("Message cannot be empty.")
        continue

    if UDP_Client_message.lower() == "exit":
        print("Exiting application...")
        break

    try:
        UDP_Client_Socket.sendto(UDP_Client_message.encode('utf-8'), (UDP_Server_Host, UDP_Server_Port))

        # Receive echoed message
        data, server_address = UDP_Client_Socket.recvfrom(2048)
        print(f"Message received response from {server_address}")
        print(f"Message received: {data.decode('utf-8')} from {server_address}")

    except socket.timeout:
        print("Error: Connection timed out. No response from server.")
    except Exception as e:
        print(f"An error occurred: {e}")
        break

# FIX: Moved socket close strictly outside the loop execution block
UDP_Client_Socket.close()
print("UDP_Client is closed.")
