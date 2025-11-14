'''For Y group:
Design suitable data structures and implement Pass-II of a two-pass macroprocessor. The output of Pass-I (MNT, MDT and intermediate code file
without any macro definitions) should be input for Pass-II.
Note: Design data structures according to input given'''

def pass1_macro_processor():
    # Predefined macro code (replace or extend as needed)
    lines = [
        "MACRO",
        "INCR &A",
        "ADD &A, 1",
        "MEND",
        "MACRO",
        "SWAP &X &Y",
        "LOAD &X",
        "STORE TEMP",
        "LOAD &Y",
        "STORE &X",
        "LOAD TEMP",
        "STORE &Y",
        "MEND",
        "START",
        "INCR NUM",
        "SWAP A B",
        "END"
    ]

    mnt = []  # Macro Name Table: [name, MDT index]
    mdt = []  # Macro Definition Table
    ala = {}  # Argument List Array: macro_name -> [#arg1, #arg2, ...]
    intermediate = []

    i = 0
    while i < len(lines):
        if lines[i] == "MACRO":
            macro_header = lines[i + 1]
            parts = macro_header.split()
            macro_name = parts[0]
            args = parts[1:] if len(parts) > 1 else []
            ala[macro_name] = [f"#{j+1}" for j in range(len(args))]
            mnt.append([macro_name, len(mdt)])
            mdt.append(macro_header)

            i += 2
            while lines[i] != "MEND":
                body = lines[i]
                for idx, arg in enumerate(args):
                    body = body.replace(arg, f"#{idx+1}")
                mdt.append(body)
                i += 1
            mdt.append("MEND")
        else:
            intermediate.append(lines[i])
        i += 1

    print("\n--- Pass-I Output ---")
    print("MNT (Macro Name Table):")
    for entry in mnt:
        print(f"Macro: {entry[0]}, MDT Index: {entry[1]}")

    print("\nMDT (Macro Definition Table):")
    for idx, line in enumerate(mdt):
        print(f"{idx}: {line}")

    print("\nALA (Argument List Array):")
    for macro, args in ala.items():
        print(f"{macro}: {args}")

    print("\nIntermediate Code (without macro definitions):")
    for line in intermediate:
        print(line)

    return mnt, mdt, ala, intermediate


def pass2_macro_processor(mnt, mdt, ala, intermediate):
    print("\n--- Pass-II Output (Expanded Code) ---")
    for line in intermediate:
        parts = line.split()
        macro_call = parts[0]
        args = parts[1:] if len(parts) > 1 else []

        found = False
        for entry in mnt:
            if entry[0] == macro_call:
                found = True
                mdt_index = entry[1]
                formal_args = ala[macro_call]
                arg_map = dict(zip(formal_args, args))

                i = mdt_index + 1  # Skip macro header
                while mdt[i] != "MEND":
                    expanded = mdt[i]
                    for key, val in arg_map.items():
                        expanded = expanded.replace(key, val)
                    print(expanded)
                    i += 1
                break
        if not found:
            print(line)


# Run both passes directly
if __name__ == "__main__":
    mnt, mdt, ala, intermediate = pass1_macro_processor()
    pass2_macro_processor(mnt, mdt, ala, intermediate)




'''--- Pass-I Output ---
MNT (Macro Name Table):
Macro: INCR, MDT Index: 0
Macro: SWAP, MDT Index: 3

MDT (Macro Definition Table):
0: INCR &A
1: ADD #1, 1
2: MEND
3: SWAP &X &Y
4: LOAD #1
5: STORE TEMP
6: LOAD #2
7: STORE #1
8: LOAD TEMP
9: STORE #2
10: MEND

ALA (Argument List Array):
INCR: ['#1']
SWAP: ['#1', '#2']

Intermediate Code (without macro definitions):
START
INCR NUM
SWAP A B
END

--- Pass-II Output (Expanded Code) ---
START
ADD NUM, 1
LOAD A
STORE TEMP
LOAD B
STORE A
LOAD TEMP
STORE B
END

=== Code Execution Successful ==='''