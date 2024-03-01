import socket

IP = "10.7.87.73"
PORT = 5000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Getting the filename from the user
    filename = "yt.txt"

    # Sending the filename to the server
    client.sendto(filename.encode(FORMAT), ADDR)

    # Receiving acknowledgment from the server
    ack, _ = client.recvfrom(SIZE)
    print(ack.decode(FORMAT))

    with open(filename, "rb") as file:
        # Sending the file data to the server
        file_data = file.read()
        client.sendto(file_data, ADDR)

    # Receiving acknowledgment from the server
    ack, _ = client.recvfrom(SIZE)
    print(ack.decode(FORMAT))

    print("File sent successfully.")

if __name__ == "__main__":
    main()