"""
Hello from LivePreso :) This is the file you should be editing. Good luck!
"""

import csv


class Passenger:
    def __init__(self, row_dict: dict[str, str]) -> None:
        self.id = int(row_dict["PassengerId"])
        self.survived = bool(row_dict["Survived"])
        self.p_class = int(row_dict["Pclass"])
        self.name = row_dict["Name"]
        self.sex = row_dict["Sex"]
        self.age = float(row_dict["Age"]) if not row_dict["Age"] == "" else None
        self.sib_sp = int(row_dict["SibSp"])
        self.parch = int(row_dict["Parch"])
        self.ticket = row_dict["Ticket"]
        self.fare = float(row_dict["Fare"])
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

    def print_passengers(self) -> None:
        for passenger in self.passengers:
            print(vars(passenger))

    def number_of_passengers(self) -> int:
        return len(self.passengers)

    def total_fare_paid(self) -> int:
        return 30000

    def median_fare(self) -> int:
        return 15

    def cherbourg_survival_rate(self) -> float:
        return 0.5

    def passenger_class_by_survival(self) -> list[int]:
        return [2, 3, 1]
