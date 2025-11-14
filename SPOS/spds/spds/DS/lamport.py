def initialize_clock(process_id):
    return 0

def event(clock):
    clock += 1
    return clock

def send_message(clock):
    clock += 1
    return clock, clock

def receive_message(local_clock, received_timestamp):
    local_clock = max(local_clock, received_timestamp) + 1
    return local_clock

if __name__ == '__main__':
    # Initial clocks for three processes
    p1_clock = initialize_clock(1)
    p2_clock = initialize_clock(2)
    p3_clock = initialize_clock(3)

    # --- Process 1 events ---
    p1_clock = event(p1_clock)
    print(f"P1: Internal event. Clock = {p1_clock}")

    p1_clock, timestamp_p1_to_p2 = send_message(p1_clock)
    print(f"P1: Sends message to P2. Clock = {p1_clock}, Timestamp = {timestamp_p1_to_p2}")

    # --- Process 2 events ---
    p2_clock = event(p2_clock)
    print(f"P2: Internal event. Clock = {p2_clock}")

    # P2 receives message from P1
    p2_clock = receive_message(p2_clock, timestamp_p1_to_p2)
    print(f"P2: Receives message from P1. Clock = {p2_clock}")

    p2_clock, timestamp_p2_to_p3 = send_message(p2_clock)
    print(f"P2: Sends message to P3. Clock = {p2_clock}, Timestamp = {timestamp_p2_to_p3}")

    # --- Process 3 events ---
    p3_clock = event(p3_clock)
    print(f"P3: Internal event. Clock = {p3_clock}")

    # P3 receives message from P2
    p3_clock = receive_message(p3_clock, timestamp_p2_to_p3)
    print(f"P3: Receives message from P2. Clock = {p3_clock}")