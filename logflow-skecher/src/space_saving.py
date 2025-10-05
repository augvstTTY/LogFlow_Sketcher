class SpaceSavingCounter:
    """
    Space-Saving Algorithm implementation for finding frequent items in data streams.
    
    Educational implementation based on the rigorous theoretical algorithm used in
    real-world systems like network monitoring and log analytics.
    """

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.counters = {}
        self._min_count = 0

    def add(self, item: str):
        """
        Process a new item from the stream.
        
        This implements the core Space-Saving logic: track frequent items
        with constant memory, trading exact counts for efficiency.
        """
        if item in self.counters:
            self.counters[item] += 1
        elif len(self.counters) < self.capacity:
            self.counters[item] = 1
            self._min_count = 1
        else:
            # Replace the item with minimum count
            self._replace_min_item(item)

    def _replace_min_item(self, new_item: str):
        """Replace an item with the current minimum count."""
        min_items = [k for k, v in self.counters.items() if v == self._min_count]
        if min_items:
            removed_item = min_items[0]
            del self.counters[removed_item]
            self.counters[new_item] = self._min_count + 1
            # Update min_count if we removed the last item with this count
            if not any(v == self._min_count for v in self.counters.values()):
                self._min_count = min(self.counters.values()) if self.counters else 0

    def get_top_k(self, k: int) -> list:
        """Get the top k most frequent items with their estimated counts."""
        if k <= 0:
            return []
        sorted_items = sorted(self.counters.items(), key=lambda x: x[1], reverse=True)
        return sorted_items[:min(k, len(sorted_items))]

    def get_metrics(self) -> dict:
        """Get algorithm performance metrics."""
        return {
            "capacity": self.capacity,
            "current_items": len(self.counters),
            "min_count": self._min_count,
            "utilization": f"{len(self.counters)}/{self.capacity}"
        }

    def __str__(self):
        return f"SpaceSavingCounter({self.get_metrics()['utilization']} items)"
