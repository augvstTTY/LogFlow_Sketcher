class SpaceSavingCounter:
    """
    A minimal implementation of the Space-Saving algorithm for finding
    frequent items in a data stream. Embodies 'Applied Rigor'.
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity  # Number of items to track
        self.counters = {}        # Format: {item: count}
        self.min_value = 0        # Track the minimum count for eviction

    def add(self, item: str):
        """Process a new item from the stream."""
        if item in self.counters:
            self.counters[item] += 1
        elif len(self.counters) < self.capacity:
            self.counters[item] = 1
            self.min_value = 1
        else:
            # Find item with min count and replace it
            min_item = None
            for key, value in self.counters.items():
                if value == self.min_value:
                    min_item = key
                    break
            
            if min_item:
                del self.counters[min_item]
                self.counters[item] = self.min_value + 1
            else:
                self.counters[item] = 1

    def get_top_k(self, k: int) -> list:
        """Get the top k most frequent items."""
        sorted_items = sorted(self.counters.items(), key=lambda x: x[1], reverse=True)
        return sorted_items[:k]

    def __str__(self):
        return f"SpaceSavingCounter(tracking {len(self.counters)}/{self.capacity} items)"
