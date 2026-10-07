import heapq

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    """Calculate Manhattan distance."""
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])

            row1, col1 = divmod(i, 3)
            row2, col2 = divmod(goal_pos, 3)

            distance += abs(row1 - row2) + abs(col1 - col2)

    return distance


def get_neighbors(state):
    neighbors = []

    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col

            new_state = list(state)
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


def solve(start):
    priority_queue = []

    # (cost, moves, state, path)
    heapq.heappush(
        priority_queue,
        (heuristic(start), 0, start, [start])
    )

    visited = set()

    while priority_queue:
        cost, moves, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for next_state in get_neighbors(current):
            if next_state not in visited:
                new_moves = moves + 1
                new_cost = new_moves + heuristic(next_state)

                heapq.heappush(
                    priority_queue,
                    (new_cost, new_moves,
                     next_state, path + [next_state])
                )

    return None


def display(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


# Input
print("Enter 9 numbers (use 0 for blank):")
start = tuple(map(int, input().split()))

solution = solve(start)

if solution:
    print("\nSolution found!")
    print("Number of moves:", len(solution) - 1)

    for i, state in enumerate(solution):
        print("Step", i)
        display(state)
else:
    print("No solution exists.")
