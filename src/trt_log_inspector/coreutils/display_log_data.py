from abc import ABC, abstractmethod


class DisplayLogData(ABC):
    @abstractmethod
    def display_table(self):
        pass

    @abstractmethod
    def display_plot(self):
        pass
