from pydoc import cli
from socket import *
# 1. 클라이언트의 메시지를 받는 주소를 설정해야함. (주소 == 서버 ip, 서버 port 번호)
serverName = '127.0.0.1'
serverPort = 12000

# 2. TCP용 소켓 생성
clientSocket = socket(AF_INET, SOCK_STREAM)
# socket() 의 파라미터 설명 
#   2-1. AF_INET == ipv4의 주소를 가진 애랑 연결하겠다는 의미.
#   2-2. SOCK_STREAM == TCP 용 소켓을 만들겠다는 의미. (TCP는 순서를 보장하고 신뢰성을 가진 통신 방식임.)
#   2-3. socket 함수의 리턴 값은 "소켓을 구분하기 위한 번호" 임. (socket 디스크립터).


# 3. TCP는 메시지 보내기 전에 connection이 있어야함. -> connect()로 서버와 연결시도.
clientSocket.connect((serverName, serverPort))

# 4. 채팅 구현
while True:
    # 4-1. 내가 보낼 메시지 입력해서 sendData에 넣음
    sendData = input('>>> ')
    # 4-2. sendData 보냄
    clientSocket.send(sendData.encode())

    # 4-3. 상대가 보낸 메시지 받아서 recvData에 넣음
    recvData = clientSocket.recv(1024)
    # 4-4. recvData 출력
    print('상대방 : ',recvData.decode())
    
    # 4-5. q를 보내거나 받았을 경우 break 후 소켓 종료    
    if sendData == 'q' :
        break
    if recvData == 'q' :
        break
    

    # 4-6. 소켓 종료 
clientSocket.close()