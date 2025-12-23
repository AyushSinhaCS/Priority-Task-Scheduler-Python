import heapq

class TaskScheduler:
    def __init__(self):
        self.priority_heap = []  # Binary Heap (Priority Queue)
        self.task_map = {}       # Hash Map for O(1) task retrieval
        self.REMOVED = '<removed-task>' # Placeholder for deleted tasks

    def add_task(self, task_id, name, priority):
        """Adds a task or updates its priority (Priority Update)."""
        if task_id in self.task_map:
            self.remove_task(task_id) # Mark old task as removed
        
        # Priority is negated for Max-Heap behavior
        entry = [-priority, task_id, name]
        self.task_map[task_id] = entry
        heapq.heappush(self.priority_heap, entry)
        print(f"✅ Added/Updated: {name} (Priority: {priority})")

    def remove_task(self, task_id):
        """Marks a task as removed (Efficient Deletion)."""
        entry = self.task_map.pop(task_id, None)
        if entry:
            entry[-1] = self.REMOVED # Invalidate the entry in the heap

    def execute_next(self):
        """Executes the highest priority task in O(log N)."""
        while self.priority_heap:
            priority, task_id, name = heapq.heappop(self.priority_heap)
            if name is not self.REMOVED:
                del self.task_map[task_id]
                print(f"🚀 Executing: {name} (ID: {task_id}) [Priority: {-priority}]")
                return name
        print("⚠️ Queue is empty.")
        return None

# Simulation
if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.add_task(101, "Fix Critical Bug", 10)
    scheduler.add_task(102, "Documentation", 2)
    
    # Priority Update (As per your CV)
    scheduler.add_task(102, "Urgent Documentation", 15) 
    
    scheduler.execute_next() # Will execute ID 102 first because it was updated to 15
