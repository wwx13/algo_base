#

def n_queens(n):
    if not n:
        return []

    def is_valid(tg_pos, states):
        for pos in states:
            # print(pos, tg_pos)
            if pos[0] == tg_pos[0] or pos[1] == tg_pos[1] or (
                    abs(pos[1] - tg_pos[1]) / abs(pos[0] - tg_pos[0])) == 1:
                return False
        return True

    all_routes = []
    routes = []
    def recur_run(i, states, routes):
        if i == n:
            all_routes.append(routes.copy())
            return
        for col in range(n):
            if is_valid((i, col), states):
                print(i, (i, col))
                # base = "." * n
                base = "." * col + "Q" + "." * (n-col-1)
                states.append((i, col))
                routes.append(base)
                recur_run(i+1, states, routes)
                states.pop(-1)
                routes.pop(-1)
    states = []
    routes = []
    recur_run(0, states, routes)

    return all_routes