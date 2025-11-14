import java.util.*;

public class NonPreemptivePriority {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] pid = new int[n]; // Process IDs
        int[] arrival = new int[n]; // Arrival times
        int[] burst = new int[n]; // Burst times
        int[] priority = new int[n]; // Priorities (lower number = higher priority)
        int[] completion = new int[n]; // Completion times
        int[] turnaround = new int[n]; // Turnaround times
        int[] waiting = new int[n]; // Waiting times
        boolean[] completed = new boolean[n]; // Completion status

        // Input process details
        for (int i = 0; i < n; i++) {
            System.out.print("Enter arrival time for process " + (i + 1) + ": ");
            arrival[i] = sc.nextInt();
            System.out.print("Enter burst time for process " + (i + 1) + ": ");
            burst[i] = sc.nextInt();
            System.out.print("Enter priority for process " + (i + 1) + " (lower number = higher priority): ");
            priority[i] = sc.nextInt();
            pid[i] = i + 1;
            completed[i] = false;
        }

        int currentTime = 0;
        int totalCompleted = 0;

        // Non-preemptive Priority scheduling
        while (totalCompleted < n) {
            int highestPriority = Integer.MAX_VALUE;
            int selectedProcess = -1;

            // Find process with highest priority (lowest number) that has arrived
            for (int i = 0; i < n; i++) {
                if (arrival[i] <= currentTime && !completed[i] && priority[i] < highestPriority) {
                    highestPriority = priority[i];
                    selectedProcess = i;
                }
            }

            if (selectedProcess == -1) {
                // No process available, move time forward
                currentTime++;
            } else {
                // Execute the selected process to completion (non-preemptive)
                currentTime += burst[selectedProcess];
                completion[selectedProcess] = currentTime;
                completed[selectedProcess] = true;
                totalCompleted++;
            }
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
        System.out.println("PID\tArrival\tBurst\tPriority\tCompletion\tTurnaround\tWaiting");
        for (int i = 0; i < n; i++) {
            System.out.printf("%d\t%d\t%d\t%d\t\t%d\t\t%d\t\t%d\n",
                    pid[i], arrival[i], burst[i], priority[i], completion[i], turnaround[i], waiting[i]);
        }

        System.out.printf("\nAverage Turnaround Time: %.2f\n", (avgTurnaround / n));
        System.out.printf("Average Waiting Time: %.2f\n", (avgWait / n));

        sc.close();
    }
}