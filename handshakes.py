def count_handshakes(inputs):
    results = []
    for diplomats in inputs:
        total_handshakes = 0
        for i in range(len(diplomats)):
            daily_handshakes = 0
            for j in range(i, len(diplomats)):
                if diplomats[j] == diplomats[j - i]:
                    daily_handshakes += 1
                else:
                    break
            total_handshakes += daily_handshakes
        results.append(total_handshakes)
    return results

print(count_handshakes(["ababaa"]))