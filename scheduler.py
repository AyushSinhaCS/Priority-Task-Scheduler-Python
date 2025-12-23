import heapq

class TaskScheduler:
    def __init__(self):
        # The heap stores tasks as [-priority, task_id, name]
        # We use negative priority because heapq is a Min-Heap by default
        self.priority_heap = []
        self.task_lookup = {}  # Hash Map for O(1) retrieval

    def add_task(self, task_id, name, priority):
        """Adds a task with O(log N) complexity."""
        # Negative priority to simulate Max-Heap
        task_entry = [-priority, task_id, name]
        heapq.heappush(self.priority_heap, task_entry)
        self.task_lookup[task_id] = name
        print(f"✅ Added Task: {name} (Priority: {priority})")

    def execute_next(self):
        """Removes and returns the highest priority task in O(log N)."""
        if not self.priority_heap:
            print("⚠️ No tasks in the queue.")
            return None
        
        neg_priority, task_id, name = heapq.heappop(self.priority_heap)
        del self.task_lookup[task_id]
        print(f"🚀 Executing: {name} [ID: {task_id}] with Priority: {-neg_priority}")
        return name

    def get_task(self, task_id):
        """Retrieves task details in O(1) average time."""
        task_name = self.task_lookup.get(task_id)
        if task_name:
            print(f"🔍 Found Task {task_id}: {task_name}")
        else:
            print(f"❌ Task ID {task_id} not found.")

# --- Simulation ---
if __name__ == "__main__":
    scheduler = TaskScheduler()
    
    # Adding tasks (Urgency based)
    scheduler.add_task(1, "Critical System Update", 10)
    scheduler.add_task(2, "Routine Database Cleanup", 3)
    scheduler.add_task(3, "Security Firewall Patch", 8)

    # Retrieval check (O(1))
    scheduler.get_task(1)

    # Execution check (Highest priority first)
    scheduler.execute_next()  # Should be Priority 10
    scheduler.execute_next()  # Should be Priority 8
