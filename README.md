Host Cost-Saving Optimization - Milestone 1

This project implements a brute-force Apriori-inspired algorithm to identify minimal tag combinations that cover the maximum number of unused hosts without including any used hosts.

Function Signature

The algorithm follows the exact structure provided in the job description:

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
    ...

▶️ How to Run

Make sure you have Python 3.7+ installed.

Save the file as unused_hosts.py.

Run the script:

python unused_hosts.py

Example Output

Given the following hosts and usage info:

M3 and M6 are unused

M1, M2, M4, M5 are used

Output:

SelectedTags(tags=[Combination(key='app', values=['paywall'])])
SelectedTags(tags=[Combination(key='app', values=['warehouse'])])

This means tags like app:paywall and app:warehouse target only unused hosts.
