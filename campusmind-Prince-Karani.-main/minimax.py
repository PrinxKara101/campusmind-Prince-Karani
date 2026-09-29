from game import CampusMindGame

def minimax(node, depth, is_maximizing, game, leaf_counter=None):
    if leaf_counter is None:
        leaf_counter = [0]

    if depth == 3:
        leaf_counter[0] += 1
        return game.utility(node), leaf_counter[0]

    neighbors = game.get_neighbors(node)

    if is_maximizing:
        max_eval = float('-inf')
        for neighbor in neighbors:
            eval_val, _ = minimax(neighbor, depth + 1, False, game, leaf_counter)
            max_eval = max(max_eval, eval_val)
        return max_eval, leaf_counter[0]
    else:
        min_eval = float('inf')
        for neighbor in neighbors:
            eval_val, _ = minimax(neighbor, depth + 1, True, game, leaf_counter)
            min_eval = min(min_eval, eval_val)
        return min_eval, leaf_counter[0]

def evaluate_root_children():
    game = CampusMindGame()
    admin_val, _ = minimax('Admin', 1, False, game, [0])
    cafeteria_val, _ = minimax('Cafeteria', 1, False, game, [0])
    return admin_val, cafeteria_val
