from abc import ABCMeta, abstractmethod
from enum import Enum

class StateType(Enum):
    STATE_STOPPED = 0
    STATE_LOGGING = 1


class State(metaclass=ABCMeta):
    # @abstractmethod
    # def get_typecode(self) -> 'StateType':
    #     pass
    @abstractmethod
    def start(self) -> 'State':
        pass
    @abstractmethod
    def stop(self) -> 'State':
        pass
    @abstractmethod
    def log(self, info) -> None:
        pass

class StateStopped(State):
    # def get_typecode(self) -> 'StateType':
    #     return StateType.STATE_STOPPED

    def start(self) -> 'State':
        print('** START LOGGING **')
        return StateLogging()
    
    def stop(self) -> 'State':
        return self

    def log(self, info):
        print('** Ignoring:{} **'.format(info))

class StateLogging(State): 
    # def get_typecode(self):
    #     return StateType.STATE_LOGGING

    def start(self) -> 'State':
        return self
    
    def stop(self) -> 'State':
        print('** STOP LOGGING **')
        return StateStopped()
        
    def log(self, info):
        print('** Logging:{} **'.format(info))

class Logger:
    def __init__(self):
        self._state = StateStopped()
    
    # def set_state(self, state):
    #     if state == StateType.STATE_STOPPED:
    #         self._state = StateStopped()
    #     elif state == StateType.STATE_LOGGING:
    #         self._state = StateLogging()

    def start(self):
        self._state = self._state.start()

    def stop(self):
        self._state = self._state.stop()

    def log(self, info):
        self._state.log(info)
