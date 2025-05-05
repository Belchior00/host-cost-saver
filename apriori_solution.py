from itertools import combinations
from collections import defaultdict

def apriori_brute_force(hosts, tags, used_hosts):
    """
    Apriori-inspired brute-force algorithm to find the minimal tag set 
    that maximizes coverage of unused hosts while excluding all used hosts.

    Args:
        hosts (dict): {host_id: set_of_tags}
        tags (dict): {tag: set_of_associated_hosts}
        used_hosts (set): Set of used host IDs

    Returns:
        tuple: (best_coverage, list_of_optimal_tag_combinations)
    """
    # Step 1: Filter out tags associated with used hosts
    invalid_tags = {
        tag for tag, tag_hosts in tags.items()
        if tag_hosts & used_hosts  # Tags intersecting with used hosts are invalid
    }
    valid_tags = set(tags.keys()) - invalid_tags

    # Step 2: Identify unused hosts
    unused_hosts = set(hosts.keys()) - used_hosts

    best_coverage = 0
    best_combinations = []

    # Step 3: Generate tag combinations of increasing size
    for r in range(1, len(valid_tags) + 1):
        # Iterate through all combinations of size r
        for combo in combinations(valid_tags, r):
            # Calculate covered hosts as the union of all tags in the combo
            covered_hosts = set().union(*(tags[tag] for tag in combo))
            # Coverage = intersection with unused hosts
            coverage = len(covered_hosts & unused_hosts)

            # Update best combinations
            if coverage > best_coverage:
                best_coverage = coverage
                best_combinations = [combo]
            elif coverage == best_coverage:
                best_combinations.append(combo)

        # Early termination if a valid solution is found
        if best_coverage > 0:
            break

    return best_coverage, best_combinations

# Example Usage
if __name__ == "__main__":
    # Sample input: 5 hosts with tags
    hosts_example = {
        'H1': {'T1', 'T3'},
        'H2': {'T3'},
        'H3': {'T1'},
        'H4': {'T2', 'T3'},
        'H5': {'T3'}
    }

    # Build tags dictionary from hosts
    tags_example = defaultdict(set)
    for host, host_tags in hosts_example.items():
        for tag in host_tags:
            tags_example[tag].add(host)

    used_hosts_example = {'H1', 'H2'}

    # Run the algorithm
    coverage, combinations = apriori_brute_force(
        hosts_example, tags_example, used_hosts_example
    )

    print(f"Best coverage: {coverage}")
    print(f"Optimal tag combinations: {combinations}")
