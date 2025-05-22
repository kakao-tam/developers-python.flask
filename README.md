# Kakao REST API Python Flask 예제

이 프로젝트는 Kakao REST API를 Python Flask로 구현한 예제입니다.

## 주요 기능

- 카카오 로그인
- 사용자 정보 가져오기
- 친구 목록 가져오기
- 나에게 메시지 발송
- 친구에게 메시지 발송
- 로그아웃
- 연결 끊기

## 프로젝트 구조
```
.
├── api.py              # Flask 애플리케이션 메인 파일
├── requirements.txt    # 프로젝트 의존성 파일
├── templates/         # HTML 템플릿 디렉토리
│   └── index.html    # 메인 페이지 템플릿
└── README.md         # 프로젝트 설명 파일
```

## 설치 방법

1. 가상환경 생성 및 활성화 (선택사항)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
```

2. 의존성 설치
```bash
pip install -r requirements.txt
```

3. 카카오 개발자 설정
- [Kakao Developers](https://developers.kakao.com)에서 애플리케이션 생성
- 생성된 애플리케이션의 REST API 키를 `api.py`의 `client_id` 변수에 입력합니다.
- Client Secret을 `api.py`의 `client_secret` 변수에 입력합니다.
- 카카오 개발자 콘솔의 "카카오 로그인 > 플랫폼 > Web 플랫폼"에서 사이트 도메인을 등록합니다.
- 카카오 개발자 콘솔의 "카카오 로그인 > 카카오 로그인 활성화"를 ON으로 설정합니다.
- Redirect URI를 `http://localhost:4000/redirect`로 등록합니다.

4. 서버 실행
```bash
python api.py
```

## 사용 방법

1. 브라우저에서 `http://localhost:4000` 접속
2. 카카오 로그인 버튼 클릭
3. 각 기능 버튼을 통해 API 테스트

## 주의사항

- 이 프로젝트는 개발 환경을 위한 예제입니다. 실제 서비스에 사용할 경우 보안 설정을 추가해야 합니다.
- 카카오 API 사용을 위해서는 카카오 개발자 계정이 필요합니다.
- 실제 서비스에서는 HTTPS를 사용해야 합니다.

## 스크린샷
![image](https://github.com/user-attachments/assets/2a4b9a6b-5224-49db-9f65-1b22223f2603)

