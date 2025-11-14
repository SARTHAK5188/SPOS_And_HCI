import java.util.*;

public class RoundRobin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();
        
        int[] pid = new int[n];      // Process IDs
        int[] arrival = new int[n];  // Arrival times
        int[] burst = new int[n];    // Burst times
        int[] remaining = new int[n]; // Remaining burst times
        int[] completion = new int[n]; // Completion times
        int[] turnaround = new int[n]; // Turnaround times
        int[] waiting = new int[n];   // Waiting times
        
        // Input process details
        for(int i = 0; i < n; i++) {
            System.out.print("Enter arrival time for process " + (i+1) + ": ");
            arrival[i] = sc.nextInt();
            System.out.print("Enter burst time for process " + (i+1) + ": ");
            burst[i] = sc.nextInt();
            remaining[i] = burst[i];
            pid[i] = i + 1;
        }
        
        System.out.print("Enter time quantum: ");
        int quantum = sc.nextInt();
        
        int currentTime = 0;
        int completed = 0;
        
        // Round Robin scheduling
        while(completed < n) {
            boolean executed = false;
            
            for(int i = 0; i < n; i++) {
                // Process is ready and has remaining burst time
                if(arrival[i] <= currentTime && remaining[i] > 0) {
                    executed = true;
                    
                    if(remaining[i] > quantum) {
                        // Execute for quantum time
                        currentTime += quantum;
                        remaining[i] -= quantum;
                    } else {
                        // Process completes execution
                        currentTime += remaining[i];
                        remaining[i] = 0;
                        completed++;
                        completion[i] = currentTime;
                    }
                }
            }
            
            // If no process was executed in this cycle, increment time
            if(!executed) {
                currentTime++;
            }
        }
        
        // Calculate turnaround and waiting times
        float avgWait = 0, avgTurnaround = 0;
        for(int i = 0; i < n; i++) {
            turnaround[i] = completion[i] - arrival[i];
            waiting[i] = turnaround[i] - burst[i];
            avgWait += waiting[i];
            avgTurnaround += turnaround[i];
        }
        
        // Display results
        System.out.println("\nProcess Table:");
        System.out.println("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting");
        for(int i = 0; i < n; i++) {
            System.out.printf("%d\t%d\t%d\t%d\t\t%d\t\t%d\n", 
                pid[i], arrival[i], burst[i], completion[i], turnaround[i], waiting[i]);
        }
        
        System.out.printf("\nAverage Turnaround Time: %.2f\n", (avgTurnaround / n));
        System.out.printf("Average Waiting Time: %.2f\n", (avgWait / n));
        
        sc.close();
    }
}