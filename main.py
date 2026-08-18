# main.py - 프롬프트 관리 프로그램

# 데이터 저장소 (기본 프롬프트 3개 포함)
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

next_id = 4  # 다음 프롬프트 ID


# ── 메뉴 출력 ──────────────────────────────
def show_menu():
    print("\n" + "="*40)
    print("   📋 프롬프트 관리 프로그램")
    print("="*40)
    print("1. 프롬프트 목록 보기")
    print("2. 프롬프트 추가")
    print("3. 프롬프트 검색")
    print("4. 즐겨찾기 보기")
    print("5. 프롬프트 삭제")
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
    title    = input("제목: ").strip()
    content  = input("내용: ").strip()
    category = input("카테고리: ").strip()

    if not title or not content:
        print("❌ 제목과 내용은 필수입니다!")
        return

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


# ── 검색 ───────────────────────────────────
def search_prompt():
    print("\n🔍 프롬프트 검색")
    print("-"*40)
    keyword = input("검색어: ").strip()
    results = [p for p in prompts
               if keyword in p["title"] or keyword in p["content"]]

    if not results:
        print("검색 결과가 없습니다.")
        return
    for p in results:
        star = "⭐" if p["favorite"] else "  "
        print(f"{star} [{p['id']}] {p['title']} ({p['category']})")
        print(f"     {p['content'][:50]}...")


# ── 즐겨찾기 ───────────────────────────────
def show_favorites():
    print("\n⭐ 즐겨찾기 목록")
    print("-"*40)
    favorites = [p for p in prompts if p["favorite"]]
    if not favorites:
        print("즐겨찾기가 없습니다.")
        return
    for p in favorites:
        print(f"⭐ [{p['id']}] {p['title']} ({p['category']})")


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
    while True:
        show_menu()
        choice = input("메뉴 선택: ").strip()

        if choice == "1":
            show_all()
        elif choice == "2":
            add_prompt()
        elif choice == "3":
            search_prompt()
        elif choice == "4":
            show_favorites()
        elif choice == "5":
            delete_prompt()
        elif choice == "0":
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("❌ 잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()