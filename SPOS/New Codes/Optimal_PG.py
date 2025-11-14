"""
Optimal Page Replacement (menu driven, simple)
- Enter reference string as space-separated integers
- Enter number of frames (positive integer)
- Program shows frame contents after each reference and total page faults
"""

def run_optimal(pages, frames_count):
    frames = []
    faults = 0

    for i, page in enumerate(pages):
        if page in frames:
            # hit — no change
            print(f"Ref {page:>2} -> Frames: {frames} (hit)")
            continue

        # page fault
        faults += 1
        if len(frames) < frames_count:
            frames.append(page)
            print(f"Ref {page:>2} -> Frames: {frames} (fault, loaded)")
            continue

        # choose a frame to replace:
        # for each page in frames, find its next use index in the future
        # if not used again, its next use is treated as infinity (best to replace)
        next_uses = []
        future = pages[i+1:]
        for f in frames:
            if f in future:
                next_uses.append(future.index(f))
            else:
                next_uses.append(float('inf'))

        # replace the page whose next use is farthest (or never used)
        replace_idx = next_uses.index(max(next_uses))
        replaced = frames[replace_idx]
        frames[replace_idx] = page
        print(f"Ref {page:>2} -> Frames: {frames} (fault, replaced P{replaced})")

    print(f"\nTotal page faults (Optimal): {faults}\n")
    return faults

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
        print("\n=== Optimal Page Replacement Simulator ===")
        print("1. Run Optimal algorithm")
        print("2. Exit")
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == "1":
            pages, frames_count = get_input()
            if pages is None:
                continue
            run_optimal(pages, frames_count)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1 or 2.")

if __name__ == "__main__":
    main_menu()