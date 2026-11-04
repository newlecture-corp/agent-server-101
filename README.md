# agent-server-101

내 PC 에 추론 엔진(Ollama)과 모델(Qwen)을 띄우는 것부터 시작해, 스스로 도구를 골라 쓰고 문서를 찾아 답하는 AI Agent 서버를 Python 으로 만드는 예제. 0단계부터 23단계까지 코드 하나를 이어서 키운다.

## 브랜치 구조

단계마다 완료 시점의 코드가 브랜치와 태그로 남아 있다.

```bash
git branch -a                          # step-00-setup, step-01-ollama, ...
git switch step-03-api                 # 특정 단계 코드로 이동
git diff step-03-api step-04-multiturn # 두 단계 사이 변경점
```

`main` 은 항상 최신 단계다.

## 실행

```bash
git clone https://github.com/newlecture-corp/agent-server-101.git
cd agent-server-101

curl -LsSf https://astral.sh/uv/install.sh | sh   # uv 설치 (처음 한 번)
uv sync                                           # Python 3.12 + 패키지 설치
uv run python check_env.py                        # 환경 점검
```
