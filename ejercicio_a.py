import sys

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * capacity
        self.values = [None] * capacity

    def _hash(self, key):
        h = 0
        for char in key:
            h = (h * 31 + ord(char)) % self.capacity
        return h

    def insert(self, key, value):
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.capacity
        self.keys[index] = key
        self.values[index] = value
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.capacity
        return None

def solve():
    line1 = sys.stdin.readline().split()
    if not line1:
        return
    p, g = map(int, line1)
    hash_table = HashTable(101)

    for _ in range(p):
        data = sys.stdin.readline().split()
        name = data[0]
        percentage = int(round(float(data[1]) * 10))
        hash_table.insert(name, percentage)

    for i in range(1, g + 1):
        tokens = sys.stdin.readline().split()
        
        current_sum = 0
        comparison_op = ""
        target_val = 0
        
        target_val = int(tokens[-1]) * 10
        comparison_op = tokens[-2]
    
        for j in range(len(tokens) - 2):
            if tokens[j] != '+':
                votes = hash_table.get(tokens[j])
                if votes is not None:
                    current_sum += votes
        
        is_correct = False
        if comparison_op == '<':
            is_correct = current_sum < target_val
        elif comparison_op == '>':
            is_correct = current_sum > target_val
        elif comparison_op == '<=':
            is_correct = current_sum <= target_val
        elif comparison_op == '>=':
            is_correct = current_sum >= target_val
        elif comparison_op == '=':
            is_correct = current_sum == target_val
        
        result_str = "correct" if is_correct else "incorrect"
        sys.stdout.write(f"Guess #{i} was {result_str}.\n")

if __name__ == "__main__":
    solve()