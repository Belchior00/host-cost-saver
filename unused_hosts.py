from dataclasses import dataclass
from typing import List, Dict
from itertools import combinations, product
from collections import defaultdict

@dataclass
class Tag:
    key: str
    value: str

@dataclass
class Host:
    name: str
    tags: List[Tag]

@dataclass
class Combination:
    key: str
    values: List[str]

@dataclass
class SelectedTags:
    tags: List[Combination]

def unused_hosts(hosts: List[Host], used: Dict[str, bool]) -> List[SelectedTags]:
    tag_to_hosts = defaultdict(set)
    for host in hosts:
        for tag in host.tags:
            tag_to_hosts[(tag.key, tag.value)].add(host.name)

    used_hosts = {name for name, is_used in used.items() if is_used}
    unused_hosts_set = {host.name for host in hosts if not used.get(host.name, False)}

    valid_tags = {
        tag for tag, host_names in tag_to_hosts.items()
        if not host_names & used_hosts
    }

    key_to_values = defaultdict(set)
    for key, value in valid_tags:
        key_to_values[key].add(value)

    best_coverage = 0
    best_combinations = []

    for r in range(1, len(key_to_values) + 1):
        for keys_combo in combinations(key_to_values.keys(), r):
            value_combinations = [list(key_to_values[key]) for key in keys_combo]
            for values_combo in product(*value_combinations):
                try:
                    covered_hosts = set.intersection(
                        *[
                            tag_to_hosts[(key, value)]
                            for key, value in zip(keys_combo, values_combo)
                        ]
                    )
                except KeyError:
                    continue

                if covered_hosts <= unused_hosts_set:
                    coverage = len(covered_hosts)
                    if coverage > best_coverage:
                        best_coverage = coverage
                        best_combinations = [list(zip(keys_combo, values_combo))]
                    elif coverage == best_coverage:
                        best_combinations.append(list(zip(keys_combo, values_combo)))

        if best_coverage > 0:
            break

    result = []
    for combo in best_combinations:
        combo_dict = defaultdict(list)
        for key, value in combo:
            combo_dict[key].append(value)
        selected_tags = SelectedTags(
            tags=[Combination(key=key, values=values) for key, values in combo_dict.items()]
        )
        result.append(selected_tags)

    return result

# Example test case
if __name__ == "__main__":
    hosts = [
        Host(name="M1", tags=[Tag("team", "ds"), Tag("bu", "ML"), Tag("app", "hydra"), Tag("instance-type", "m1")]),
        Host(name="M2", tags=[Tag("team", "ds"), Tag("bu", "ML"), Tag("app", "psz"), Tag("instance-type", "m1")]),
        Host(name="M3", tags=[Tag("team", "ds"), Tag("bu", "ML"), Tag("app", "paywall"), Tag("instance-type", "m1")]),
        Host(name="M4", tags=[Tag("team", "de"), Tag("bu", "ML"), Tag("app", "search"), Tag("instance-type", "m1")]),
        Host(name="M5", tags=[Tag("team", "de"), Tag("bu", "ML"), Tag("app", "cron"), Tag("instance-type", "m1")]),
        Host(name="M6", tags=[Tag("team", "de"), Tag("bu", "ML"), Tag("app", "warehouse"), Tag("instance-type", "m1")]),
    ]

    used = {
        "M1": True,
        "M2": True,
        "M3": False,
        "M4": True,
        "M5": True,
        "M6": False,
    }

    result = unused_hosts(hosts, used)
    for selected in result:
        print(selected)
