def accept():
    global no_of_blocks, no_of_processes, blocks, processes
    no_of_blocks = int(input("Enter no. of blocks : "))
    blocks = [int(input(f"Enter block size for b{i+1} : ")) for i in range(no_of_blocks)]
    print()
    
    no_of_processes = int(input("Enter no. of Processes or Files : "))
    processes = [int(input(f"Enter Process or File size for P{i+1} : ")) for i in range(no_of_processes)]

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
            temp_blocks[worst_block_index] -= processes[i]  # reduce block by allocated size
        else:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")
    print("-" * 50)

def menu():
    """
    Simple menu-driven interface. You can:
      1 - Enter input (calls accept)
      2 - Run Worst Fit
      3 - Exit
    """
    while True:
        print("\nMenu:")
        print("1. Enter blocks and processes (accept)")
        print("2. Worst Fit")
        print("3. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            accept()
        elif choice == "2":
            try:
                worst_fit()
            except NameError:
                print("Error: Please enter blocks and processes first (choose option 1).")
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 7.")

if __name__ == "__main__":
    menu()
