import pygame
import socket
from PIL import Image
import io

# Pygame 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("수신된 이미지")

# 서버 연결
HOST = "127.0.0.1"  # 서버 IP 주소 (서버 실행 중인 컴퓨터의 IP로 변경 가능)
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# 1. 파일 크기 수신 (4바이트)
file_size = int.from_bytes(client_socket.recv(4), 'big')
print(f"수신할 파일 크기: {file_size} 바이트")

# 2. 이미지 데이터 수신
received_data = b""
while len(received_data) < file_size:
    packet = client_socket.recv(4096)
    if not packet:
        break
    received_data += packet

client_socket.close()

# 3. 받은 데이터를 PIL 이미지로 변환
image = Image.open(io.BytesIO(received_data))  # 메모리에서 이미지 열기
image = image.convert("RGB")  # pygame은 RGB 형식 필요

# 4. PIL 이미지를 pygame 이미지로 변환
mode = image.mode
size = image.size
data = image.tobytes()

pygame_image = pygame.image.fromstring(data, size, mode)

# Pygame 루프 (이미지 표시)
running = True
while running:
    screen.fill((0, 0, 0))  # 배경 검은색
    screen.blit(pygame_image, ((WIDTH - size[0]) // 2, (HEIGHT - size[1]) // 2))  # 중앙 정렬
    pygame.display.flip()  # 화면 업데이트

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
