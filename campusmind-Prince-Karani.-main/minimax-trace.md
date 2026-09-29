# Hand-Trace: Cafeteria Subtree (MAX moves to Cafeteria)

## Node Traversal & Evaluation
- **Subtree Root**: Cafeteria (Ply 1 - MIN Turn)
- **Initial Bounds**: α = -∞, β = +∞

### 1. MIN options from Cafeteria: ['MainGate', 'StudentCentre', 'SportsComplex']

#### Branch A: MIN moves to MainGate (Ply 2, MAX Turn)
- MAX options: ['Admin', 'Cafeteria']
  - Move to Admin (Ply 3 - Leaf): Utility = -1
  - Move to Cafeteria (Ply 3 - Leaf): Utility = 3
- MAX Value at MainGate: max(-1, 3) = 3
- MIN updates β: β = min(+∞, 3) = 3

#### Branch B: MIN moves to StudentCentre (Ply 2, MAX Turn)
- MAX options: ['Admin', 'Cafeteria', 'SportsComplex']
  - Move to Admin (Ply 3 - Leaf): Utility = -1
  - Move to Cafeteria (Ply 3 - Leaf): Utility = 3
  - Move to SportsComplex (Ply 3 - Leaf): Utility = 2
- MAX Value at StudentCentre: max(-1, 3, 2) = 3
- MIN updates β: β = min(3, 3) = 3

#### Branch C: MIN moves to SportsComplex (Ply 2, MAX Turn)
- MAX options: ['StudentCentre', 'Cafeteria']
  - Move to StudentCentre (Ply 3 - Leaf): Utility = 1
  - Move to Cafeteria (Ply 3 - Leaf): Utility = 3
- MAX Value at SportsComplex: max(1, 3) = 3
- MIN updates β: β = min(3, 3) = 3

---

## Final Backed-Up Result
- Cafeteria Subtree Value: min(3, 3, 3) = 3
