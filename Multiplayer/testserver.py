import socket

# 서버 설정
HOST = "0.0.0.0"  # 모든 네트워크에서 수신
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("서버 대기 중...")
conn, addr = server_socket.accept()
print(f"{addr}에서 연결됨.")

# 전송할 이미지 파일 경로
file_path = "Multiplayer/images/PokerTable.png"

# 1. 이미지 파일을 읽고 바이너리 데이터로 변환
with open(file_path, "rb") as f:
    image_data = f.read()

# 2. 파일 크기 전송 (4바이트)
file_size = len(image_data)
conn.send(file_size.to_bytes(4, 'big'))

# 3. 파일 데이터 전송
conn.sendall(image_data)

print("이미지 전송 완료!")
conn.close()
server_socket.close()
