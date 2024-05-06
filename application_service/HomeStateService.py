import domain.HomeState as homeState
from abc import ABC, abstractmethod

class HomeStateService:
    @abstractmethod
    def update(present, occupied):
        pass

    @abstractmethod
    def retrieve_home_state(home_state):
        pass