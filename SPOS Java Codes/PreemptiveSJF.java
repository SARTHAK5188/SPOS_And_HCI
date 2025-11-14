import java.util.*;

public class PreemptiveSJF {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] pid = new int[n]; // Process IDs
        int[] arrival = new int[n]; // Arrival times
        int[] burst = new int[n]; // Burst times
        int[] remaining = new int[n]; // Remaining burst times
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
            remaining[i] = burst[i];
            pid[i] = i + 1;
            completed[i] = false;
        }

        int currentTime = 0;
        int totalCompleted = 0;

        // Preemptive SJF scheduling
        while (totalCompleted < n) {
            int shortestJob = -1;
            int shortestTime = Integer.MAX_VALUE;

            // Find process with shortest remaining time that has arrived
            for (int i = 0; i < n; i++) {
                if (arrival[i] <= currentTime && !completed[i] && remaining[i] < shortestTime) {
                    shortestTime = remaining[i];
                    shortestJob = i;
                }
            }

            if (shortestJob == -1) {
                // No process available, move time forward
                currentTime++;
            } else {
                // Execute the shortest job for 1 unit of time
                remaining[shortestJob]--;
                currentTime++;

                // Check if process completed
                if (remaining[shortestJob] == 0) {
                    completion[shortestJob] = currentTime;
                    completed[shortestJob] = true;
                    totalCompleted++;
                }
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