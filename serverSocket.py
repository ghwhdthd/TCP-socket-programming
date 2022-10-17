from socket import *

# 1. 포트 번호 설정
serverPort = 12000

# 2. TCP용 welcome 소켓 생성
serverWelcomeSocket = socket(AF_INET, SOCK_STREAM)
# socket() 의 파라미터 설명 
#   2-1. AF_INET == ipv4의 주소를 가진 애랑 연결하겠다는 의미.
#   2-2. SOCK_STREAM == TCP 용 소켓을 만들겠다는 의미. (TCP는 순서를 보장하고 신뢰성을 가진 통신 방식임.)
#   2-3. socket 함수의 리턴 값은 "소켓을 구분하기 위한 번호"임 (socket 디스크립터).

# 3. welcome 소켓을 ip 주소 + port번호와 연결(bind) 해줘야함.
serverWelcomeSocket.bind(('', serverPort))
# bind()의 파라미터 설명
#   3-1. '' == 서버에는 여려 개의 ip가 존재할 수 있는데 '' 로 설정했다는 것은 어떤 ip든 상관없이 port번호만 맞으면 내가 서비스 하겠다는 의미.
#   3-2. serverPort == 위에 설정한 포트 번호



# 4. welcome 소켓은 클라이언트의 요청이 오기를 기다림.
serverWelcomeSocket.listen(1)
#   4-1. listen(1)에서 1의 의미는 최대 1개의 연결 요청을 큐에 넣겠다는 의미. -> 1개까지 연결 가능하다.
    
print('The TCP server is ready to receive.')

# 5. 클라이언트로 부터 connection이 오면 서버는 accept 함.   
connectionSocket,clientAddr = serverWelcomeSocket.accept()
#   5-1. accept를 하는 것과 동시에 서버는 새로운 소켓을 만들어냄. 그게 connectionSocket이다.
#   5-2. clientAddr == 요청한 클라이언트의 주소

#   상황 정리.
#   즉, welcome 소켓은 클라이언트 요청이 오기를 기다렸다가 수락하고 
#   새로운 connetionSocket을 만들어서 요청한 클라이언트와 연결시키는 일을 수행.
#   실제 업무는 connectionSocket가 다 하는 구조임.


# 6. 채팅 구현
while True:
    # 6-1. 상대가 보낸 메시지 받아서 recvData에 넣음
    recvData = connectionSocket.recv(1024).decode()
    # 6-2. recvData 출력
    print('상대방 : ', recvData)
    
    # 6-3. 내가 보낼 메시지 입력해서 sendData에 넣음
    sendData = input('>>> ')
    # 6-4. sendData 보냄
    connectionSocket.send(sendData.encode())

    # 6-5. q를 보내거나 받았을 경우 break 후 소켓 종료    
    if sendData == 'q' :
        break
    if recvData == 'q' :
        break

    # 6-6. 소켓 종료 
serverWelcomeSocket.close()

