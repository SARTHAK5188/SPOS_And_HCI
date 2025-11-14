import java.util.Arrays;

public class WorstFit {
    private int[] memoryBlocks;
    private int[] processSizes;

    public WorstFit(int[] blocks, int[] processes) {
        this.memoryBlocks = Arrays.copyOf(blocks, blocks.length);
        this.processSizes = Arrays.copyOf(processes, processes.length);
    }

    public void allocateMemory() {
        System.out.println("\n=== WORST FIT MEMORY ALLOCATION ===");
        System.out.println("Initial Memory Blocks: " + Arrays.toString(memoryBlocks));
        System.out.println("Process Sizes: " + Arrays.toString(processSizes));
        System.out.println("\nAllocation Process:");

        boolean[] allocated = new boolean[processSizes.length];
        int[] allocation = new int[processSizes.length];
        Arrays.fill(allocation, -1);

        for (int i = 0; i < processSizes.length; i++) {
            int worstBlock = -1;
            int worstRemaining = -1;

            // Find the worst fit block (largest sufficient block)
            for (int j = 0; j < memoryBlocks.length; j++) {
                if (memoryBlocks[j] >= processSizes[i]) {
                    int remaining = memoryBlocks[j] - processSizes[i];
                    if (remaining > worstRemaining) {
                        worstRemaining = remaining;
                        worstBlock = j;
                    }
                }
            }

            if (worstBlock != -1) {
                allocation[i] = worstBlock;
                memoryBlocks[worstBlock] -= processSizes[i];
                allocated[i] = true;
                System.out.println("Process " + (i + 1) + " (" + processSizes[i] +
                        " KB) allocated to Block " + (worstBlock + 1) +
                        " (Worst Fit). Remaining: " + memoryBlocks[worstBlock] + " KB");
            } else {
                System.out.println("Process " + (i + 1) + " (" + processSizes[i] +
                        " KB) could not be allocated - No suitable block found");
            }
        }

        printFinalStatus(allocation);
    }

    private void printFinalStatus(int[] allocation) {
        System.out.println("\n=== FINAL STATUS ===");
        System.out.println("Process Allocation Results:");
        for (int i = 0; i < processSizes.length; i++) {
            if (allocation[i] != -1) {
                System.out.println("Process " + (i + 1) + " -> Block " + (allocation[i] + 1));
            } else {
                System.out.println("Process " + (i + 1) + " -> Not Allocated");
            }
        }

        System.out.println("\nRemaining Memory Blocks:");
        for (int i = 0; i < memoryBlocks.length; i++) {
            System.out.println("Block " + (i + 1) + ": " + memoryBlocks[i] + " KB free");
        }
    }

    public static void main(String[] args) {
        int[] memoryBlocks = { 100, 500, 200, 300, 600 };
        int[] processes = { 212, 417, 112, 426 };

        WorstFit manager = new WorstFit(memoryBlocks, processes);
        manager.allocateMemory();
    }
}