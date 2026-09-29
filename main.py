from game import CampusMindGame
from minimax import minimax, evaluate_root_children
from alphabeta import alphabeta

def run_flipped_game():
    game = CampusMindGame()
    val, _ = minimax('MainGate', 0, False, game, [0])
    admin_val, _ = minimax('Admin', 1, True, game, [0])
    cafeteria_val, _ = minimax('Cafeteria', 1, True, game, [0])
    best_min_move = 'Admin' if admin_val < cafeteria_val else 'Cafeteria'
    best_move_val = min(admin_val, cafeteria_val)
    return val, best_min_move, best_move_val

def main():
    game = CampusMindGame()

    print("==========================================")
    print("CAMPUSMIND GAME VERIFICATION")
    print("==========================================")

    mm_val, mm_leaves = minimax('MainGate', 0, True, game)
    admin_val, caf_val = evaluate_root_children()
    
    print(f"Minimax Return Value: {mm_val} (Target: 3)")
    print(f"Root Option Admin: {admin_val} (Target: -1)")
    print(f"Root Option Cafeteria: {caf_val} (Target: 3)")
    print(f"Full Minimax Leaves Evaluated: {mm_leaves} (Target: 9)")

    ab_val, ab_leaves = alphabeta('MainGate', 0, float('-inf'), float('inf'), True, game)
    print(f"\nAlpha-Beta Return Value: {ab_val} (Target: 3)")
    print(f"Alpha-Beta Leaves Evaluated: {ab_leaves} (Target: 7)")

    flipped_val, best_move, move_val = run_flipped_game()
    print("\n==========================================")
    print("FLIPPED FIRST MOVER EXTENSION")
    print("==========================================")
    print(f"New Game Value: {flipped_val}")
    print(f"MIN's Best First Move: {best_move} (Value: {move_val})")

if __name__ == '__main__':
    main()
