import socket
import serial

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.0.39", 1234))
server.listen()
print("[*] Server listening on port 1234...")

ser = serial.Serial("/dev/ttyACM0")
print("[*] Serial communication established")

soc, addr = server.accept()
print("[*] Connection established for", addr)

while True:
    speed = soc.recv(128).decode().replace("\r", "")

    if not speed:
        continue

    ser.write(speed.encode())