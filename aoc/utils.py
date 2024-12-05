from typing import List


def load_data(path) -> List[str]:
    with open(path) as f:
        content = f.readlines()
    return content
