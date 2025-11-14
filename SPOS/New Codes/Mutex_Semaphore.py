''' Write a program to solve Classical Problems of Synchronization using Mutex
and Semaphore.
'''

class Synchronization:
    def __init__(self):
        self.buffer = [0] * 10  # Buffer size 10
        self.mutex = 1
        self.empty = 10
        self.full = 0
        self.in_index = 0
        self.out_index = 0

    def wait(self, x):
        if x > 0:
            return x - 1
        return x

    def signal(self, x):
        return x + 1

    def producer(self):
        if self.empty > 0 and self.mutex == 1:
            self.empty = self.wait(self.empty)
            self.mutex = self.wait(self.mutex)
            data = int(input("Data to be produced: "))
            self.buffer[self.in_index] = data
            self.in_index = (self.in_index + 1) % 10
            self.mutex = self.signal(self.mutex)
            self.full = self.signal(self.full)
        else:
            print("Buffer is full, cannot produce!")

    def consumer(self):
        if self.full > 0 and self.mutex == 1:
            self.full = self.wait(self.full)
            self.mutex = self.wait(self.mutex)
            print("Data consumed is:", self.buffer[self.out_index])
            self.out_index = (self.out_index + 1) % 10
            self.mutex = self.signal(self.mutex)
            self.empty = self.signal(self.empty)
        else:
            print("Buffer is empty, cannot consume!")

def main():
    sync = Synchronization()
    while True:
        print("\n1. Producer\n2. Consumer\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            sync.producer()
        elif choice == '2':
            sync.consumer()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()


