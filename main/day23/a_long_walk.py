from collections import deque, defaultdict

SLOPE_DIRS = {'<': (-1, 0), '>': (1, 0), 'v': (0, 1), '^': (0, -1)}


def solve(walkable, handle_slopes) -> int:
    graph = build_graph(walkable, handle_slopes)
    graph = squash_nodes(graph)
    start = next(k for k, v in walkable.items() if v == 'S')
    end = next(k for k, v in walkable.items() if v == 'E')
    return find_longest_path(start, end, graph)


def build_graph(walkable, handle_slopes):
    # build graph of (x, y): [(neighbour, num_steps_between)]
    graph = defaultdict(dict)
    for coord, tile in walkable.items():
        for neighbour in get_adjacent_cells(coord, tile, handle_slopes):
            if walkable.get(neighbour, None):
                graph[coord][neighbour] = 1
    return graph


def squash_nodes(graph):
    to_squash = next(iter(k for k, v in graph.items() if len(v) == 2), None)
    while to_squash:
        to_merge = []
        num_steps = 0
        for adj_coord, adj_steps in graph[to_squash].items():
            if to_squash in graph[adj_coord]:
                graph[adj_coord].pop(to_squash)
            to_merge.append(adj_coord)
            num_steps += adj_steps

        graph[to_merge[0]][to_merge[1]] = num_steps
        graph[to_merge[1]][to_merge[0]] = num_steps

        graph.pop(to_squash)
        to_squash = next(iter(k for k, v in graph.items() if len(v) == 2), None)
    return graph


def find_longest_path(start, end, graph):
    to_visit = deque([(start, set(), 0)])
    longest = 0
    while to_visit:
        current, visited, num_steps = to_visit.popleft()
        if current == end:
            longest = max(longest, num_steps)
            continue

        for neighbour_coord, neighbour_steps in graph[current].items():
            if neighbour_coord not in visited:
                to_visit.append((neighbour_coord, visited | {current}, num_steps + neighbour_steps))

    return longest


def get_adjacent_cells(current, tile, handle_slopes):
    if handle_slopes and tile in ('<', '>', 'v', '^'):
        slope_direction = SLOPE_DIRS[tile]
        return [(current[0] + slope_direction[0], current[1] + slope_direction[1])]
    else:
        return [(current[0] + 1, current[1]),
                (current[0] - 1, current[1]),
                (current[0], current[1] + 1),
                (current[0], current[1] - 1)]
