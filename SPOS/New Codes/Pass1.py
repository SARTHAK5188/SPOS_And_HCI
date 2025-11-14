
# pass1.py
# Standalone Pass-I for the pseudo-machine two-pass assembler.
# Produces and prints SYMTAB and intermediate code (no file I/O).

# OPTAB and directives (same as your original)
OPTAB = {
    "LOAD": "01",
    "STORE": "02",
    "ADD": "03",
    "SUB": "04",
    "JMP": "05"
}

DIRECTIVES = ["START", "END", "WORD", "RESW", "RESB"]

# Symbol Table (SYMTAB) and Intermediate Code (intermediate_code)
SYMTAB = {}
intermediate_code = []

# Parse a line of input (splits line into label, opcode, operand)
def parse_line(line):
    parts = line.split()
    label = parts[0] if len(parts) == 3 else None
    opcode = parts[1] if len(parts) == 3 else parts[0]
    operand = parts[2] if len(parts) == 3 else parts[1] if len(parts) == 2 else None
    return label, opcode, operand

# Pass-I: Generates the symbol table and intermediate code
def pass1(input_lines):
    locctr = 0
    start_address = 0
    for line in input_lines:
        # preserve original behavior: strip only newline/outer spaces
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

# Main (example usage)
def main():
    # Provide assembly code directly here (same sample you gave)
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
    start_address, inter = pass1(input_lines)

    # Display Symbol Table and Intermediate Code
    print("\nPass-I Output:")
    print("Symbol Table (SYMTAB):", SYMTAB)
    print("\nIntermediate Code:")
    for entry in intermediate_code:
        print(entry)

    return start_address

if __name__ == "__main__":
    main()
