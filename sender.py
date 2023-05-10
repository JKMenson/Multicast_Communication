import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
group = "224.1.1.1"
port = 5004
ttl = 2
message = input("Type Your Message: ")
messageBytes = bytes(message, "utf-8")

sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
sock.sendto(messageBytes, (group, port))