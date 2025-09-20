from dataclasses import dataclass

@dataclass
class Interval:
    start: int
    end: int

@dataclass
class Schedule:
    _intervals: list[Interval]

    @staticmethod
    def from_tuples(intervals: list[tuple[int, int]]) -> "Schedule":
        return Schedule([Interval(i[0], i[1]) for i in intervals])

    @property
    def intervals(self) -> list[Interval]:
        return self._intervals



