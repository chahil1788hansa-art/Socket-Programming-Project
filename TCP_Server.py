# TCP Server
# Import modules relevant to your application development and socket programming.


import socket

#Define the server IP and port addresses that the client connects to.
TCP_Server_IP =  '192.168.1.124'
TCP_Server_PORT = 10000

#Create a server side TCP socket.
Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Setting socket reuse option
Server_Socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

try:
    # Bind the socket to the address and port.
    Server_Socket.bind((TCP_Server_IP, TCP_Server_PORT))

    # Start listening for the client connections
    Server_Socket.listen(5)
    print(f"Server listening on {TCP_Server_IP}:{TCP_Server_PORT}")

    while True:
        # Accept client connection
        connectionSocket, addr = Server_Socket.accept()
        print("The Server is ready to receive")

        try:
            # Continuous inner streaming loop to keep handling data from the client
            while True:
                # Receive message from the client
                Message = connectionSocket.recv(2048).decode()
                if not Message:
                    break
                    
                capitalizedSentence = Message.upper()
                print(f"{capitalizedSentence} received from {addr}")

                #Sending the received data back
                connectionSocket.send(capitalizedSentence.encode())

        except ConnectionResetError:
            print("Client disconnected")

        except Exception as e:
            print(f"Error: {e}")

        except ConnectionError:
            print("Connection Error")

        finally:
            # To close the client connection after they exit the inner loop
            connectionSocket.close()
            print("Client connection closed")

except KeyboardInterrupt:
    print("Server closing down")

except Exception as e:
    print(f"Error: {e}")
    
finally:
    Server_Socket.close()
    print("TCP Connection closed")
