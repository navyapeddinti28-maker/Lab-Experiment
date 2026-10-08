from collections import deque

def is_valid(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    # Missionaries should not be outnumbered by cannibals
    if m_left > 0 and m_left < c_left:
        return False

    if m_right > 0 and m_right < c_right:
        return False

    return True


def get_next_states(state):
    m_left, c_left, boat = state

    # Possible combinations in the boat
    moves = [
        (1, 0),   # 1 missionary
        (2, 0),   # 2 missionaries
        (0, 1),   # 1 cannibal
        (0, 2),   # 2 cannibals
        (1, 1)    # 1 missionary and 1 cannibal
    ]

    next_states = []

    for m, c in moves:
        if boat == 0:  # Boat on left side
            new_state = (m_left - m, c_left - c, 1)

            if m_left >= m and c_left >= c and is_valid(new_state):
                next_states.append(new_state)

        else:  # Boat on right side
            new_state = (m_left + m, c_left + c, 0)

            if (3 - m_left) >= m and (3 - c_left) >= c:
                if is_valid(new_state):
                    next_states.append(new_state)

    return next_states


def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Solution:")
            for step in path:
                print(step)
            return

        for next_state in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    print("No solution found.")


solve()
