from datetime import date
from enum import Enum

from pydantic import (
    BaseModel,
    PositiveInt,
    NegativeInt,
    AwareDatetime,
    TypeAdapter,
    Field,
    ConfigDict,
)


class Units(str, Enum):
    gramm = "gramm"
    _1 = "1"

class Currencies(str, Enum):
    USD = "USD"
    EUR = "EUR"


class BaseRec(BaseModel):
    # allow using both aliases ('datetime-in') and field names ('datetime_in')
    model_config = ConfigDict(populate_by_name=True)


class BuyRec(BaseRec):
    # {'buy': '25-07-2025', ...}
    buy: date
    plan: str
    ticket: str
    datetime_in: date | AwareDatetime = Field(alias="datetime-in")
    quantity: PositiveInt
    units: Units | None = Units._1
    price: float
    currency: Currencies
    exit_plan: str = Field(alias="exit-plan")
    fee: float | None = None


class SellRec(BaseRec):
    # {'sell': '12-08-2025', ...}
    sell: date
    plan: str
    description: str
    ticket: str
    datetime_in: date | AwareDatetime = Field(alias="datetime-in")
    quantity: NegativeInt
    units: Units | None = None
    price: float
    currency: Currencies
    realised_plan: str = Field(alias="realised-plan")
    fee: float | None = None


class DecisionRec(BaseRec):
    # {'decision': '21-05-2025', ...}
    decision: date
    plan: str
    description: str
    datetime_in: date | AwareDatetime = Field(alias="datetime-in")
    exit_plan: str = Field(alias="exit-plan")


IRecord = TypeAdapter(BuyRec | SellRec | DecisionRec)
