from __future__ import annotations

import random
from abc import ABC, abstractmethod
from typing import List


class PredictionMonitor(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        raise NotImplementedError

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        raise NotImplementedError

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        raise NotImplementedError


class WeatherPredictionMonitor(PredictionMonitor):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _prediction_today: str = "default"
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("PredictionMonitor: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def get_weather_prediction_for_today(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nGeting weather prediction for today")
        #
        self._prediction_today = random.choice(["Sunny", "Cloudy", "Rainy", "Tornado"])

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: PredictionMonitor) -> None:
        """
        Receive update from subject.
        """
        raise NotImplementedError


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class RainyObserver(Observer):
    def update(self, subject: PredictionMonitor) -> None:
        if subject._prediction_today == "Rainy":
            print("Today is a rainy day. Please bring umbrella.")


class TornadoObserver(Observer):
    def update(self, subject: PredictionMonitor) -> None:
        if subject._prediction_today == "Tornado":
            print("Ther is a tornado. Please do not go out!")


if __name__ == "__main__":
    # The client code.

    subject = WeatherPredictionMonitor()

    observer_a = RainyObserver()
    subject.attach(observer_a)

    observer_b = TornadoObserver()
    subject.attach(observer_b)

    subject.get_weather_prediction_for_today()
    subject.get_weather_prediction_for_today()

    subject.detach(observer_a)

    subject.get_weather_prediction_for_today()
