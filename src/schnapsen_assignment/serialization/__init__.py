from .gamelog_pb2 import ActionGameLog, ConditionGameLog, GameLog, Move, MoveType, Card
from schnapsen.game import Move as SchnapsenMove, RegularMove, Marriage, TrumpExchange
from schnapsen.deck import Card as SchnapsenCard


def to_pb_move(move: SchnapsenMove) -> Move:
    if move.is_regular_move():
        move_type = MoveType.REGULAR
    elif move.is_trump_exchange():
        move_type = MoveType.TRUMP_EXCHANGE
    elif move.is_marriage():
        move_type = MoveType.MARRIAGE
    else:
        raise AssertionError("Code path must never reach here. File an issue on github")
    return Move(move_type=move_type, cards=[card.name for card in move.cards])


def to_schnapsen_card(card: Card) -> SchnapsenCard:
    name = Card.Name(card)
    return SchnapsenCard[name]


def to_schnapsen_move(move: Move) -> SchnapsenMove:
    if move.move_type == MoveType.REGULAR:
        assert len(move.cards) == 1
        return RegularMove(to_schnapsen_card(move.cards[0]))
    elif move.move_type == MoveType.TRUMP_EXCHANGE:
        assert len(move.cards) == 1
        return TrumpExchange(to_schnapsen_card(move.cards[0]))
    elif move.move_type == MoveType.MARRIAGE:
        assert len(move.cards) == 2
        return Marriage(to_schnapsen_card(move.cards[0]), to_schnapsen_card(move.cards[1]))
    else:
        raise AssertionError("Code path must never reach here. File an issue on github")


__all__ = ["ActionGameLog", "ConditionGameLog", "GameLog", "Move", "to_pb_move", "to_schnapsen_move"]
