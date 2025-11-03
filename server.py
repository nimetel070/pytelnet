import socket
import os
import sys

# The ASCII art for "KERNEL"
# Note: Telnet clients typically expect \r\n (CRLF) for a new line.
ASCII_ART = """
  _  __ _____ ___ _____ _   _
 | |/ // ____|/ _ \_   _| \ | |
 | ' /| (___| | | || | |  \| |
 |  <  \___ \| | | || | | . ` |
 | . \ ____) | |_| || |_| |\  |
 |_|\_\_____|\___/_____|_| \_|
\r\n
Welcome to KERNEL Telnet Server on Render!
Closing connection in 5 seconds...\r\n
""".encode('ascii') # Encode the text to bytes using ASCII

HOST = '0.0.0.0'
# Render automatically sets the PORT environment variable
PORT = int(os.environ.get('PORT', 8080))

# Create a socket object (AF_INET for IPv4, SOCK_STREAM for TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Binding to {HOST}:{PORT}")
    s.bind((HOST, PORT))
    # Listen for one incoming connection
    s.listen(1)
    print("Server listening...")

    while True:
        try:
            # Accept a connection
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                # Send the ASCII art and closing message
                conn.sendall(ASCII_ART)
                # After sending the message, we can close the connection
                conn.close()
                print(f"Disconnected from {addr}")

        except KeyboardInterrupt:
            print("\nServer shutting down.")
            sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")
