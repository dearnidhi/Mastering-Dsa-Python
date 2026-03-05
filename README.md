# Mastering DSA with Python — FAANG/MNC Interview Roadmap

A complete, structured DSA course in Python to crack **FAANG & Big MNC interviews**.
Every topic has: Dry Run tables + Optimal Code + Time/Space Complexity Analysis.

---

## FAANG Interview Roadmap (10 Phases)

| Phase | Topics | Status |
|-------|--------|--------|
| **Phase 1 – Foundations** | Big O, Arrays, Lists, Strings, Math, Tuples | Done |
| **Phase 2 – Core DS** | LinkedList, Stack, Queue, Hash/Dict | Done |
| **Phase 3 – Algorithms** | Recursion, Searching, Sorting, Sliding Window | Done |
| **Phase 4 – Two Pointers** | Classic patterns, 3Sum, Trapping Rain Water | Done |
| **Phase 5 – Trees** | Binary Tree, BST, BFS/DFS on Trees | Done |
| **Phase 6 – Heaps** | Priority Queue, Top K, Median, Task Scheduler | Done |
| **Phase 7 – Graphs** | BFS/DFS, Topo Sort, Union-Find, Dijkstra | Done |
| **Phase 8 – Dynamic Programming** | 1D/2D DP, Knapsack, LCS, LIS, Coin Change | Done |
| **Phase 9 – Backtracking** | Subsets, Permutations, Combination Sum | Done |
| **Phase 10 – Greedy** | Intervals, Jump Game, Gas Station | Done |

> Study Order: Do phases in order. Do NOT skip to DP before Trees and Graphs.

---

## Total Questions: ~170 Questions

### Phase 1 — Foundations

#### 1-Big O Notation
- Time and Space Complexity analysis
- Best / Average / Worst case
- Amortized analysis

#### 2-Array (16 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 268 | Missing Number | Easy |
| 2 | 1 | Two Sum | Easy |
| 3 | 121 | Best Time to Buy and Sell Stock | Easy |
| 4 | N/A | Find a Number (Linear Search) | Easy |
| 5 | 1464 | Maximum Product of Two Integers | Easy |
| 6 | N/A | Middle of List | Easy |
| 7 | 1572 | 2D List Diagonal Sum | Easy |
| 8 | 414 | Third Maximum Number | Easy |
| 9 | 26 | Remove Duplicates from Sorted Array | Easy |
| 10 | Var | Pair Sum (Two Sum variation) | Easy |
| 11 | 217 | Contains Duplicate | Easy |
| 12 | 567 | Permutation in String | Medium |
| 13 | 48 | Rotate Image (Matrix) | Medium |
| 14 | 1929 | Concatenation of Array | Easy |
| 15 | 1512 | Number of Good Pairs | Easy |
| 16 | 2011 | Final Value of Variable After Operations | Easy |

#### 3-List (10 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 1365 | How Many Numbers Smaller Than Current | Easy |
| 2 | 1470 | Shuffle the Array | Easy |
| 3 | 1431 | Kids With Greatest Candies | Easy |
| 4 | 1389 | Create Target Array in Given Order | Easy |
| 5 | 448 | Find All Numbers Disappeared in Array | Easy |
| 6 | 350 | Intersection of Two Arrays II | Easy |
| 7 | 88 | Merge Sorted Array | Easy |
| 8 | 283 | Move Zeroes | Easy |
| 9 | 118 | Pascal's Triangle | Easy |
| 10 | 485 | Max Consecutive Ones | Easy |

#### 4-Dict (15 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 260 | Single Number III | Medium |
| 2 | 720 | Longest Word in Dictionary | Medium |
| 3 | 676 | Implement Magic Dictionary | Medium |
| 4 | 139 | Word Break | Medium |
| 5 | 884 | Uncommon Words from Two Sentences | Easy |
| 6 | 953 | Verifying an Alien Dictionary | Easy |
| 7 | 127 | Word Ladder | Hard |
| 8 | 269 | Alien Dictionary | Hard |
| 9 | 49 | Group Anagrams | Medium |
| 10 | 1160 | Find Words Formed by Characters | Easy |

#### 5-Tuple
- Immutability, Named tuples, use as hashmap keys

#### 6-String (5 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | Custom | Count Vowels and Consonants | Easy |
| 2 | 5 | Longest Palindromic Substring | Medium |
| 3 | 6 | Zigzag Conversion | Medium |
| 4 | 14 | Longest Common Prefix | Easy |
| 5 | 125 | Valid Palindrome | Easy |

#### 7-Math
- Prime numbers, GCD, LCM, Modular arithmetic

---

### Phase 2 — Core Data Structures

#### 8-Recursion (5 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | Custom | Factorial | Easy |
| 2 | 509 | Fibonacci Number | Easy |
| 3 | Custom | Sum of First N Numbers | Easy |
| 4 | 344 | Reverse String | Easy |
| 5 | 24 | Swap Nodes in Pairs | Medium |

#### 9-LinkedList (10 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 206 | Reverse Linked List | Easy |
| 2 | 21 | Merge Two Sorted Lists | Easy |
| 3 | 141 | Linked List Cycle | Easy |
| 4 | 876 | Middle of Linked List | Easy |
| 5 | 203 | Remove Linked List Elements | Easy |
| 6 | 708 | Insert into Sorted Circular Linked List | Medium |
| 7 | Custom | Josephus Circle | Medium |
| 8 | 707 | Design Linked List | Medium |
| 9 | 430 | Flatten Multilevel Doubly Linked List | Medium |
| 10 | 146 | LRU Cache | Hard |

#### 10-Stack (9 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 155 | Min Stack | Medium |
| 2 | 1172 | Dinner Plate Stacks | Hard |
| 3 | 232 | Implement Queue using Stacks | Easy |
| 4 | 20 | Valid Parentheses | Easy |
| 5 | 739 | Daily Temperatures | Medium |
| 6 | 84 | Largest Rectangle in Histogram | Hard |
| 7 | 394 | Decode String | Medium |

#### 11-Queue (6 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 622 | Design Circular Queue | Medium |
| 2 | 933 | Number of Recent Calls | Easy |
| 3 | 225 | Implement Stack using Queues | Easy |
| 4 | 346 | Moving Average from Data Stream | Easy |
| 5 | 239 | Sliding Window Maximum | Hard |

#### 12-Hash (15 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 383 | Ransom Note | Easy |
| 2 | 238 | Product of Array Except Self | Medium |
| 3 | 451 | Sort Characters by Frequency | Medium |
| 4 | 387 | First Unique Character in String | Easy |
| 5 | 3541 | Count Elements with Max Frequency | Easy |
| 6 | 242 | Valid Anagram | Easy |
| 7 | 525 | Contiguous Array | Medium |
| 8 | 560 | Subarray Sum Equals K | Medium |
| 9 | 347 | Top K Frequent Elements | Medium |
| 10 | 290 | Word Pattern | Easy |
| 11 | 205 | Isomorphic Strings | Easy |

---

### Phase 3 — Algorithms

#### 13-Searching (3 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 35 | Search Insert Position | Easy |
| 2 | 704 | Binary Search | Easy |
| 3 | 74 | Search a 2D Matrix | Medium |

#### 14-Sorting
- Bubble, Selection, Insertion, Bucket, Merge, Quick, Heap Sort

#### 15-Sliding Window (10 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 209 | Minimum Size Subarray Sum | Medium |
| 2 | 1456 | Max Vowels in Substring of Length K | Medium |
| 3 | 2461 | Max Sum of Distinct Subarrays Length K | Medium |
| 4 | 643 | Maximum Average Subarray I | Easy |
| 5 | 904 | Fruit Into Baskets | Medium |
| 6 | 3 | Longest Substring Without Repeating Chars | Medium |
| 7 | 1004 | Max Consecutive Ones III | Medium |
| 8 | 76 | Minimum Window Substring | Hard |
| 9 | 30 | Substring with Concatenation of All Words | Hard |
| 10 | 567 | Permutation in String | Medium |

---

### Phase 4 — Two Pointers (NEW)

#### 16-TwoPointers (8 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 167 | Two Sum II (Sorted Array) | Medium |
| 2 | 977 | Squares of a Sorted Array | Easy |
| 3 | 11 | Container With Most Water | Medium |
| 4 | 42 | Trapping Rain Water | Hard |
| 5 | 15 | 3Sum | Medium |
| 6 | 16 | 3Sum Closest | Medium |
| 7 | 75 | Sort Colors (Dutch National Flag) | Medium |
| 8 | 680 | Valid Palindrome II | Easy |

---

### Phase 5 — Trees (NEW)

#### 17-Trees (12 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 104 | Maximum Depth of Binary Tree | Easy |
| 2 | 226 | Invert Binary Tree | Easy |
| 3 | 100 | Same Tree | Easy |
| 4 | 102 | Binary Tree Level Order Traversal | Medium |
| 5 | 543 | Diameter of Binary Tree | Easy |
| 6 | 110 | Balanced Binary Tree | Easy |
| 7 | 112 | Path Sum | Easy |
| 8 | 199 | Binary Tree Right Side View | Medium |
| 9 | 98 | Validate Binary Search Tree | Medium |
| 10 | 235 | Lowest Common Ancestor of BST | Medium |
| 11 | 230 | Kth Smallest Element in BST | Medium |
| 12 | 105 | Construct BT from Preorder and Inorder | Medium |

---

### Phase 6 — Heaps / Priority Queue (NEW)

#### 18-Heaps (8 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 215 | Kth Largest Element in Array | Medium |
| 2 | 1046 | Last Stone Weight | Easy |
| 3 | 347 | Top K Frequent Elements | Medium |
| 4 | 295 | Find Median from Data Stream | Hard |
| 5 | 23 | Merge K Sorted Lists | Hard |
| 6 | 973 | K Closest Points to Origin | Medium |
| 7 | 621 | Task Scheduler | Medium |
| 8 | 378 | Kth Smallest Element in Matrix | Medium |

---

### Phase 7 — Graphs (NEW)

#### 19-Graphs (10 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 200 | Number of Islands | Medium |
| 2 | 695 | Max Area of Island | Medium |
| 3 | 994 | Rotting Oranges | Medium |
| 4 | 133 | Clone Graph | Medium |
| 5 | 207 | Course Schedule (Cycle Detection) | Medium |
| 6 | 210 | Course Schedule II (Topological Sort) | Medium |
| 7 | 417 | Pacific Atlantic Water Flow | Medium |
| 8 | 684 | Redundant Connection (Union-Find) | Medium |
| 9 | 743 | Network Delay Time (Dijkstra) | Medium |
| 10 | 130 | Surrounded Regions | Medium |

---

### Phase 8 — Dynamic Programming (NEW)

#### 20-DynamicProgramming (12 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 70 | Climbing Stairs | Easy |
| 2 | 53 | Maximum Subarray (Kadane's Algorithm) | Medium |
| 3 | 198 | House Robber | Medium |
| 4 | 213 | House Robber II | Medium |
| 5 | 322 | Coin Change | Medium |
| 6 | 518 | Coin Change II | Medium |
| 7 | 300 | Longest Increasing Subsequence | Medium |
| 8 | 1143 | Longest Common Subsequence | Medium |
| 9 | 416 | Partition Equal Subset Sum | Medium |
| 10 | 152 | Maximum Product Subarray | Medium |
| 11 | 62 | Unique Paths | Medium |
| 12 | 72 | Edit Distance | Hard |

---

### Phase 9 — Backtracking (NEW)

#### 21-Backtracking (8 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 78 | Subsets | Medium |
| 2 | 90 | Subsets II | Medium |
| 3 | 46 | Permutations | Medium |
| 4 | 47 | Permutations II | Medium |
| 5 | 39 | Combination Sum | Medium |
| 6 | 40 | Combination Sum II | Medium |
| 7 | 17 | Letter Combinations of Phone Number | Medium |
| 8 | 79 | Word Search | Medium |

---

### Phase 10 — Greedy (NEW)

#### 22-Greedy (8 Qs)
| # | LeetCode | Problem | Difficulty |
|---|----------|---------|-----------|
| 1 | 455 | Assign Cookies | Easy |
| 2 | 55 | Jump Game | Medium |
| 3 | 45 | Jump Game II | Medium |
| 4 | 56 | Merge Intervals | Medium |
| 5 | 57 | Insert Interval | Medium |
| 6 | 435 | Non-overlapping Intervals | Medium |
| 7 | 763 | Partition Labels | Medium |
| 8 | 134 | Gas Station | Medium |

---

## Optimization Cheat Sheet

| Brute Force | Optimal | Technique |
|-------------|---------|-----------|
| O(n^2) nested loops | O(n) two pointers | Two Pointers |
| O(n^2) nested loops | O(n) hashmap | Hashing |
| O(2^n) recursive | O(n) or O(n^2) DP | Dynamic Programming |
| O(n) scan per query | O(n) prefix sum | Prefix Sum |
| O(n*k) subarray | O(n) | Sliding Window |
| O(n^2) re-sort | O(n log n) heap | Heap / Priority Queue |
| O(n) per find/union | O(alpha n) approx O(1) | Union-Find |

## DS to Pattern Mapping (Interview Quick Ref)

| Data Structure | When to Use |
|---------------|-------------|
| HashMap | Frequency count, 2Sum, anagram check |
| Stack | Parentheses matching, monotonic, next greater element |
| Queue / Deque | BFS, sliding window max |
| Heap / heapq | Top K elements, merge K lists, median stream |
| Union-Find | Connected components, cycle detection |
| TreeNode DFS | Path sum, diameter, LCA, validate BST |
| TreeNode BFS | Level order, right side view, zigzag |

---

## File Structure

```
Mastering-Dsa-Python/
├── 1-Big O Notation/
├── 2-Array/                    16 Qs
├── 3-List/                     10 Qs
├── 4-Dict/                     15 Qs
├── 5-tuple/
├── 6-String/                    5 Qs
├── 7-Math/
├── 8-Recursion/                 5 Qs
├── 9-LinkedList/               10 Qs
├── 10-Stack/                    9 Qs
├── 11-Queue/                    6 Qs
├── 12-Hash/                    15 Qs
├── 13-searching/                3 Qs
├── 14-sorting/
├── 15-SlidingWindow/           10 Qs
├── 16-TwoPointers/              8 Qs  NEW
├── 17-Trees/                   12 Qs  NEW
├── 18-Heaps/                    8 Qs  NEW
├── 19-Graphs/                  10 Qs  NEW
├── 20-DynamicProgramming/      12 Qs  NEW
├── 21-Backtracking/             8 Qs  NEW
├── 22-Greedy/                   8 Qs  NEW
├── Dsa Q.docx
└── Python Dsa Pattern & Template Handbook.docx
```

---

## How to Use

1. Follow phases in ORDER — do not skip ahead
2. For each problem: read -> trace dry run -> code yourself -> compare solution
3. After each topic: solve 2-3 new LeetCode problems unseen
4. Always state TC/SC — interviewers WILL ask
5. When stuck: explain what you know, ask clarifying questions — do not go silent

---

## Additional Resources

- **DSA Q.docx** – Practice questions (your personal progress tracker)
- **Python Dsa Pattern and Template Handbook.docx** – Common patterns and reusable templates

---

## Tech Stack

- Python 3.12
- Jupyter Notebooks (.ipynb)
- LeetCode for online practice
