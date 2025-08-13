A simple Python console application to manage your tasks using a list in memory and store them in a text file using open().

Features:
1)Add a new task
2)Remove an existing task
3)View all tasks
4) Store tasks in a tasks.txt file (auto-created if it doesn’t exist)
5) Loads saved tasks on program start

How It Works:
All tasks are stored in tasks.txt (one per line).

On startup, the program loads tasks from the file into a Python list.

When you add or remove tasks, the changes are immediately saved to the file.
