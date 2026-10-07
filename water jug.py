from collections import deque

def water_jug(jug1, jug2, target):
    queue = deque()
    visited = set()

    # Start with both jugs empty
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        a, b = queue.popleft()

        print("Jug 1:", a, "Jug 2:", b)

        # Check whether target is reached
        if a == target or b == target:
            print("Target reached!")
            return

        # All possible operations
        states = [
            (jug1, b),                  # Fill Jug 1
            (a, jug2),                  # Fill Jug 2
            (0, b),                     # Empty Jug 1
            (a, 0),                     # Empty Jug 2

            # Pour Jug 1 into Jug 2
            (a - min(a, jug2 - b),
             b + min(a, jug2 - b)),

            # Pour Jug 2 into Jug 1
            (a + min(b, jug1 - a),
             b - min(b, jug1 - a))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No solution exists.")


# Input
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

water_jug(jug1, jug2, target)
