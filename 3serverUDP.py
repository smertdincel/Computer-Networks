import socket

IP = "10.7.87.73"
PORT = 5000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    print("[STARTING] Server is starting.")

    # Creating a UDP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Binding the IP and PORT to the server
    server.bind(ADDR)

    print("[LISTENING] Server is listening.")

    while True:
        # Receiving data and address from the client
        data, addr = server.recvfrom(SIZE)
        print(f"[NEW CONNECTION] {addr} connected.")

        # Receiving the filename from the client
        filename = data.decode(FORMAT)
        print(f"[RECV] Receiving the filename: {filename}")

        # Sending an acknowledgment to the client
        server.sendto("".encode(FORMAT), addr)

        # Receiving the file data from the client
        data, addr = server.recvfrom(SIZE)
        print(f"[RECV] Receiving the file data.")

        # Writing the file data to a file
        with open(filename, "wb") as file:
            file.write(data)

        # Sending an acknowledgment to the client
        server.sendto("".encode(FORMAT), addr)

        print(f"[DISCONNECTED] {addr} disconnected.")


if __name__ == "__main__":
    main()