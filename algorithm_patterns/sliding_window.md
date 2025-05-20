# Sliding window Pattern

## ✅ When to use

Use **sliding window** when you're dealing with problems involving:
- **Contiguous sequence** (subarray or substrings)
- **Fixed or dynamic size window**
- **Max/min/avg/sum** within a window

---

## 💡 Core idea

- Move a **start** and **end** pointer over the array
- Keep track of values (sum, count, etc.) as the window moves
- Shrink or expand the window based on condition

---

## 🧠 Template (Fixed Size)

```python

def sliding_window(arr):
    window_start = 0
    result = 0 or float('inf') or [] depending on the problem
    window_data = {} # For frequency maps or state tracking

    for window_end in range(len(arr)):
        right_char = arr[window_end]
        # update the window state (e.g add to window_data)
        # window_data[right_char] = window_data.get(char, 0) + 1

        # Shrink the window untill condition is valid
        while invalid_window_condition(window_data):
            left_char = arr[window_start]
            # Remove left_char from window data
            window_start += 1

        # update result (max, min, count, etc)
        # result = max(result, window_end - window_start +1)

    return result