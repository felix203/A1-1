# main.py - 프롬프트 관리 프로그램
import json  # ← 추가
import os    # ← 추가
prompts = [
    {
        "id": 1,
        "title": "블로그 글쓰기",
        "content": "당신은 전문 블로거입니다. 주어진 주제로 읽기 쉽고 흥미로운 블로그 글을 작성해주세요.",
        "category": "글쓰기",
        "favorite": False
    },
    {
        "id": 2,
        "title": "코드 리뷰",
        "content": "당신은 시니어 개발자입니다. 아래 코드를 검토하고 개선점을 알려주세요.",
        "category": "개발",
        "favorite": True
    },
    {
        "id": 3,
        "title": "영어 번역",
        "content": "당신은 전문 번역가입니다. 아래 한국어 텍스트를 자연스러운 영어로 번역해주세요.",
        "category": "번역",
        "favorite": False
    }
]

next_id = 4
CATEGORIES = ["글쓰기", "개발", "번역", "이미지 생성", "페르소나", "자동화", "기타"]

FILE_NAME = "prompts.json"  # ← 추가


# ── 저장 ───────────────────────────────────
def save_data():
    data = {
        "next_id": next_id,
        "prompts": prompts
    }
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("💾 저장 완료!")


# ── 불러오기 ───────────────────────────────
def load_data():
    global prompts, next_id
    if not os.path.exists(FILE_NAME):
        return  # 파일 없으면 기본 데이터 사용
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
    prompts = data["prompts"]
    next_id = data["next_id"]
    print("📂 데이터 불러오기 완료!")

# ── 메뉴 출력 ──────────────────────────────
def show_menu():
    print("\n" + "="*40)
    print("   📋 프롬프트 관리 프로그램")
    print("="*40)
    print("1. 프롬프트 목록 보기")
    print("2. 프롬프트 추가")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 프롬프트 수정")   # ← 새로 추가
    print("8. 통계 보기")       # ← 새로 추가
    print("9. 프롬프트 삭제")   # ← 9번으로 변경
    print("0. 종료")
    print("="*40)


# ── 목록 보기 ──────────────────────────────
def show_all():
    print("\n📋 전체 프롬프트 목록")
    print("-"*40)
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for p in prompts:
        star = "⭐" if p["favorite"] else "  "
        print(f"{star} [{p['id']}] {p['title']} ({p['category']})")
    print("-"*40)


# ── 프롬프트 추가 ──────────────────────────
def add_prompt():
    global next_id
    print("\n➕ 프롬프트 추가")
    print("-"*40)

    while True:
        title = input("제목: ").strip()
        if title:
            duplicate = False
            for prompt in prompts:
                if prompt["title"] == title:
                    duplicate = True
                    break
            
            if duplicate:
                print(f"⚠️ '{title}' 은(는) 이미 존재하는 제목입니다!")
                print("다른 제목을 입력해주세요.")
                continue  # 다시 제목 입력
            break
        print("❌ 제목은 필수입니다!")

    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("❌ 내용은 필수입니다!")

    print("\n카테고리 선택:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")
    print(f"  {len(CATEGORIES)+1}. 직접 입력")

    while True:
        try:
            cat_choice = int(input("번호 선택: "))
            if 1 <= cat_choice <= len(CATEGORIES):
                category = CATEGORIES[cat_choice - 1]
                break
            elif cat_choice == len(CATEGORIES) + 1:
                category = input("카테고리 직접 입력: ").strip()
                if category:
                    break
                print("❌ 카테고리를 입력해주세요!")
            else:
                print("❌ 올바른 번호를 선택해주세요!")
        except ValueError:
            print("❌ 숫자를 입력해주세요!")

    new_prompt = {
        "id": next_id,
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_prompt)
    next_id += 1
    print(f"✅ '{title}' 프롬프트가 추가되었습니다!")


# ── 카테고리별 조회 ────────────────────────
def show_by_category():
    print("\n📂 카테고리별 조회")
    print("-"*40)

    used_categories = sorted(list(set(p["category"] for p in prompts)))

    print("카테고리 목록:")
    for i, cat in enumerate(used_categories, 1):
        count = len([p for p in prompts if p["category"] == cat])
        print(f"  {i}. {cat} ({count}개)")

    while True:
        try:
            choice = int(input("\n번호 선택: "))
            if 1 <= choice <= len(used_categories):
                selected = used_categories[choice - 1]
                break
            print("❌ 올바른 번호를 선택해주세요!")
        except ValueError:
            print("❌ 숫자를 입력해주세요!")

    results = [p for p in prompts if p["category"] == selected]
    print(f"\n📂 [{selected}] 카테고리 프롬프트")
    print("-"*40)
    for p in results:
        star = "⭐" if p["favorite"] else "  "
        print(f"{star} [{p['id']}] {p['title']}")
    print("-"*40)


# ── 검색 ───────────────────────────────────
def search_prompt():
    print("\n🔍 프롬프트 검색")
    print("-"*40)
    keyword = input("검색어: ").strip()
    if not keyword:
        print("❌ 검색어를 입력해주세요!")
        return

    results = [p for p in prompts
               if keyword in p["title"] or keyword in p["content"]]

    if not results:
        print("검색 결과가 없습니다.")
        return

    print(f"\n🔍 '{keyword}' 검색 결과 ({len(results)}개)")
    print("-"*40)
    for p in results:
        star = "⭐" if p["favorite"] else "  "
        print(f"{star} [{p['id']}] {p['title']} ({p['category']})")
        print(f"     {p['content'][:50]}...")
    print("-"*40)


# ── 상세 보기 ──────────────────────────────
def show_detail():
    print("\n🔎 프롬프트 상세 보기")
    print("-"*40)
    show_all()

    try:
        pid = int(input("상세 볼 ID: "))
        target = next((p for p in prompts if p["id"] == pid), None)
        if not target:
            print("❌ 해당 ID가 없습니다.")
            return

        star = "⭐ 즐겨찾기" if target["favorite"] else "즐겨찾기 없음"
        print(f"\n{'='*40}")
        print(f"📌 제목    : {target['title']}")
        print(f"📂 카테고리: {target['category']}")
        print(f"⭐ 상태    : {star}")
        print(f"📝 내용    :")
        print(f"{target['content']}")
        print(f"{'='*40}")

    except ValueError:
        print("❌ 숫자를 입력해주세요.")


# ── 즐겨찾기 관리 ──────────────────────────
def manage_favorites():
    print("\n⭐ 즐겨찾기 관리")
    print("-"*40)
    print("1. 즐겨찾기 목록 보기")
    print("2. 즐겨찾기 추가/해제")
    print("-"*40)

    choice = input("선택: ").strip()

    if choice == "1":
        favorites = [p for p in prompts if p["favorite"]]
        if not favorites:
            print("즐겨찾기가 없습니다.")
            return
        print(f"\n⭐ 즐겨찾기 목록 ({len(favorites)}개)")
        print("-"*40)
        for p in favorites:
            print(f"⭐ [{p['id']}] {p['title']} ({p['category']})")
        print("-"*40)

    elif choice == "2":
        show_all()
        try:
            pid = int(input("즐겨찾기 변경할 ID: "))
            target = next((p for p in prompts if p["id"] == pid), None)
            if not target:
                print("❌ 해당 ID가 없습니다.")
                return
            target["favorite"] = not target["favorite"]
            status = "추가" if target["favorite"] else "해제"
            print(f"✅ '{target['title']}' 즐겨찾기 {status}!")
        except ValueError:
            print("❌ 숫자를 입력해주세요.")
    else:
        print("❌ 잘못된 입력입니다.")


# ── 프롬프트 수정 ──────────────────────────
def edit_prompt():
    print("\n✏️  프롬프트 수정")
    print("-"*40)
    show_all()

    try:
        pid = int(input("수정할 ID: "))
        target = next((p for p in prompts if p["id"] == pid), None)
        if not target:
            print("❌ 해당 ID가 없습니다.")
            return

        print(f"\n현재 제목: {target['title']}")
        new_title = input("새 제목 (그대로면 Enter): ").strip()

        print(f"현재 내용: {target['content'][:50]}...")
        new_content = input("새 내용 (그대로면 Enter): ").strip()

        if new_title:
            target["title"] = new_title
        if new_content:
            target["content"] = new_content

        print("✅ 수정 완료!")

    except ValueError:
        print("❌ 숫자를 입력해주세요.")


# ── 통계 보기 ──────────────────────────────
def show_stats():
    print("\n📊 통계")
    print("="*40)
    print(f"전체 프롬프트 : {len(prompts)}개")
    print(f"즐겨찾기      : {len([p for p in prompts if p['favorite']])}개")
    print()
    print("📂 카테고리별 현황")
    print("-"*40)
    used = {}
    for p in prompts:
        used[p["category"]] = used.get(p["category"], 0) + 1
    for cat, count in sorted(used.items()):
        bar = "█" * count
        print(f"  {cat:<10} {bar} ({count}개)")
    print("="*40)


# ── 삭제 ───────────────────────────────────
def delete_prompt():
    print("\n🗑️  프롬프트 삭제")
    print("-"*40)
    show_all()
    try:
        pid = int(input("삭제할 ID: "))
        target = next((p for p in prompts if p["id"] == pid), None)
        if not target:
            print("❌ 해당 ID가 없습니다.")
            return
        prompts.remove(target)
        print(f"✅ [{pid}] '{target['title']}' 삭제 완료!")
    except ValueError:
        print("❌ 숫자를 입력해주세요.")


# ── 메인 루프 ──────────────────────────────
def main():
    print("프롬프트 관리 프로그램을 시작합니다!")
    load_data()  # ← 추가 (시작 시 자동 불러오기)
    while True:
        show_menu()
        choice = input("메뉴 선택: ").strip()

        if choice == "1":
            show_all()
        elif choice == "2":
            add_prompt()
            save_data()   # ← 추가
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            manage_favorites()
            save_data()   # ← 추가
        elif choice == "7":
            edit_prompt()
            save_data()   # ← 추가
        elif choice == "8":
            show_stats()
        elif choice == "9":
            delete_prompt()
            save_data()   # ← 추가
        elif choice == "0":
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("❌ 잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()