"""PawPal+ system — class skeleton generated from diagrams/uml.mmd.

Keep this file in sync with the UML class diagram.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Pet:
    pet_id: int
    name: str
    age: int
    breed: str


@dataclass
class Task:
    task_id: int
    title: str
    duration_minutes: int
    priority: str
    status: str


@dataclass
class DailyPlan:
    date: date
    tasks: list[Task] = field(default_factory=list)

    def num_tasks(self) -> int:
        """Return the number of tasks in this plan."""
        pass


@dataclass
class PetOwner:
    name: str
    pets: list[Pet] = field(default_factory=list)
    tasks: list[Task] = field(default_factory=list)

    def num_pets(self) -> int:
        """Return the number of pets owned."""
        pass

    def num_tasks(self) -> int:
        """Return the number of tasks managed."""
        pass

    def addTask(self, task: Task) -> None:
        """Add a task to this owner's task list."""
        pass

    def removeTask(self, task_id: int) -> None:
        """Remove the task with the given id from this owner's task list."""
        pass

    def generate_daily_plan(self, date: date) -> DailyPlan:
        """Build and return a DailyPlan for the given date."""
        pass
