def accept():
    global no_of_blocks, no_of_processes, blocks, processes
    no_of_blocks = int(input("Enter no. of blocks : "))
    blocks = [int(input(f"Enter block size for b{i+1} : ")) for i in range(no_of_blocks)]
    print()
    
    no_of_processes = int(input("Enter no. of Processes or Files : "))
    processes = [int(input(f"Enter Process or File size for P{i+1} : ")) for i in range(no_of_processes)]

def next_fit():
    print("\n----- NEXT FIT (MODIFIED) -----")
    print("File No.\tFile Size\tBlock No.\tBlock Size\tFragment")
    temp_blocks = list(blocks)
    last_allocated_index = 0
    for i in range(no_of_processes):
        allocated = False
        # The search starts from the last allocated block index
        for j in range(no_of_blocks):
            current_index = (last_allocated_index + j) % no_of_blocks
            if processes[i] <= temp_blocks[current_index]:
                fragment = temp_blocks[current_index] - processes[i]
                print(f"{i+1}\t\t{processes[i]}\t\t{current_index+1}\t\t{temp_blocks[current_index]}\t\t{fragment}")
                temp_blocks[current_index] -= processes[i]  # reduce block by allocated size
                last_allocated_index = (current_index + 1) % no_of_blocks
                allocated = True
                break
        if not allocated:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")
    print("-" * 50)

def menu():
    """
    Simple menu-driven interface. You can:
      1 - Enter input (calls accept)
      2 - Run Next Fit
      7 - Exit
    """
    while True:
        print("\nMenu:")
        print("1. Enter blocks and processes (accept)")
        print("2. Next Fit")
        print("3. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            accept()
        elif choice == "2":
            try:
                next_fit()
            except NameError:
                print("Error: Please enter blocks and processes first (choose option 1).")

        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 7.")

if __name__ == "__main__":
    menu()
