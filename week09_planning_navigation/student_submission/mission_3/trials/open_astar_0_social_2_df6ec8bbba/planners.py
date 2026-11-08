"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct

def _is_free(grid, cell):
    """True if the cell is inside the grid and not a wall (wall = 1)."""
    r, c = cell
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0


def bfs(ctx):
    """FIFO queue. Mark discovered cells when enqueuing and store parents.
    Use ctx.expand(current, len(frontier)+1) to obtain neighbours.
    BFS minimizes number of unit-cost edges, not execution time on a robot.
    """
    start, goal = ctx.start, ctx.goal
    if not _is_free(ctx.grid, start) or not _is_free(ctx.grid, goal):
        return []
    if start == goal:
        return [start]
    parent = {start: None}
    queue = deque([start])
    while queue:
        current = queue.popleft()              # oldest entry first
        if current == goal:
            return reconstruct(parent, goal)
        for nxt in ctx.expand(current, len(queue) + 1):
            if nxt not in parent:
                parent[nxt] = current
                queue.append(nxt)
    return []


def dfs(ctx):
    """LIFO stack. Track discovered cells and parents to avoid cycles.
    A valid DFS path need not be shortest. Keep the supplied neighbour order.
    """
    start, goal = ctx.start, ctx.goal
    if not _is_free(ctx.grid, start) or not _is_free(ctx.grid, goal):
        return []
    if start == goal:
        return [start]
    parent = {start: None}
    stack = [start]
    while stack:
        current = stack.pop()                  # newest entry first
        if current == goal:
            return reconstruct(parent, goal)
        for nxt in ctx.expand(current, len(stack) + 1):
            if nxt not in parent:
                parent[nxt] = current
                stack.append(nxt)
    return []

def iddfs(ctx):
    """Run depth-limited DFS with bounds 0, 1, 2, ... .
    Prevent cycles on the current path. Do not keep a global visited set across
    depth limits. Count expansions again on every iteration. Return [] only
    after exhaustive failure. Catch no budget exceptions. The runner records
    resource_limit honestly if this expensive method reaches its budget.
    """
    start, goal = ctx.start, ctx.goal
    if not _is_free(ctx.grid, start) or not _is_free(ctx.grid, goal):
        return []
    if start == goal:
        return [start]

    def has_open_neighbor(cell, on_path):
        r, c = cell
        for n in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
            if _is_free(ctx.grid, n) and n not in on_path:
                return True
        return False

    limit = 0
    while True:
        cutoff = False                         # did the limit hide anything?
        path = [start]
        on_path = {start}
        frames = []                            # one neighbour iterator per expanded cell
        if limit == 0:
            cutoff = has_open_neighbor(start, on_path)
        else:
            frames.append(iter(ctx.expand(start, 1)))
        while frames:
            nxt = next(frames[-1], None)
            if nxt is None:                    # cell finished, back up
                frames.pop()
                on_path.discard(path.pop())
                continue
            if nxt in on_path:
                continue
            if nxt == goal:
                return path + [nxt]
            path.append(nxt)
            on_path.add(nxt)
            if len(path) - 1 < limit:
                frames.append(iter(ctx.expand(nxt, len(frames) + 1)))
            else:                              # at the limit, do not go deeper
                if has_open_neighbor(nxt, on_path):
                    cutoff = True
                path.pop()
                on_path.discard(nxt)
        if not cutoff:                         # nothing cut off, search exhausted
            return []
        limit += 1


def astar(ctx):
    """Use a heap ordered by g + ctx.heuristic(cell).
    Keep best g costs and parents. Ignore outdated heap entries. Each edge
    costs 1. Stop when the goal is removed from the priority queue.
    """
    start, goal = ctx.start, ctx.goal
    if not _is_free(ctx.grid, start) or not _is_free(ctx.grid, goal):
        return []
    if start == goal:
        return [start]
    g = {start: 0}
    parent = {start: None}
    heap = []
    heappush(heap, (ctx.heuristic(start), 0, start))
    while heap:
        _, cost, current = heappop(heap)
        if cost > g[current]:                  # outdated entry
            continue
        if current == goal:
            return reconstruct(parent, goal)
        for nxt in ctx.expand(current, len(heap) + 1):
            new_cost = cost + 1
            if new_cost < g.get(nxt, float("inf")):
                g[nxt] = new_cost
                parent[nxt] = current
                heappush(heap, (new_cost + ctx.heuristic(nxt), new_cost, nxt))
    return []