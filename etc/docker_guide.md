# Docker Guide

## 1. Docker란?
- 컨테이너 기술을 이용하여 애플리케이션을 실행하는 플랫폼
- 컨테이너는 가상화 기술의 한 종류로, 가상 머신(VM)보다 가볍고 빠르게 애플리케이션을 배포할 수 있도록 도와줌

### Docker의 주요 특징
- 가볍고 빠른 실행 속도
- 운영체제에 독립적인 환경 제공
- 애플리케이션 배포 및 관리 용이
- 컨테이너 기반의 마이크로서비스 아키텍처 지원

## 2. Docker 설치
```bash
sudo apt update
sudo apt install docker.io -y
```

## 3. Docker 명령어

### 3.1 Docker 컨테이너 관리
```bash
docker ps -a     # 컨테이너 목록 확인
docker stop [CONTAINER_ID]  # 컨테이너 중지
docker start [CONTAINER_ID]  # 컨테이너 시작
docker rm [CONTAINER_ID]  # 컨테이너 삭제
```

### 3.2 Docker 이미지 관리
```bash
docker images    # 로컬에 저장된 이미지 목록 확인
docker rmi [IMAGE_ID]  # 이미지 삭제
docker pull ubuntu  # Ubuntu 이미지 다운로드
docker build -t my-image .  # Dockerfile을 이용해 이미지 빌드
```

### 3.3 Docker 컨테이너 실행
```bash
docker run -d -p 8080:80  # 컨테이너 실행 (외부 8080 포트 → 내부 80 포트 매핑)
docker exec -it [CONTAINER_ID] /bin/bash  # 실행 중인 컨테이너에 접속
```

## 4. Dockerfile 예제
```Dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
EXPOSE 8000
CMD ["python3", "-m", "http.server", "8000"]
```

