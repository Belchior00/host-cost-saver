Approach: Apriori-Inspired Brute Force

Step 1: Parse Host Data

Each host is defined by a name and a list of tags.

Step 2: Remove Invalid Tags

All tags associated with used hosts are filtered out.

Step 3: Group Tags by Key

Tag values are grouped under each tag key to allow combinations like:

Combination(key="app", values=["paywall", "warehouse"])

Step 4: Generate Combinations

For increasing sizes of tag key combinations (e.g., just "app", then "app+team", etc):

All value combinations are tested

The set of hosts covered by those tags is computed

Only combinations that cover unused hosts only are kept

Track the one(s) with maximum coverage

Step 5: Return Result

The best combinations are returned using the required dataclass structure.

✅ Output Format

Returns a list of SelectedTags, each containing:

key: tag key (e.g., app)

values: list of values that together identify only unused hosts
