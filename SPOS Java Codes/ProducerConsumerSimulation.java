import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

class Synchronization {
    private final BlockingQueue<Integer> buffer;
    private volatile boolean producerActive;
    private volatile boolean consumerActive;
    private final Random random;

    public Synchronization() {
        this.buffer = new ArrayBlockingQueue<>(10);
        this.producerActive = false;
        this.consumerActive = false;
        this.random = new Random();
    }

    // ---------- PRODUCER ----------
    public void startProducer() {
        if (consumerActive) {
            System.out.println("Cannot start Producer while Consumer is active!");
            return;
        }
        if (producerActive) {
            System.out.println("Producer already running!");
            return;
        }

        producerActive = true;
        System.out.println("\1nProducer started.");

        Thread producerThread = new Thread(() -> {
            while (producerActive) {
                try {
                    int data = random.nextInt(100);
                    buffer.put(data); // Automatically waits if buffer is full
                    System.out.println("Produced: " + data);
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
            System.out.println("Producer stopped.");
        });
        producerThread.start();
    }

    public void stopProducer() {
        if (!producerActive) {
            System.out.println("Producer is not running!");
            return;
        }
        producerActive = false;
    }

    // ---------- CONSUMER ----------
    public void startConsumer() {
        if (producerActive) {
            System.out.println("Cannot start Consumer while Producer is active!");
            return;
        }
        if (consumerActive) {
            System.out.println("Consumer already running!");
            return;
        }

        consumerActive = true;
        System.out.println("Consumer started.");

        Thread consumerThread = new Thread(() -> {
            while (consumerActive) {
                try {
                    int data = buffer.take(); // Automatically waits if buffer is empty
                    System.out.println("Consumed: " + data);
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
            System.out.println("Consumer stopped.");
        });
        consumerThread.start();
    }

    public void stopConsumer() {
        if (!consumerActive) {
            System.out.println("Consumer is not running!");
            return;
        }
        consumerActive = false;
    }
}

public class ProducerConsumerSimulation {
    public static void main(String[] args) {
        Synchronization s = new Synchronization();
        Scanner scanner = new Scanner(System.in);
        int choice;

        System.out.println("\n--- Producer-Consumer Problem Simulation ---");

        do {
            System.out.println("\n1. Start Producer");
            System.out.println("2. Stop Producer");
            System.out.println("3. Start Consumer");
            System.out.println("4. Stop Consumer");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    s.startProducer();
                    break;
                case 2:
                    s.stopProducer();
                    break;
                case 3:
                    s.startConsumer();
                    break;
                case 4:
                    s.stopConsumer();
                    break;
                case 5:
                    System.out.println("Exiting simulation...");
                    break;
                default:
                    System.out.println("Invalid choice!");
            }
        } while (choice < 6);

        scanner.close();
    }
}