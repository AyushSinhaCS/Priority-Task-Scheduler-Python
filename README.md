# Priority-Task-Scheduler-Python
# Dynamic Priority Task Scheduler (Python)

## 📌 Project Overview
A high-performance task scheduling system built in Python to manage concurrent processes based on urgency. This project implements core Data Structures (Heaps and Hash Maps) to ensure tasks are prioritized and retrieved with optimal time complexity.

## 🛠️ Data Structures Used
* **Binary Heap (`heapq`):** Used to maintain the priority queue. Provides $O(\log N)$ time for both insertion and extraction, ensuring the most urgent task is always at the top.
* **Hash Map (`dict`):** Used for instant $O(1)$ task lookups and metadata management.



## 🚀 Key Features
* **Max-Priority Logic:** Dynamically handles task urgency using a negated heap implementation.
* **Real-time Management:** Designed to simulate task scheduling in high-load backend environments.
* **Efficient Memory Usage:** Uses a compact dictionary-heap hybrid to minimize overhead.

## 💻 Usage
1. Clone the repo:
   ```bash
   git clone [https://github.com/AyushSinhaCS/Priority-Task-Scheduler-Python.git](https://github.com/AyushSinhaCS/Priority-Task-Scheduler-Python.git)
