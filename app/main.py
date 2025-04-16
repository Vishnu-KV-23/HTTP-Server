import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    #Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    #server_socket.accept() # wait for client
    server_socket.accept()[0].sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    #byte literak needed to send data accross network, server_socket.accept() returns a tuple (client_socket, address) where client_socket is the socket object for the client and address is the address of the client. We use this object to use the sendall function
    #status line and header.. first crlf means end of status line and next crlf means end of header lines

if __name__ == "__main__":
    main()
