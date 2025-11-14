"""
FIFO Page Replacement Simulator (menu driven, simple)

- Enter reference string as space-separated integers.
- Enter number of frames (positive integer).
- Program shows frame contents after each reference and total page faults.
"""

def run_fifo(pages, frames_count):
    frames = []
    page_faults = 0
    next_replace = 0  # index to replace next (circular)

    print("\nFIFO Page Replacement Process:")
    for page in pages:
        if page in frames:
            print(f"Ref {page:>2} -> Frames: {frames} (hit)")
        else:
            page_faults += 1
            if len(frames) < frames_count:
                frames.append(page)
                print(f"Ref {page:>2} -> Frames: {frames} (fault, loaded)")
            else:
                replaced = frames[next_replace]
                frames[next_replace] = page
                next_replace = (next_replace + 1) % frames_count
                print(f"Ref {page:>2} -> Frames: {frames} (fault, replaced {replaced})")

    print(f"\nTotal page faults (FIFO): {page_faults}\n")
    return page_faults

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

def main_menu():
    while True:
        print("\n=== FIFO Page Replacement Simulator ===")
        print("1. Run FIFO algorithm")
        print("2. Exit")
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == "1":
            pages, frames_count = get_input()
            if pages is None:
                continue
            run_fifo(pages, frames_count)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1 or 2.")

if __name__ == "__main__":
    main_menu()