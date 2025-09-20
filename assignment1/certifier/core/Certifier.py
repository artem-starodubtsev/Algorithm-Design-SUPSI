from abc import ABC, abstractmethod


class Certifier[TInstance, TSolution](ABC):
    @abstractmethod
    def certify(self, instance: TInstance, solution: TSolution) -> bool:
        raise NotImplementedError
