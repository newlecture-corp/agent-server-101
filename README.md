# agent-server-101

Python 과 Gemini API 로 만드는 AI Agent 서버 예제. 0단계부터 20단계까지 코드 하나를 이어서 키웁니다.

## 브랜치 구조

단계마다 완료 시점의 코드가 브랜치와 태그로 남아 있습니다.

```bash
git branch -a                                    # step-00-setup, step-01-first-call, ...
git switch step-03-system-prompt                 # 특정 단계 코드로 이동
git diff step-02-multiturn step-03-system-prompt # 두 단계 사이 변경점
```

`main` 은 항상 최신 단계입니다.

## 실행

```bash
git clone https://github.com/newlecture-corp/agent-server-101.git
cd agent-server-101

curl -LsSf https://astral.sh/uv/install.sh | sh   # uv 설치 (처음 한 번)
uv sync                                           # Python 3.12 + 패키지 설치

cp .env.example .env                              # GEMINI_API_KEY 채우기
uv run python check_env.py                        # 환경 점검
```
