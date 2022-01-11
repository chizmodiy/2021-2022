
from collections import Counter

def frequency_sort(items):
    counts = Counter(items)
    return sorted(items, key=lambda k: counts[k] * len(items) - items.index(k), reverse=True)

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4,6,2,2,2,6,4,4,4]))