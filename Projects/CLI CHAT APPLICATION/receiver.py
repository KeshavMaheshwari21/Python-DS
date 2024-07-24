# The Socket library is used to establish connection between computers.
import socket
import datetime

# creating the object of the socket class
# AF_INET is used to send message through internet
# We have to use some protocol to send the message
# SOCK_DGRAM is UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# ip_address = "192.168.1.22" for network
ip_address = "127.0.0.1" # single-person
port_no = 2525 # 0---65353

complete_address = (ip_address,port_no)
s.bind(complete_address)

print("Ready to receive Message!")
print("Press 0 to QUIT!\n")

# using now() to get current time
current_time = datetime.datetime.now()
time = str(current_time)
while True:

    message = s.recvfrom(100) # We are giving a buffer size that at a time 100 char message
    
    received_message=message[0]
    decrypted_message = received_message.decode('ascii')

    if(decrypted_message == "0"):
        print("\nSender Quits!\n")
        break

    print("Sender :",decrypted_message)

    sender_address = message[1][0]

    with open(sender_address+'.txt','a+') as file:
        file.write(time+"  "+decrypted_message+'\n')

    send_address = message[1]

    message_to_send = input("Enter to message back :")
    
    encrypt_send_message = message_to_send.encode('ascii')
    s.sendto(encrypt_send_message,send_address)
    if(message_to_send == "0"):
        print("\nYou Quit!\n")
        break