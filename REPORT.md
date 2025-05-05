# Milestone 1 Report: Apriori Brute-Force Solution

## Problem Statement
Given a set of hosts (used/unused) and their tags, find the **smallest subset of tags** that:
1. Maximizes coverage of unused hosts,
2. Excludes all used hosts.

## Methodology
### Algorithm Design
1. **Tag Filtering**: Remove tags associated with any used host.
2. **Combinatorial Search**: Use Apriori-style iteration to generate tag combinations of increasing size.
3. **Coverage Calculation**: For each combination, compute how many unused hosts are covered.
4. **Early Termination**: Stop when the first valid solution is found (smallest tag set with maximal coverage).

## Results
- **Optimality**: Guarantees the minimal tag set for maximal coverage.
- **Example Output**: For 5 hosts and 3 tags, the algorithm correctly identifies `T2` as the optimal tag.

## Limitations
1. **Scalability**: Fails for datasets with >20 tags due to exponential complexity.
2. **Input Sensitivity**: If all valid tags are excluded (e.g., due to association with used hosts), coverage drops to zero.