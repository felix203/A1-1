# 🗂️ 프롬프트 관리 프로그램 (Prompt Manager)

GenAI 미션을 수행하며 쌓인 프롬프트를 체계적으로 관리하는 **Python 콘솔 프로그램**입니다.
프롬프트를 카테고리별로 분류하고 키워드로 검색하며, 자주 쓰는 항목은 즐겨찾기로 관리할 수 있습니다.

> codyssey AI Native Advanced 1st mission

---

## 📌 프로젝트 소개

흩어진 프롬프트를 메모장, 노션, 메신저에서 찾아 헤매던 경험을 해결하기 위해 만든
**나만의 프롬프트 관리 도구**입니다.

파이썬의 **리스트·딕셔너리·함수**를 활용해 데이터를 다루는 논리를 익히고,
**Git & GitHub**로 버전 관리와 협업 워크플로우(브랜치·PR·병합)를 경험했습니다.

---

## 🛠️ 개발 환경

| 항목 | 내용 |
|------|------|
| 언어 | Python 3.10+ |
| 에디터 | Visual Studio Code |
| 버전 관리 | Git & GitHub |
| 사용 모듈 | `json`, `os` (Python 내장 모듈) |

---

## 🚀 실행 방법

### 1. 저장소 복제
```bash
git clone https://github.com/felix203/A1-1.git
cd A1-1
```

### 2. 프로그램 실행
```bash
python main.py
```

> Python 3.10 이상이 설치되어 있어야 합니다.
> 버전 확인: `python --version`

---

## ✨ 주요 기능

프로그램 실행 후 **메뉴 번호를 입력**하여 기능을 선택합니다.

| 번호 | 기능 | 설명 |
|:---:|------|------|
| 1 | 📋 프롬프트 목록 보기 | 전체 프롬프트를 ID·제목·카테고리·즐겨찾기(⭐)와 함께 출력 |
| 2 | ➕ 프롬프트 추가 | 제목·내용·카테고리를 입력해 새 프롬프트 등록 (제목 중복 방지) |
| 3 | 📂 카테고리별 조회 | 등록된 카테고리별로 프롬프트를 필터링해 출력 |
| 4 | 🔍 프롬프트 검색 | 제목·내용에 키워드가 포함된 프롬프트 검색 |
| 5 | 🔎 상세 보기 | 특정 프롬프트의 제목·카테고리·상태·내용 전체 표시 |
| 6 | ⭐ 즐겨찾기 관리 | 즐겨찾기 목록 보기 / 즐겨찾기 추가·해제 |
| 7 | ✏️ 프롬프트 수정 | 기존 프롬프트의 제목·내용 수정 |
| 8 | 📊 통계 보기 | 전체 개수, 즐겨찾기 수, 카테고리별 현황(그래프) |
| 9 | 🗑️ 프롬프트 삭제 | 선택한 프롬프트 삭제 |
| 0 | 🚪 종료 | 프로그램 종료 |

> 잘못된 번호 입력 시 안내 메시지를 출력하고 다시 메뉴로 돌아갑니다.

---

## 📁 프롬프트 카테고리

프롬프트는 아래 카테고리로 분류하여 관리합니다.

| 카테고리 | 설명 |
|---------|------|
| 글쓰기 | 블로그·기사 등 글쓰기 프롬프트 |
| 개발 | 코드 리뷰·개발 관련 프롬프트 |
| 번역 | 언어 번역 프롬프트 |
| 이미지 생성 | 이미지 생성용 키워드·묘사 |
| 페르소나 | 캐릭터·역할 설계안 |
| 자동화 | 노코드·워크플로우 자동화 |
| 기타 | 그 외 프롬프트 |

> 추가 시 목록에서 선택하거나 **직접 입력**할 수도 있습니다.

---

## 💾 데이터 저장

- 프롬프트 데이터는 `prompts.json` 파일에 **자동 저장**됩니다.
- 추가·수정·삭제·즐겨찾기 변경 시 즉시 저장되어 프로그램을 종료해도 유지됩니다.
- 프로그램 시작 시 저장된 데이터를 **자동으로 불러옵니다.**
- 이전 미션에서 작성한 **기본 프롬프트 3개**가 등록되어 있습니다.
  (블로그 글쓰기 / 코드 리뷰 / 영어 번역)

---

## 🧩 코드 구조

모든 코드를 한 함수에 몰아넣지 않고 **기능별로 함수를 분리**했습니다.

```
main()              # 메인 루프
show_menu()         # 메뉴 출력
show_all()          # 목록 보기
add_prompt()        # 프롬프트 추가 (중복 방지)
show_by_category()  # 카테고리별 조회
search_prompt()     # 검색
show_detail()       # 상세 보기
manage_favorites()  # 즐겨찾기 관리
edit_prompt()       # 수정
show_stats()        # 통계 보기
delete_prompt()     # 삭제
save_data()         # JSON 저장
load_data()         # JSON 불러오기
```
---
## 🧱 자료구조 선택 이유

### 딕셔너리(dict)를 선택한 이유
프롬프트 하나를 표현할 때 **딕셔너리**를 사용했습니다.

```python
{
    "id": 1,
    "title": "블로그 글쓰기",
    "content": "...",
    "category": "글쓰기",
    "favorite": False
}

항목	내용
선택 이유	제목·내용·카테고리 등 이름(키)으로 값에 접근하므로 가독성이 높음
대안	튜플 → 인덱스(0,1,2...)로 접근해 의미 파악 어려움
대안	클래스 → 기능은 강력하지만 이 규모에서는 과도한 복잡성
리스트(list)를 선택한 이유
전체 프롬프트 목록을 리스트로 관리했습니다.

prompts = [dict1, dict2, dict3, ...]

항목	내용
선택 이유	순서 유지가 필요하고, 추가·삭제·반복이 간단함
대안	집합(set) → 순서 없음, 중복 제거 목적이라 부적합
대안	딕셔너리 → ID를 키로 쓸 수 있지만 순서 보장이 복잡해짐


---

## 🔴 FAIL #17 — while 반복문 설계 이유

### README에 추가할 섹션

```markdown
## 🔄 메인 루프 설계

프로그램의 핵심 흐름은 `while True:` 무한 루프로 구성됩니다.

```python
def main():
    load_data()          # 시작 시 데이터 불러오기
    while True:
        show_menu()      # 메뉴 출력
        choice = input("선택: ")
        if choice == "0":
            print("종료합니다.")
            break        # 유일한 종료 조건
        elif choice == "1":
            show_all()
        # ... 나머지 메뉴
        else:
            print("잘못된 입력입니다.")  # 예외 처리

설계 이유
항목	내용
while True 선택 이유	사용자가 0을 입력하기 전까지 계속 메뉴를 보여줘야 하므로, 종료 시점을 미리 알 수 없는 구조에 적합
종료 조건	사용자가 0 입력 → break로 루프 탈출
안전성	else 블록으로 잘못된 입력을 처리해 프로그램이 비정상 종료되지 않음
대안 비교	for 루프 → 반복 횟수가 정해진 경우에 적합, 메뉴 루프에는 부적합
---

## 🌿 Git 워크플로우

기능 단위로 **브랜치를 나눠 작업**하고 **Pull Request로 병합**했습니다.

| PR | 브랜치 | 작업 내용 |
|:--:|--------|----------|
| #1 | `feature/prompt-manager` | 프롬프트 관리 기본 기능 구현 |
| #2 | `feature/add-functions` | 수정 기능·통계 보기 추가 |
| #3 | `feature/duplicate-check` | 제목 중복 방지 기능 추가 |
| #4 | `feature/file-save` | JSON 저장/불러오기 기능 구현 |

- ✅ 총 **11개 커밋** (기능 단위)
- ✅ `init`, `add`, `commit`, `push`, `pull`, `checkout`, `clone`, `merge` 모두 사용
- ✅ 브랜치 생성 및 병합 기록 4회
- ✅ 로컬에서 `git checkout -b`로 브랜치 생성 후 
     `git merge`로 병합, GitHub PR로 최종 반영

---

## 📷 스크린샷

**git clone 터미널 스크린샷**
<img width="661" height="142" alt="image" src="https://github.com/user-attachments/assets/024b502a-4aa4-4ffc-8eb9-b2a3cf5fb90f" />


**개발 환경 (VSCode, Python·Git 버전)**
<img width="957" height="1028" alt="개발환경" src="https://github.com/user-attachments/assets/bb5d97da-b8f3-49c6-985e-777dd4c56202" />
**프로그램 실행 화면 (메뉴·추가·목록·검색)**

<img width="358" height="781" alt="실행화면2" src="https://github.com/user-attachments/assets/32e75bd3-2620-4574-87cb-2b5bdbe471ef" />
<img width="652" height="724" alt="실행화면1" src="https://github.com/user-attachments/assets/44b8162b-874c-4262-a646-b8789fe56ece" />

**커밋 그래프 (`git log --oneline --graph`)**
<img width="662" height="408" alt="커밋그래프" src="https://github.com/user-attachments/assets/6ee144d8-1b41-4a29-8e71-257192522024" />


---

## 👤 작성자

- GitHub: [felix203](https://github.com/felix203)
