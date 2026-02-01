import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    ptr = 0
    num_cases = int(data[ptr])
    ptr += 1
    
    for case_idx in range(num_cases):
        n = int(data[ptr])
        nc = int(data[ptr+1])
        text = data[ptr+2]
        ptr += 3
        
        text_len = len(text)
        if n > text_len:
            sys.stdout.write("0\n")
            if case_idx < num_cases - 1:
                sys.stdout.write("\n")
            continue

        char_map = [0] * 256
        distinct_count = 0
        used = [False] * 256
        for char in text:
            char_code = ord(char)
            if not used[char_code]:
                used[char_code] = True
                char_map[char_code] = distinct_count
                distinct_count += 1
            if distinct_count == nc:
                break
        
        max_hash_possible = 16000001 
        seen = [False] * max_hash_possible
        unique_count = 0
        
        current_hash = 0
        multiplier = 1
        for i in range(n - 1):
            multiplier *= nc
            
        for i in range(n):
            current_hash = current_hash * nc + char_map[ord(text[i])]
            
        seen[current_hash] = True
        unique_count = 1
    
        for i in range(1, text_len - n + 1):
            prev_char_val = char_map[ord(text[i-1])]
            next_char_val = char_map[ord(text[i+n-1])]
            
            current_hash = (current_hash - prev_char_val * multiplier) * nc + next_char_val
            
            if not seen[current_hash]:
                seen[current_hash] = True
                unique_count += 1
                
        sys.stdout.write(str(unique_count) + "\n")
        if case_idx < num_cases - 1:
            sys.stdout.write("\n")

if __name__ == "__main__":
    solve()