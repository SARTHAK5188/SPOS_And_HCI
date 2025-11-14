import java.util.Arrays;

public class NextFit {
    private int[] memoryBlocks;
    private int[] processSizes;

    public NextFit(int[] blocks, int[] processes) {
        this.memoryBlocks = Arrays.copyOf(blocks, blocks.length);
        this.processSizes = Arrays.copyOf(processes, processes.length);
    }

    public void allocateMemory() {
        System.out.println("\n=== NEXT FIT MEMORY ALLOCATION ===");
        System.out.println("Initial Memory Blocks: " + Arrays.toString(memoryBlocks));
        System.out.println("Process Sizes: " + Arrays.toString(processSizes));
        System.out.println("\nAllocation Process:");

        boolean[] allocated = new boolean[processSizes.length];
        int[] allocation = new int[processSizes.length];
        Arrays.fill(allocation, -1);

        int lastAllocatedBlock = 0; // Start from first block

        for (int i = 0; i < processSizes.length; i++) {
            boolean allocatedCurrent = false;
            int startPoint = lastAllocatedBlock;

            // Search from last allocated position
            for (int j = 0; j < memoryBlocks.length; j++) {
                int currentBlock = (startPoint + j) % memoryBlocks.length;

                if (memoryBlocks[currentBlock] >= processSizes[i]) {
                    allocation[i] = currentBlock;
                    memoryBlocks[currentBlock] -= processSizes[i];
                    allocated[i] = true;
                    lastAllocatedBlock = (currentBlock + 1) % memoryBlocks.length;
                    allocatedCurrent = true;

                    System.out.println("Process " + (i + 1) + " (" + processSizes[i] +
                            " KB) allocated to Block " + (currentBlock + 1) +
                            " (Next Fit). Remaining: " + memoryBlocks[currentBlock] + " KB");
                    break;
                }
            }

            if (!allocatedCurrent) {
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

        NextFit manager = new NextFit(memoryBlocks, processes);
        manager.allocateMemory();
    }
}