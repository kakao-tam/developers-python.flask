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
├── static/            # 정적 파일 디렉토리
│   └── style.css     # 스타일시트
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

2. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

## 설정 방법

1. [카카오 개발자 콘솔](https://developers.kakao.com)에서 애플리케이션을 생성합니다.
2. 생성된 애플리케이션의 REST API 키를 `api.py`의 `client_id` 변수에 입력합니다.
3. Client Secret을 `api.py`의 `client_secret` 변수에 입력합니다.
4. 카카오 개발자 콘솔의 "카카오 로그인 > 플랫폼 > Web 플랫폼"에서 사이트 도메인을 등록합니다.
5. 카카오 개발자 콘솔의 "카카오 로그인 > 카카오 로그인 활성화"를 ON으로 설정합니다.
6. Redirect URI를 `http://localhost:4000/redirect`로 등록합니다.

## 실행 방법

```bash
python api.py
```

실행 후 웹 브라우저에서 `http://localhost:4000`으로 접속하면 웹 애플리케이션을 확인할 수 있습니다.

## API 엔드포인트

- `/`: 메인 페이지
- `/authorize`: 카카오 로그인 인증
- `/redirect`: 카카오 로그인 콜백 처리
- `/profile`: 사용자 프로필 조회
- `/friends`: 친구 목록 조회
- `/message`: 나에게 메시지 전송
- `/friends_message`: 친구에게 메시지 전송
- `/logout`: 로그아웃
- `/unlink`: 계정 연결 해제

## 주의사항

- 이 프로젝트는 개발 환경을 위한 예제입니다. 실제 서비스에 사용할 경우 보안 설정을 추가해야 합니다.
- 카카오 API 사용을 위해서는 카카오 개발자 계정이 필요합니다.
- 실제 서비스에서는 HTTPS를 사용해야 합니다.

## 스크린샷

<img width="817" alt="image" src="https://github.com/user-attachments/assets/7a04964f-b5ad-45fe-a634-24675cb3036d" />
