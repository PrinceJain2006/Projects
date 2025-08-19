🚀 Data Structures Mini Projects (Python)
This repository contains three Python projects that demonstrate core data structures (Linked Lists, Stacks, Queues, and Deques) in practical real-world scenarios.

📂 Projects
1. 🚗 Smart Parking Lot

Description:
A parking lot simulation using a singly linked list. Cars are added to the parking lot until it reaches full capacity. Cars can also exit, and the system dynamically updates available slots.

Features:

Park cars until capacity is reached.

Prevents overflow (parking beyond capacity).

Remove a specific car by its number.

Display currently parked cars.

2. 🚆 Virtual Train Route

Description:
A train route simulation using a doubly linked list. The program supports both linear routes and circular metro routes, allowing forward/backward navigation between stations.

Features:

Add stations dynamically.

Choose between linear or circular routes.

Move train forward ⏩ or backward ⏪.

3. 💬 Message History Manager

Description:
A simple chat/message system that uses queue, stack, and deque concepts. Messages can be sent, undone, and redone, mimicking chat history management.

Features:

Send messages with timestamps.

Undo the last message (removes it from chat).

Redo the last undone message.

View full chat history.

Show the full route.

Show the current station.

📖 Concepts Covered

Linked Lists (singly & doubly linked)

Stacks (LIFO) – Undo/Redo functionality

Queues (FIFO) – Message handling

Deques – Efficient double-ended queue

🚀 Quick Demo
# Run Parking Lot demo
python Smart_parking.py

# Run Train Route demo
python Virtual_Train.py

# Run Message History demo
python Message_history.py

📌 Author

Made with ❤️ for learning Data Structures & Algorithms in Python.

👉 This will make your GitHub README professional and clear.

Do you also want me to add ASCII diagrams (like linked list arrows) to visually show how cars/trains/messages are stored in memory? That would make the README more engaging.

You said:
yes
ChatGPT said:

Perfect! 😃 Adding ASCII diagrams will make your README much more engaging and educational.
Here’s the updated README.md with diagrams included for each project:

🚀 Data Structures Mini Projects (Python)

This repository contains three Python projects that demonstrate core data structures (Linked Lists, Stacks, Queues, and Deques) in practical real-world scenarios.

📂 Projects
1. 🚗 Smart Parking Lot

Description:
A parking lot simulation using a singly linked list. Cars are parked sequentially, and the list updates dynamically as cars enter and exit.

Features:

Park cars until capacity is reached.

Prevents overflow (parking beyond capacity).

Remove a specific car by its number.

Display currently parked cars.

Data Structure: Singly Linked List

Head → [Car KA-01] → [Car KA-02] → [Car KA-03] → None


How to Run:

python Smart_parking.py

2. 🚆 Virtual Train Route

Description:
A train route simulation using a doubly linked list. Supports both linear and circular train routes.

Features:

Add stations dynamically.

Choose between linear and circular routes.

Move train forward ⏩ or backward ⏪.

Show the full route.

Show the current station.

Data Structures: Doubly Linked List (Linear & Circular)

Linear Route Example:

Head ↔ [Station A] ↔ [Station B] ↔ [Station C] ↔ [Station D] ↔ Tail


Circular Route Example:

↔ [Metro X] ↔ [Metro Y] ↔ [Metro Z] ↔
       ↑                       ↓
       └────────── ⭕ ──────────┘


How to Run:

python Virtual_Train.py

3. 💬 Message History Manager

Description:
A simple chat/message system that uses queue, stack, and deque concepts. Messages can be sent, undone, and redone — mimicking a chat history system.

Features:

Send messages with timestamps.

Undo the last message (removes it from chat).

Redo the last undone message.

View full chat history.

Data Structures Used:

Queue (FIFO): Stores active chat messages.

Stack (LIFO): Used for undo and redo actions.

Flow Diagram:

Message Queue (Chat History) → [Msg1] → [Msg2] → [Msg3]

Undo Stack (LIFO): Top → [Msg3]
Redo Stack (LIFO): Top → []


After Undo:

Message Queue → [Msg1] → [Msg2]
Undo Stack    → [Msg1] → [Msg2]
Redo Stack    → [Msg3]


How to Run:

python Message_history.py

🛠 Requirements

Python 3.7+ (tested on Python 3.9+)

No external libraries required (only uses built-in modules).

📖 Concepts Covered

Singly Linked List → Parking Lot

Doubly Linked List → Train Route

Queue (FIFO) → Chat history

Stack (LIFO) → Undo/Redo feature

Deque → Efficient message management

🚀 Quick Demo
# Run Parking Lot demo
python Smart_parking.py

# Run Train Route demo
python Virtual_Train.py

# Run Message History demo
python Message_history.py

📌 Author

Made with ❤️ for learning Data Structures & Algorithms in Python.

✅ With diagrams, anyone reading your README will immediately understand the underlying data structures.

Do you want me to also create a graphical flowchart (PNG/SVG) version of these diagrams so you can add visuals to GitHub instead of just ASCII art?
