def accept():
    global no_of_blocks, no_of_processes, blocks, processes
    no_of_blocks = int(input("Enter no. of blocks : "))
    blocks = [int(input(f"Enter block size for b{i+1} : ")) for i in range(no_of_blocks)]
    print()
    no_of_processes = int(input("Enter no. of Processes or Files : "))
    processes = [int(input(f"Enter Process or File size for P{i+1} : ")) for i in range(no_of_processes)]

def first_fit():
    print("\n----- FIRST FIT -----")
    print("File No.\tFile Size\tBlock No.\tBlock Size\tFragment")
    temp_blocks = list(blocks)
    for i in range(no_of_processes):
        allocated = False
        for j in range(no_of_blocks):
            if processes[i] <= temp_blocks[j]:
                fragment = temp_blocks[j] - processes[i]
                print(f"{i+1}\t\t{processes[i]}\t\t{j+1}\t\t{temp_blocks[j]}\t\t{fragment}")
                temp_blocks[j] -= processes[i]
                allocated = True
                break
        if not allocated:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")
    print("-" * 50)

def best_fit():
    print("\n----- BEST FIT -----")
    print("File No.\tFile Size\tBlock No.\tBlock Size\tFragment")
    temp_blocks = list(blocks)
    for i in range(no_of_processes):
        best_block_index = -1
        for j in range(no_of_blocks):
            if processes[i] <= temp_blocks[j]:
                if best_block_index == -1 or temp_blocks[j] < temp_blocks[best_block_index]:
                    best_block_index = j
        if best_block_index != -1:
            fragment = temp_blocks[best_block_index] - processes[i]
            print(f"{i+1}\t\t{processes[i]}\t\t{best_block_index+1}\t\t{temp_blocks[best_block_index]}\t\t{fragment}")
            temp_blocks[best_block_index] -= processes[i]
        else:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")
    print("-" * 50)

def worst_fit():
    print("\n----- WORST FIT -----")
    print("File No.\tFile Size\tBlock No.\tBlock Size\tFragment")
    temp_blocks = list(blocks)
    for i in range(no_of_processes):
        worst_block_index = -1
        for j in range(no_of_blocks):
            if processes[i] <= temp_blocks[j]:
                if worst_block_index == -1 or temp_blocks[j] > temp_blocks[worst_block_index]:
                    worst_block_index = j
        if worst_block_index != -1:
            fragment = temp_blocks[worst_block_index] - processes[i]
            print(f"{i+1}\t\t{processes[i]}\t\t{worst_block_index+1}\t\t{temp_blocks[worst_block_index]}\t\t{fragment}")
            temp_blocks[worst_block_index] -= processes[i]
        else:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")
    print("-" * 50)

def next_fit():
    print("\n----- NEXT FIT (MODIFIED) -----")
    print("File No.\tFile Size\tBlock No.\tBlock Size\tFragment")
    temp_blocks = list(blocks)
    last_allocated_index = 0
    for i in range(no_of_processes):
        allocated = False
        for j in range(no_of_blocks):
            current_index = (last_allocated_index + j) % no_of_blocks
            if processes[i] <= temp_blocks[current_index]:
                fragment = temp_blocks[current_index] - processes[i]
                print(f"{i+1}\t\t{processes[i]}\t\t{current_index+1}\t\t{temp_blocks[current_index]}\t\t{fragment}")
                temp_blocks[current_index] -= processes[i]
                last_allocated_index = (current_index + 1) % no_of_blocks
                allocated = True
                break
        if not allocated:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")
    print("-" * 50)

def menu():
    """
    Simple menu-driven interface:
      1 - Enter input (accept)
      2 - First Fit
      3 - Best Fit
      4 - Worst Fit
      5 - Next Fit
      6 - Run All (First, Best, Worst, Next)
      7 - Exit
    """
    while True:
        print("\nMenu:")
        print("1. Enter blocks and processes (accept)")
        print("2. First Fit")
        print("3. Best Fit")
        print("4. Worst Fit")
        print("5. Next Fit")
        print("6. Run All (First, Best, Worst, Next)")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            try:
                accept()
            except Exception as e:
                print("Input error:", e)
        elif choice == "2":
            try:
                first_fit()
            except NameError:
                print("Error: Please enter blocks and processes first (choose option 1).")
        elif choice == "3":
            try:
                best_fit()
            except NameError:
                print("Error: Please enter blocks and processes first (choose option 1).")
        elif choice == "4":
            try:
                worst_fit()
            except NameError:
                print("Error: Please enter blocks and processes first (choose option 1).")
        elif choice == "5":
            try:
                next_fit()
            except NameError:
                print("Error: Please enter blocks and processes first (choose option 1).")
        elif choice == "6":
            try:
                first_fit()
                best_fit()
                worst_fit()
                next_fit()
            except NameError:
                print("Error: Please enter blocks and processes first (choose option 1).")
        elif choice == "7":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 7.")

if __name__ == "__main__":
    menu()