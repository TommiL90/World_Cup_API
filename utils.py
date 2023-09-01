from datetime import datetime
from teams.exceptions import (
    ImpossibleTitlesError,
    InvalidYearCupError,
    NegativeTitlesError,
)


def data_processing(data: dict):
    titles = data.get("titles", 0)
    if titles < 0:
        raise NegativeTitlesError()

    first_cup_date = datetime.strptime(data.get("first_cup"), "%Y-%m-%d")
   
    if first_cup_date.year < 1930 or (first_cup_date.year - 1930) % 4 != 0:
        raise InvalidYearCupError()

    cups = (datetime.now().year - first_cup_date.year) // 4

    if cups < titles:
        raise ImpossibleTitlesError()

    return data
