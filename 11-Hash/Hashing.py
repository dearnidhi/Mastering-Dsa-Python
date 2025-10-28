

def mod(number, cellNumber):
    return number % cellNumber


# print(mod(400, 24))


def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber

print(modASCII("ABC", 24))



# ✅ 1. Find the First Non-Repeating Character in a String
def first_non_repeating_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return "_"

# ✅ 2. Check for Duplicates in an Array
def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

# ✅ 3. Two Sum Problem
def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in hashmap:
            return [hashmap[comp], i]
        hashmap[num] = i
# ✅ 4. Group Anagrams Together
from collections import defaultdict

def group_anagrams(words):
    hashmap = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))  # sort as key
        hashmap[key].append(word)
    return list(hashmap.values())

#✅ 5. Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    seen = {}
    left = max_len = 0
    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1
        seen[s[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len



