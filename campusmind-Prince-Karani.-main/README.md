# campusmind-Prince-Karani.ICS 2413: Artificial Intelligence
CampusMind — Project Introduction & Individual Foundation Assignment (Weeks 1–3)

1. What You're Building
Imagine a new student arrives on campus. They might ask:

"How do I get from the Main Gate to the Library?"
"What is the shortest route to the Science Laboratory?"
"Which office should I visit if I have a problem with fees?"
"I need to register for a course. Where should I go?"

A normal website could just show a map. CampusMind is different. Over this semester, you're building a small AI system that doesn't just display a route — it reasons about campus. By the end of the semester, it will represent the campus as a formal problem, search for routes, compare them, represent knowledge about locations, reason with rules, answer logic queries, and accept simple natural-language questions.


This is the individual foundation phase. Every student builds their own version of the same problem, alone. You're not designing the campus, and you're not building search intelligence yet either. Your job across these three weeks is narrower and more specific:

Week 1: turn a real-world map into a formal problem a machine can search. No algorithm code.
Week 2: teach that formal problem to search blindly — BFS and DFS.
Week 3: teach it to search with a sense of direction — A*, with a heuristic you derive yourself.



2. The Campus
You are not inventing the campus. Everyone uses this one, exactly as given:

                [Library]
                    |
                  2 km
                    |

[Main Gate] – 1 km– [Admin Block] – 2 km – [Science Lab]

     |                                      			|

    3 km                                  			2 km

     |                                      			|

[Cafeteria] ---------------- 2 km -------- [Student Affairs]

Code
Location
What it's for
L1
Main Gate
Primary entrance to campus
L2
Administration Block
Admissions, registration, finance, general admin
L3
Library
Academic learning and study resources
L4
Science Laboratory
Science and computing practical facilities
L5
Student Affairs
Student welfare, guidance, student-related services
L6
Cafeteria
Food and refreshment services


Connections and costs (movement is possible in both directions):

From
To
Cost
Main Gate
Administration Block
1
Administration Block
Library
2
Administration Block
Science Lab
2
Main Gate
Cafeteria
3
Cafeteria
Student Affairs
2
Science Lab
Student Affairs
2



3. Turning a Map into a Formal Problem
A human can look at the diagram above and answer "how do I get from the Main Gate to the Science Lab?" by eye. An AI system can't — it needs the problem stated precisely, using the same five parts every search problem in this course is built from:

Part
Question it answers
State
Where is the user currently located?
Initial state
Where does the journey begin?
Goal state
Where does the user want to go?
Actions
What moves are legal from a given state?
Cost
What does the number on each connection represent?


This is the transformation this whole course is built on: "find a route" becomes a state-space search problem. Week 1 is you doing that transformation, on paper, before any code exists.



4. Tools
Python 3 — this is what you build CampusMind in, this week and for the rest of the semester
Git and GitHub — for submission, starting now, and again in Week 7 when teams merge individual work into one shared repository
A text editor or IDE of your choice
Google Classroom (submission)

You do not need LISP or PROLOG installed for this assignment. PROLOG has its own dedicated weeks later in the semester (9–10), with its own setup instructions when you get there.

5. Repository Setup (do this before Part 1)
Create a free GitHub account if you don't have one: github.com
Create a new repository named campusmind-yourfirstname-yourlastname (e.g. campusmind-john-mwangi), set to Private
Add your instructor as a collaborator (Settings > Collaborators), username bbworksb
Clone the repository, or create your project folder locally and connect it — whichever works for you
Make your first commit before writing any real content, even just an empty README.md

Repository structure for Weeks 1–3:

campusmind/
│
├── problem-definition/
│   └── 01_problem-definition.pdf
├── bfs/
│   └── bfs.py
├── dfs/
│   └── dfs.py
├── astar/
│   └── astar.py
├── search-comparison/
│   └── 03-search-comparison.pdf
└── README.md



New to git?

Check if it's installed: git --version (if missing, install from git-scm.com)
Connect your folder to your new repo:

git clone https://github.com/your-username/campusmind-yourname.git

or, if you already have a folder:

git init

git remote add origin https://github.com/your-username/campusmind-yourname.git

Your workflow after each part:

git add .

git commit -m "Part 1: problem definition"

git push

(First push may need git push -u origin main.)

Commit as you go, at each part — not as one upload the night before it's due. Bring git problems to Monday's lab rather than debugging alone.



PART 1 — Define the AI Problem (Week 1)
No code this week. This part is a written formalization only.

Task: write the formal definition of the CampusMind navigation problem, using the campus given in Section 2.

Deliverable: 01_problem-definition.pdf, containing:

A. Problem statement — explain the practical problem in your own words
B. Initial state — the starting location
C. Goal state — the destination
D. State representation — what one state looks like, e.g. CurrentLocation = Administration Block
E. Actions — what movements are allowed
F. Goal test — how the system knows it has arrived
G. Cost — what the numbers on each connection represent
H. State-space graph — draw the six-location graph yourself

Commit checkpoint: "Part 1: problem definition"

PART 2 — BFS and DFS (Week 2)
Task 1: implement BFS. Test it on Main Gate → Science Lab.

Task 2: implement DFS. Use the same problem.

Task 3: compare them. In your README or a short note, answer:

Which path did each find?
Were the paths different? Why or why not, on this specific graph?
Which algorithm would you prefer, and under what conditions?

Deliverable: bfs/ and dfs/ folders as shown in Section 5, each containing working, runnable code, plus your short comparison note.

Commit checkpoint: "Part 2: BFS and DFS"

PART 3 — Heuristic Search: A* (Week 3)
Task: implement A* for the same navigation problem.

You must define your own heuristic. The map in Section 2 gives you a topology and edge costs, not coordinates — so you choose how to estimate. Pick one of these two approaches:

Option A — Hop-count heuristic (safe default): estimate the distance to the goal by counting the minimum number of connections to reach it, ignoring cost. On this specific graph, this is always admissible — explain in one sentence why (hint: every connection costs at least 1, so hop-count can never exceed the true cost).

Option B — Estimated-distance heuristic (more ambitious): sketch your own reasonable relative positions for the six locations, based on the layout diagram in Section 2, and compute straight-line distance estimates yourself. This is harder to justify — you must argue, in your own words, why your specific estimates never overestimate the true cost.

Whichever you choose, state it clearly and justify it. There is no single correct heuristic here — there is a correct argument for whichever one you pick.

Compare: run BFS, DFS, and A* on the same selected route.

Deliverable: astar/ folder with working code, plus 03-search-comparison.pdf containing:

Route chosen
Search behavior of each algorithm
Path cost found by each
Heuristic used, and your admissibility argument
Comparison of the three
Explanation of why A* performed differently (or didn't, and why)

Important: do not just copy a search algorithm from somewhere. You must be able to explain, without notes:

what the frontier contains at any point
how a node is expanded
how the goal is detected
what your heuristic estimates, and why it doesn't overestimate

Commit checkpoint: "Part 3: A* and heuristic comparison"

What to Submit
The link to your private GitHub repository, pasted into Google Classroom, before the next session.

Your repository should show at least three meaningful commits, one per part, not one commit containing everything. A single commit dated the night before the deadline will be treated as a red flag.
How This Will Be Checked
You may be asked to walk through and explain any part of what you submit, in your own words, without notes. Work you cannot explain will not be treated as your own for grading purposes.

