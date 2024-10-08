from dataclasses import dataclass


@dataclass
class Stats:
    length_of_path: int
    is_coin_found: bool
    is_swamp_found: bool
