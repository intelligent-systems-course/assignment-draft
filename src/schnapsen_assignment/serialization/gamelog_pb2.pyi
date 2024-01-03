from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MoveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGULAR: _ClassVar[MoveType]
    TRUMP_EXCHANGE: _ClassVar[MoveType]
    MARRIAGE: _ClassVar[MoveType]

class Card(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACE_HEARTS: _ClassVar[Card]
    TWO_HEARTS: _ClassVar[Card]
    THREE_HEARTS: _ClassVar[Card]
    FOUR_HEARTS: _ClassVar[Card]
    FIVE_HEARTS: _ClassVar[Card]
    SIX_HEARTS: _ClassVar[Card]
    SEVEN_HEARTS: _ClassVar[Card]
    EIGHT_HEARTS: _ClassVar[Card]
    NINE_HEARTS: _ClassVar[Card]
    TEN_HEARTS: _ClassVar[Card]
    JACK_HEARTS: _ClassVar[Card]
    QUEEN_HEARTS: _ClassVar[Card]
    KING_HEARTS: _ClassVar[Card]
    ACE_CLUBS: _ClassVar[Card]
    TWO_CLUBS: _ClassVar[Card]
    THREE_CLUBS: _ClassVar[Card]
    FOUR_CLUBS: _ClassVar[Card]
    FIVE_CLUBS: _ClassVar[Card]
    SIX_CLUBS: _ClassVar[Card]
    SEVEN_CLUBS: _ClassVar[Card]
    EIGHT_CLUBS: _ClassVar[Card]
    NINE_CLUBS: _ClassVar[Card]
    TEN_CLUBS: _ClassVar[Card]
    JACK_CLUBS: _ClassVar[Card]
    QUEEN_CLUBS: _ClassVar[Card]
    KING_CLUBS: _ClassVar[Card]
    ACE_SPADES: _ClassVar[Card]
    TWO_SPADES: _ClassVar[Card]
    THREE_SPADES: _ClassVar[Card]
    FOUR_SPADES: _ClassVar[Card]
    FIVE_SPADES: _ClassVar[Card]
    SIX_SPADES: _ClassVar[Card]
    SEVEN_SPADES: _ClassVar[Card]
    EIGHT_SPADES: _ClassVar[Card]
    NINE_SPADES: _ClassVar[Card]
    TEN_SPADES: _ClassVar[Card]
    JACK_SPADES: _ClassVar[Card]
    QUEEN_SPADES: _ClassVar[Card]
    KING_SPADES: _ClassVar[Card]
    ACE_DIAMONDS: _ClassVar[Card]
    TWO_DIAMONDS: _ClassVar[Card]
    THREE_DIAMONDS: _ClassVar[Card]
    FOUR_DIAMONDS: _ClassVar[Card]
    FIVE_DIAMONDS: _ClassVar[Card]
    SIX_DIAMONDS: _ClassVar[Card]
    SEVEN_DIAMONDS: _ClassVar[Card]
    EIGHT_DIAMONDS: _ClassVar[Card]
    NINE_DIAMONDS: _ClassVar[Card]
    TEN_DIAMONDS: _ClassVar[Card]
    JACK_DIAMONDS: _ClassVar[Card]
    QUEEN_DIAMONDS: _ClassVar[Card]
    KING_DIAMONDS: _ClassVar[Card]
REGULAR: MoveType
TRUMP_EXCHANGE: MoveType
MARRIAGE: MoveType
ACE_HEARTS: Card
TWO_HEARTS: Card
THREE_HEARTS: Card
FOUR_HEARTS: Card
FIVE_HEARTS: Card
SIX_HEARTS: Card
SEVEN_HEARTS: Card
EIGHT_HEARTS: Card
NINE_HEARTS: Card
TEN_HEARTS: Card
JACK_HEARTS: Card
QUEEN_HEARTS: Card
KING_HEARTS: Card
ACE_CLUBS: Card
TWO_CLUBS: Card
THREE_CLUBS: Card
FOUR_CLUBS: Card
FIVE_CLUBS: Card
SIX_CLUBS: Card
SEVEN_CLUBS: Card
EIGHT_CLUBS: Card
NINE_CLUBS: Card
TEN_CLUBS: Card
JACK_CLUBS: Card
QUEEN_CLUBS: Card
KING_CLUBS: Card
ACE_SPADES: Card
TWO_SPADES: Card
THREE_SPADES: Card
FOUR_SPADES: Card
FIVE_SPADES: Card
SIX_SPADES: Card
SEVEN_SPADES: Card
EIGHT_SPADES: Card
NINE_SPADES: Card
TEN_SPADES: Card
JACK_SPADES: Card
QUEEN_SPADES: Card
KING_SPADES: Card
ACE_DIAMONDS: Card
TWO_DIAMONDS: Card
THREE_DIAMONDS: Card
FOUR_DIAMONDS: Card
FIVE_DIAMONDS: Card
SIX_DIAMONDS: Card
SEVEN_DIAMONDS: Card
EIGHT_DIAMONDS: Card
NINE_DIAMONDS: Card
TEN_DIAMONDS: Card
JACK_DIAMONDS: Card
QUEEN_DIAMONDS: Card
KING_DIAMONDS: Card

class GameLog(_message.Message):
    __slots__ = ("condition1", "condition2", "condition3", "action1", "action2", "action3", "action4", "integration")
    CONDITION1_FIELD_NUMBER: _ClassVar[int]
    CONDITION2_FIELD_NUMBER: _ClassVar[int]
    CONDITION3_FIELD_NUMBER: _ClassVar[int]
    ACTION1_FIELD_NUMBER: _ClassVar[int]
    ACTION2_FIELD_NUMBER: _ClassVar[int]
    ACTION3_FIELD_NUMBER: _ClassVar[int]
    ACTION4_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    condition1: _containers.RepeatedCompositeFieldContainer[ConditionGameLog]
    condition2: _containers.RepeatedCompositeFieldContainer[ConditionGameLog]
    condition3: _containers.RepeatedCompositeFieldContainer[ConditionGameLog]
    action1: _containers.RepeatedCompositeFieldContainer[ActionGameLog]
    action2: _containers.RepeatedCompositeFieldContainer[ActionGameLog]
    action3: _containers.RepeatedCompositeFieldContainer[ActionGameLog]
    action4: _containers.RepeatedCompositeFieldContainer[ActionGameLog]
    integration: _containers.RepeatedCompositeFieldContainer[ActionGameLog]
    def __init__(self, condition1: _Optional[_Iterable[_Union[ConditionGameLog, _Mapping]]] = ..., condition2: _Optional[_Iterable[_Union[ConditionGameLog, _Mapping]]] = ..., condition3: _Optional[_Iterable[_Union[ConditionGameLog, _Mapping]]] = ..., action1: _Optional[_Iterable[_Union[ActionGameLog, _Mapping]]] = ..., action2: _Optional[_Iterable[_Union[ActionGameLog, _Mapping]]] = ..., action3: _Optional[_Iterable[_Union[ActionGameLog, _Mapping]]] = ..., action4: _Optional[_Iterable[_Union[ActionGameLog, _Mapping]]] = ..., integration: _Optional[_Iterable[_Union[ActionGameLog, _Mapping]]] = ...) -> None: ...

class Move(_message.Message):
    __slots__ = ("move_type", "cards")
    MOVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CARDS_FIELD_NUMBER: _ClassVar[int]
    move_type: MoveType
    cards: _containers.RepeatedScalarFieldContainer[Card]
    def __init__(self, move_type: _Optional[_Union[MoveType, str]] = ..., cards: _Optional[_Iterable[_Union[Card, str]]] = ...) -> None: ...

class ActionGameLog(_message.Message):
    __slots__ = ("game_id", "outcomes")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    OUTCOMES_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    outcomes: _containers.RepeatedCompositeFieldContainer[Move]
    def __init__(self, game_id: _Optional[int] = ..., outcomes: _Optional[_Iterable[_Union[Move, _Mapping]]] = ...) -> None: ...

class ConditionGameLog(_message.Message):
    __slots__ = ("game_id", "outcomes")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    OUTCOMES_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    outcomes: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, game_id: _Optional[int] = ..., outcomes: _Optional[_Iterable[bool]] = ...) -> None: ...
