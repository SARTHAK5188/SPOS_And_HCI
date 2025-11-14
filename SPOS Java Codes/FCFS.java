import java.util.*;

public class FCFS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] pid = new int[n]; // Process IDs
        int[] arrival = new int[n]; // Arrival times
        int[] burst = new int[n]; // Burst times
        int[] completion = new int[n]; // Completion times
        int[] turnaround = new int[n]; // Turnaround times
        int[] waiting = new int[n]; // Waiting times

        // Input process details
        for (int i = 0; i < n; i++) {
            System.out.print("Enter arrival time for process " + (i + 1) + ": ");
            arrival[i] = sc.nextInt();
            System.out.print("Enter burst time for process " + (i + 1) + ": ");
            burst[i] = sc.nextInt();
            pid[i] = i + 1;
        }

        // Sort processes by arrival time (FCFS)
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arrival[j] > arrival[j + 1]) {
                    // Swap arrival times
                    int temp = arrival[j];
                    arrival[j] = arrival[j + 1];
                    arrival[j + 1] = temp;

                    // Swap burst times
                    temp = burst[j];
                    burst[j] = burst[j + 1];
                    burst[j + 1] = temp;

                    // Swap process IDs
                    temp = pid[j];
                    pid[j] = pid[j + 1];
                    pid[j + 1] = temp;
                }
            }
        }

        // Calculate completion times
        int currentTime = 0;
        for (int i = 0; i < n; i++) {
            if (currentTime < arrival[i]) {
                currentTime = arrival[i];
            }
            completion[i] = currentTime + burst[i];
            currentTime = completion[i];
        }

        // Calculate turnaround and waiting times
        float avgWait = 0, avgTurnaround = 0;
        for (int i = 0; i < n; i++) {
            turnaround[i] = completion[i] - arrival[i];
            waiting[i] = turnaround[i] - burst[i];
            avgWait += waiting[i];
            avgTurnaround += turnaround[i];
        }

        // Display results
        System.out.println("\nProcess Table:");
        System.out.println("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting");
        for (int i = 0; i < n; i++) {
            System.out.printf("%d\t%d\t%d\t%d\t\t%d\t\t%d\n",
                    pid[i], arrival[i], burst[i], completion[i], turnaround[i], waiting[i]);
        }

        System.out.printf("\nAverage Turnaround Time: %.2f\n", (avgTurnaround / n));
        System.out.printf("Average Waiting Time: %.2f\n", (avgWait / n));

        sc.close();
    }
}