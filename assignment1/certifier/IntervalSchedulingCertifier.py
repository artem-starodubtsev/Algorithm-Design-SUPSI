from dataclasses import dataclass

from .core.Certifier import Certifier
from .core.Schedule import Schedule, Interval


@dataclass
class IntervalSchedulingInstance:
    S: Schedule


@dataclass
class IntervalSchedulingSolution:
    interval_idxes: list[int]


class IntervalSchedulingCertifier(Certifier[IntervalSchedulingInstance, IntervalSchedulingSolution]):
    def certify(self, instance: IntervalSchedulingInstance, solution: IntervalSchedulingSolution) -> bool:
        chosen = [instance.S.intervals[i] for i in solution.interval_idxes]
        chosen.sort(key=lambda x: x.start)

        for a, b in zip(chosen, chosen[1:]):
            if b.start < a.end:
                return False

        return True
