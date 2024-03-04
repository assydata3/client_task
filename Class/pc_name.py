import socket

pc_dist = {
    "10.169.211.74": "main_pc"
}

pc_ip = socket.gethostbyname(socket.gethostname())
try:
     pc_name = pc_dist[pc_ip]
except:
    pc_name = 'unknow'


