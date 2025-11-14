"""
LRU Page Replacement Simulator (menu driven, simple)

- Enter reference string as space-separated integers.
- Enter number of frames (positive integer).
- Lower-level implementation suitable for beginners.
"""

def get_input():
    ref = input("Enter reference string (space-separated page numbers): ").strip()
    if not ref:
        print("Reference string cannot be empty.")
        return None, None
    try:
        pages = list(map(int, ref.split()))
    except ValueError:
        print("Invalid reference string: use integers separated by spaces.")
        return None, None

    try:
        frames_count = int(input("Enter number of frames: ").strip())
        if frames_count <= 0:
            print("Number of frames must be a positive integer.")
            return None, None
    except ValueError:
        print("Invalid frame count: enter a positive integer.")
        return None, None

    return pages, frames_count


def run_lru(pages, frames_count):
    frames = []                # current pages in frames (order not significant)
    last_used = {}             # page -> last time index when it was used
    page_faults = 0

    print("\nLRU Page Replacement Process:")
    for t, page in enumerate(pages):
        # Hit: page already in frames
        if page in frames:
            last_used[page] = t
            print(f"Ref {page:>2} -> Frames: {frames} (hit)")
            continue

        # Miss / page fault
        page_faults += 1

        if len(frames) < frames_count:
            # empty frame available: load page
            frames.append(page)
            last_used[page] = t
            print(f"Ref {page:>2} -> Frames: {frames} (fault, loaded)")
            continue

        # no empty frame: find LRU page to replace
        # consider only pages currently in frames and pick the one with smallest last_used
        lru_page = min(frames, key=lambda p: last_used.get(p, -1))
        replace_index = frames.index(lru_page)
        frames[replace_index] = page

        # update last_used: remove old page entry and set for new page
        del last_used[lru_page]
        last_used[page] = t

        print(f"Ref {page:>2} -> Frames: {frames} (fault, replaced {lru_page})")

    print(f"\nTotal page faults (LRU): {page_faults}\n")
    return page_faults


def main_menu():
    while True:
        print("\n=== LRU Page Replacement Simulator ===")
        print("1. Run LRU algorithm")
        print("2. Exit")
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == "1":
            pages, frames_count = get_input()
            if pages is None:
                continue
            run_lru(pages, frames_count)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1 or 2.")


if __name__ == "__main__":
    main_menu()