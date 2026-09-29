"""
alphabeta.py - Alpha-Beta Pruning Algorithm
"""
from game import CampusMindGame

def alphabeta(node, depth, alpha, beta, is_maximizing, game, leaf_counter=None):
    if leaf_counter is None:
        leaf_counter = [0]

    # Leaf node reached at depth 3
    if depth == 3:
        leaf_counter[0] += 1
        return game.utility(node), leaf_counter[0]

    neighbors = game.get_neighbors(node)

    if is_maximizing:
        value = float('-inf')
        for neighbor in neighbors:
            eval_val, _ = alphabeta(neighbor, depth + 1, alpha, beta, False, game, leaf_counter)
            value = max(value, eval_val)
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # Beta cutoff
        return value, leaf_counter[0]
    else:
        value = float('inf')
        for neighbor in neighbors:
            eval_val, _ = alphabeta(neighbor, depth + 1, True, game, leaf_counter)
            value = min(value, eval_val)
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cutoff
        return value, leaf_counter[0]