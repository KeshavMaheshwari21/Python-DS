# The Socket library is used to establish connection between computers.
import socket
# creating the object of the socket class
# AF_INET is used to send message through internet
# We have to use some protocol to send the message
# SOCK_DGRAM is UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# target_ip = "192.168.1.22"
target_ip = "127.0.0.1"
port_no = 2525

target_address = (target_ip,port_no)

print("Ready to send Message!")
print("Press 0 to QUIT!\n")

while True:

    message = input("Please write the message :")
    
    encrypt_message = message.encode('ascii') # Encrypting the message
    s.sendto(encrypt_message,target_address)

    if(message == "0"):
        print("\nYou Quit!\n")
        break

    rec_message = s.recvfrom(100) # We are giving a buffer size that at a time 100 char message
   
    received_message=rec_message[0]
    decrypted_message = received_message.decode('ascii')

    if(decrypted_message == "0"):
        print("\nReceiver Quits!\n")
        break

    print("Receiver :",decrypted_message)
