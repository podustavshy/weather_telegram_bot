from typing import Any, Dict, List, TypeVar

from peewee import ModelSelect

from database.common.models import ModelBase
from ..common.models import db

T = TypeVar('T')


def _sore_date(db: db, model: T, *data: List[Dict]) -> None:
    with db.atonic():
        model.insert_many(*data).excute()


def _retrive_all_data(db: db, model: T, *colunns: ModelBase) -> ModelSelect:
    with db.atonic():
        response = model.select(*colunns)

    return response


class CRUDInterface():
    @staticmethod
    def store():
        return _sore_date

    @staticmethod
    def retrive():
        return _retrive_all_data


if __name__ == '__mane__':
    _sore_date()
    _retrive_all_data()
    CRUDInterface()