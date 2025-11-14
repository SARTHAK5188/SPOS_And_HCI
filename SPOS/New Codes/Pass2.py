# Example Opcode Table (OPTAB)
OPTAB = {
    "LOAD": "01",
    "STORE": "02",
    "ADD": "03",
    "SUB": "04",
    "JMP": "05"
}

# Example Assembler Directives
DIRECTIVES = ["START", "END", "WORD", "RESW", "RESB"]

# Symbol Table (SYMTAB) and Intermediate Code
SYMTAB = {}
intermediate_code = []

# Pass-I: Generates the symbol table and intermediate code
def pass1(input_lines):
    locctr = 0
    start_address = 0
    for line in input_lines:
        label, opcode, operand = parse_line(line.strip())

        if opcode == "START":
            start_address = int(operand)
            locctr = start_address
            intermediate_code.append((locctr, label, opcode, operand))
            continue

        # Process label
        if label:
            if label in SYMTAB:
                print(f"Error: Duplicate symbol {label}")
            SYMTAB[label] = locctr

        # Process opcode
        if opcode in OPTAB:
            intermediate_code.append((locctr, label, opcode, operand))
            locctr += 3 # Assume all instructions are 3 bytes
        elif opcode in DIRECTIVES:
            if opcode == "WORD":
                intermediate_code.append((locctr, label, opcode, operand))
                locctr += 3
            elif opcode == "RESW":
                intermediate_code.append((locctr, label, opcode, operand))
                locctr += 3 * int(operand)
            elif opcode == "RESB":
                intermediate_code.append((locctr, label, opcode, operand))
                locctr += int(operand)
            elif opcode == "END":
                intermediate_code.append((locctr, label, opcode, operand))
                break
        else:
            print(f"Error: Invalid opcode {opcode}")

    return start_address, intermediate_code

# Parse a line of input (splits line into label, opcode, operand)
def parse_line(line):
    parts = line.split()
    label = parts[0] if len(parts) == 3 else None
    opcode = parts[1] if len(parts) == 3 else parts[0]
    operand = parts[2] if len(parts) == 3 else parts[1] if len(parts) == 2 else None
    return label, opcode, operand

# Pass-II: Generates the final machine code (in DECIMAL format)
def pass2(start_address, intermediate_code):
    final_code = []
    for locctr, label, opcode, operand in intermediate_code:
        if opcode in OPTAB:
            machine_code = int(OPTAB[opcode], 16)  # Convert hex opcode to decimal
            if operand in SYMTAB:
                address = SYMTAB[operand]           # Use decimal address directly
            else:
                address = 0
            final_code.append(f"{locctr:04d} {machine_code:02d} {address:04d}")
        elif opcode == "WORD":
            final_code.append(f"{locctr:04d} {int(operand):06d}")
        elif opcode == "RESW" or opcode == "RESB":
            final_code.append(f"{locctr:04d} ----")
        elif opcode == "END":
            final_code.append(f"{locctr:04d} END")
    return final_code

# Main function (NO external file required)
def main():
    # Provide assembly code directly here
    input_lines = [
        "COPY START 1000",
        "FIRST LOAD ALPHA",
        " ADD BETA",
        " STORE GAMMA",
        "ALPHA WORD 5",
        "BETA WORD 10",
        "GAMMA RESW 1",
        " END FIRST"
    ]

    # Run Pass-I
    start_address, intermediate_code = pass1(input_lines)

    # Display Symbol Table and Intermediate Code
    print("\nPass-I Output:")
    print("Symbol Table (SYMTAB):", SYMTAB)
    print("\nIntermediate Code:")
    for entry in intermediate_code:
        print(entry)

    # Run Pass-II
    final_code = pass2(start_address, intermediate_code)

    # Display Final Machine Code (DECIMAL)
    print("\nPass-II Output (Final Machine Code - DECIMAL):")
    for code in final_code:
        print(code)

# Run the main function
if __name__ == "__main__":
    main()

"""This is a two-pass assembler simulator written in Python.

In very simple words:

You have an assembly language program — human-readable instructions like:

LOAD ALPHA
ADD BETA
STORE GAMMA


An assembler converts this human-readable program into machine code — numbers the computer understands.

So what are “two passes”?

The assembler does this in two rounds:

Pass	What it does	Why it’s needed
Pass-I	Reads the source code line by line and records where each label is located (builds a symbol table).	So later we know the address of every label (like variables).
Pass-II	Uses the symbol table to convert each instruction into final machine code (numbers).	Because now we know all addresses.

Example:

ALPHA WORD 5   -> stores 5 at address 1009
LOAD ALPHA     -> becomes something like "opcode for LOAD + 1009"

🧠 Let’s decode the main parts

I’ll go piece by piece, but keep it plain-language.

🧩 1. The Opcode Table (OPTAB)
OPTAB = {
    "LOAD": "01",
    "STORE": "02",
    "ADD": "03",
    "SUB": "04",
    "JMP": "05"
}


Think of this like a mini dictionary that tells the computer:

“When you see the word LOAD, it means instruction number 01.”

So:

LOAD → 01

STORE → 02

ADD → 03

SUB → 04

JMP → 05

These numbers are the machine codes for each operation.

🧩 2. The Directives
DIRECTIVES = ["START", "END", "WORD", "RESW", "RESB"]


These are not real instructions — they’re commands for the assembler, not the CPU.

Directive	Meaning
START	Marks where the program begins
END	Marks where it ends
WORD	Store a 3-byte constant (a number)
RESW	Reserve a number of words (for variables)
RESB	Reserve bytes (for small memory chunks)
🧩 3. The Symbol Table (SYMTAB)
SYMTAB = {}


Think of SYMTAB as a list of all variable names (labels) and their memory addresses.

Example after Pass-I:

SYMTAB = {
  "ALPHA": 1009,
  "BETA": 1012,
  "GAMMA": 1015
}


It’s how the assembler remembers where each variable or label is stored in memory.

🧩 4. The Location Counter (LOCCTR)

Inside the program, you’ll see:

locctr = start_address


LOCCTR = “Location Counter.”
It tells the assembler which memory address it’s currently on while reading instructions.

Every time you process an instruction, you increase it (because each instruction takes space in memory).

Example:

START 1000   → locctr = 1000
LOAD ALPHA   → locctr = 1003 (added 3 bytes)
ADD BETA     → locctr = 1006

🧩 5. The Intermediate Code

This is like the assembler’s scratch notebook — where it records what it has read so far.

Each line looks like:

(1000, 'FIRST', 'LOAD', 'ALPHA')


That means:

Address 1000

Label = FIRST

Opcode = LOAD

Operand = ALPHA

This helps Pass-II later when it generates final code.

⚙️ What happens step by step (Pass-I)

Imagine your input program:

COPY START 1000
FIRST LOAD ALPHA
 ADD BETA
 STORE GAMMA
ALPHA WORD 5
BETA WORD 10
GAMMA RESW 1
 END FIRST


Now let’s trace what happens.

Step 1: See COPY START 1000

→ This means: program starts at address 1000
So:

start_address = 1000
locctr = 1000

Step 2: FIRST LOAD ALPHA

Label: FIRST

Opcode: LOAD

Operand: ALPHA
→ Adds FIRST to symbol table with address 1000
→ Writes to intermediate code (1000, 'FIRST', 'LOAD', 'ALPHA')
→ Increases locctr by 3 → becomes 1003

Step 3: ADD BETA

→ No label
→ Writes (1003, None, 'ADD', 'BETA')
→ locctr = 1006

Step 4: STORE GAMMA

→ (1006, None, 'STORE', 'GAMMA')
→ locctr = 1009

Step 5: ALPHA WORD 5

→ label = ALPHA, opcode = WORD, operand = 5
→ Adds ALPHA = 1009 to SYMTAB
→ locctr = 1012

Step 6: BETA WORD 10

→ Adds BETA = 1012
→ locctr = 1015

Step 7: GAMMA RESW 1

→ Adds GAMMA = 1015
→ “Reserve 1 word” = 3 bytes
→ locctr = 1018

Step 8: END FIRST

→ End of program
→ Stops Pass-I.

✅ After Pass-I

Symbol table (SYMTAB):

{'FIRST': 1000, 'ALPHA': 1009, 'BETA': 1012, 'GAMMA': 1015}


Intermediate code:

(1000, 'COPY', 'START', '1000')
(1000, 'FIRST', 'LOAD', 'ALPHA')
(1003, None, 'ADD', 'BETA')
(1006, None, 'STORE', 'GAMMA')
(1009, 'ALPHA', 'WORD', '5')
(1012, 'BETA', 'WORD', '10')
(1015, 'GAMMA', 'RESW', '1')
(1018, None, 'END', 'FIRST')

⚙️ What happens in Pass-II

Pass-II takes that intermediate code and symbol table, and produces machine code.

Step 1: Go line by line

Line 1: START → ignored for machine code
Line 2: LOAD ALPHA

LOAD opcode = "01" → decimal 1

ALPHA address = 1009
→ Output: 1000 1 1009

Line 3: ADD BETA

Opcode "03" → decimal 3

BETA address = 1012
→ Output: 1003 3 1012

Line 4: STORE GAMMA

Opcode "02" → decimal 2

GAMMA address = 1015
→ Output: 1006 2 1015

Line 5: ALPHA WORD 5
→ Output: 1009 5

Line 6: BETA WORD 10
→ Output: 1012 10

Line 7: GAMMA RESW 1
→ Reserved memory → Output: 1015 ----

Line 8: END FIRST
→ Output: 1018 END

✅ Final machine code (in decimal)
1000  1  1009
1003  3  1012
1006  2  1015
1009  5
1012  10
1015  ----
1018  END


This is the “machine code” your assembler generated.

🧾 Quick summary in plain English
Step	What happens	Example
Pass 1	Reads program, builds symbol table & intermediate code	ALPHA = 1009
Pass 2	Converts everything into machine code using addresses from SYMTAB	LOAD ALPHA → 1 1009
SYMTAB	Keeps label → address mapping	{‘BETA’: 1012, ...}
Intermediate code	Keeps line info for second pass	(1003, None, 'ADD', 'BETA')
Final code	Machine code in decimal	1003 3 1012
💡 How to explain it in your practical exam

If your examiner asks:

“Explain what your assembler does.”

You can say:

“My program is a simple two-pass assembler.
In the first pass, it builds a symbol table that stores the addresses of all labels.
In the second pass, it uses that table to generate machine code in decimal form.
Each instruction in my program is assumed to be 3 bytes long, and assembler directives like START, WORD, RESW, and END are also handled.”

If they ask:

“What are the data structures used?”

You answer:

OPTAB → Dictionary for opcodes

SYMTAB → Dictionary for symbols

intermediate_code → List to store temporary output

If they ask:

“Why do we need two passes?”

You answer:

Because sometimes labels are used before they are defined.
The assembler needs one pass to find all label addresses (Pass-I), and the second to replace label names with their addresses (Pass-II).

Now you can confidently explain your code line by line in your practical"""