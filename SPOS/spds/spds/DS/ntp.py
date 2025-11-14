import sys

def manual_ntp_calculation(t1, t2, t3, t4):
    """
    Perform NTP offset and delay calculations using user-entered timestamps.
    NTP Formulas:
      Offset (θ) = ((t2 - t1) + (t3 - t4)) / 2
      Delay  (δ) = (t4 - t1) - (t3 - t2)
    """
    theta = ((t2 - t1) + (t3 - t4)) / 2.0
    delta = (t4 - t1) - (t3 - t2)
    adjusted_local_time = t4 + theta
    return adjusted_local_time, theta, delta


try:
    t1 = float(input("Enter t1 (client send time): ").strip())
    t2 = float(input("Enter t2 (server receive time): ").strip())
    t3 = float(input("Enter t3 (server send time): ").strip())
    t4 = float(input("Enter t4 (client receive time): ").strip())
except ValueError:
    print("\nInvalid input! Please enter numeric values only.")
    sys.exit(1)

# Validate timestamp order (relaxed for real-world conditions)
if t2 > t3:
    print("\nInvalid: Server transmit time (t3) cannot be before server receive time (t2).")
    sys.exit(1)
if t1 >= t4:
    print("\nInvalid: Client receive time (t4) must be after client send time (t1).")
    sys.exit(1)

# Perform calculation
adjusted_local_time, offset, delay = manual_ntp_calculation(t1, t2, t3, t4)

# Display results (numeric only — no date strings)
print("\n=== RESULTS ===")
print(f"Adjusted local time (seconds): {adjusted_local_time:.6f}")
print(f"Offset (θ) in seconds: {offset:.6f}")
print(f"Round-trip delay (δ) in seconds: {delay:.6f}")

# Interpret offset
if offset > 0:
    print(f"Interpretation: Client clock is BEHIND the server by {offset:.6f} seconds.")
elif offset < 0:
    print(f"Interpretation: Client clock is AHEAD of the server by {abs(offset):.6f} seconds.")
else:
    print("Interpretation: Client and server clocks are perfectly synchronized.")

print("\nCorrected timestamps (raw + offset) in seconds:")
print(f"t1 corrected: {t1 + offset:.6f}")
print(f"t2 corrected: {t2 + offset:.6f}")
print(f"t3 corrected: {t3 + offset:.6f}")
print(f"t4 corrected: {t4 + offset:.6f}")

print("\nNote: This output uses numeric timestamps only (no human-readable date/time strings).")
