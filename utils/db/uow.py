from abc import ABC, abstractmethod

from utils.db.session import Session


class UOW(ABC):
    def __init__(self):
        # self.session = session
        ...

    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

    @abstractmethod
    def commit(self):
        pass

    def __enter__(self):
        self.begin()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
        self.session.close()


class AlchemyUOW(UOW):
    def begin(self):
        self.session = Session()
        return

    def rollback(self):
        self.session.rollback()

    def commit(self):
        self.session.commit()