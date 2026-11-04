"""0단계 환경 점검 스크립트.

실행:  uv run python check_env.py

확인하는 것
  1. .env 파일이 읽히는가
  2. GEMINI_API_KEY 가 들어 있는가
  3. google-genai SDK 가 설치되어 있는가
  4. (키가 있으면) Gemini 서버에 실제로 연결되는가
"""

import os
import sys

from dotenv import load_dotenv


def main() -> int:
    load_dotenv()  # 현재 폴더의 .env 를 읽어 환경변수로 올립니다.

    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

    print(f"Python      : {sys.version.split()[0]}")

    if not api_key or api_key.startswith("여기에"):
        print("GEMINI_API_KEY: 없음  ->  .env 파일을 만들고 키를 넣어 주세요.")
        return 1
    print(f"GEMINI_API_KEY: 있음 (앞 4자리 {api_key[:4]}...)")

    try:
        from google import genai
    except ImportError:
        print("google-genai: 설치 안 됨  ->  uv sync 를 실행해 주세요.")
        return 1
    print(f"google-genai: {genai.__version__}")

    # 실제 연결 확인: 모델 정보를 한 번 조회합니다. (토큰을 쓰지 않습니다)
    client = genai.Client(api_key=api_key)
    info = client.models.get(model=model)
    print(f"모델 연결    : {info.name}  (입력 한도 {info.input_token_limit:,} 토큰)")
    print("\n환경 준비 완료. 1단계로 넘어가세요.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
