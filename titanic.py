"""
Hello from LivePreso :) This is the file you should be editing. Good luck!
"""

from collections import Counter
import csv
import decimal
import statistics


class Passenger:
    def __init__(self, row_dict: dict[str, str]) -> None:
        self.id = (
            int(row_dict["PassengerId"]) if not row_dict["PassengerId"] == "" else None
        )
        self.survived = (
            bool(int(row_dict["Survived"])) if not row_dict["Survived"] == "" else None
        )
        self.p_class = int(row_dict["Pclass"]) if not row_dict["Pclass"] == "" else None
        self.name = row_dict["Name"]
        self.sex = row_dict["Sex"]
        self.age = (
            decimal.Decimal(row_dict["Age"]) if not row_dict["Age"] == "" else None
        )
        self.sib_sp = int(row_dict["SibSp"]) if not row_dict["SibSp"] == "" else None
        self.parch = int(row_dict["Parch"]) if not row_dict["Parch"] == "" else None
        self.ticket = row_dict["Ticket"]
        self.fare = (
            decimal.Decimal(row_dict["Fare"]) if not row_dict["Fare"] == "" else None
        )
        self.cabin = row_dict["Cabin"]
        self.embarked = row_dict["Embarked"]


class Titanic:
    def __init__(self) -> None:
        self.passengers = list[Passenger]()

    def load_csv(self, input_file: str) -> None:
        with open(input_file, newline="") as file:
            file_reader = csv.DictReader(file)

            for row_dict in file_reader:
                self.passengers.append(Passenger(row_dict))

    def number_of_passengers(self) -> int:
        return len(self.passengers)

    def total_fare_paid(self) -> float:
        return float(
            sum(
                passenger.fare
                for passenger in self.passengers
                if passenger.fare is not None
            )
        )

    def median_fare(self) -> float:
        return float(
            statistics.median(
                passenger.fare
                for passenger in self.passengers
                if passenger.fare is not None
            )
        )

    def cherbourg_survival_rate(self) -> float:
        cherbourg_passengers = [
            passenger for passenger in self.passengers if passenger.embarked == "C"
        ]

        cherbourg_survivors = [
            passenger for passenger in cherbourg_passengers if passenger.survived
        ]

        return len(cherbourg_survivors) / len(cherbourg_passengers)

    def passenger_class_by_survival(self) -> list[int]:
        passengers_by_class = Counter(
            passenger.p_class
            for passenger in self.passengers
            if passenger.p_class is not None
        )

        survivors_by_class = Counter(
            passenger.p_class
            for passenger in self.passengers
            if passenger.p_class is not None and passenger.survived
        )

        # Create a list of tuples containing the class and the percentage of passengers from that class who
        # survived
        survival_percentage_by_class = [
            (p_class, survivors_by_class[p_class] / total)
            for (p_class, total) in passengers_by_class.items()
        ]
        survival_percentage_by_class.sort(key=lambda x: x[1], reverse=True)

        return [item[0] for item in survival_percentage_by_class]
