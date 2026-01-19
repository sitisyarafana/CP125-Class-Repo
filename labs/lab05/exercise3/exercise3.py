
def find_bottleneck_index(traceroute):
    """
    Find the index of the hop where the largest latency jump begins.
    """
    hop_number, latency_in_ms = traceroute[0]
    bottleneck_index = 0
    largest_jumps = 0.0
    for i in range(len(traceroute)-1):
        latency_in_ms = traceroute[i][1]
        nxt_latency_in_ms = traceroute[i+1][1]
        jumps = abs(nxt_latency_in_ms - latency_in_ms)

        if jumps > largest_jumps:
            largest_jumps = jumps
            bottleneck_index = i

    return bottleneck_index




# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
