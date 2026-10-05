#Importing module relevant to the application
import socket

#Defining server ip and port address
TCP_Server_Host = '192.168.1.124'
TCP_Server_Port = 10000

# Creating a client side TCP Socket
TCP_Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    TCP_Client_Socket.connect((TCP_Server_Host, TCP_Server_Port))

    while True:
        #Getting input from the client
        Message = input("Enter your message or 'exit' to end: ")

        if Message.lower() == "exit":
            break

        try:
            #Sending message to the server
            TCP_Client_Socket.sendall(Message.encode())

            #Message received from the server
            modifiedSentence = TCP_Client_Socket.recv(2048)

            if not modifiedSentence:
                print("Server closed the connection.")
                break
                
            # Display the received message
            print("Echo message from TCP_Server:", modifiedSentence.decode())

        except ConnectionAbortedError:
            print("Connection was aborted.")
            break

        except ConnectionResetError:
            print("Server closed/reset the connection.")
            break

        except Exception as e:
            print("Error:", e)
            break

except Exception as e:
    print("Connection error:", e)

finally:
    # Closed outside the while loop so the socket isn't dropped after the first message
    TCP_Client_Socket.close()
    print("TCP Client Closed")
