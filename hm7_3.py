""" Task 3: missed value statues """

statues_now = [6, 2, 3, 8]
statues_should_be = len(range(min(statues_now), max(statues_now) + 1))

print(f"Missed value statues: {statues_should_be - len(statues_now)}")
