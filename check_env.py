"""0단계 환경 점검.

실행:  uv run python check_env.py
"""

import sys


def main() -> int:
    print(f"Python   : {sys.version.split()[0]}")
    print(f"가상환경  : {sys.prefix}")
    print()

    if sys.version_info[:2] != (3, 12):
        print("Python 3.12 가 아니다. .python-version 을 확인하고 uv sync 를 다시 실행한다.")
        return 1

    if sys.prefix == sys.base_prefix:
        print("가상환경 밖에서 실행했다. `uv run python check_env.py` 로 실행한다.")
        return 1

    print("환경 준비 완료. 1단계로 넘어간다.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
