from models.pots_model import Pot, Pots


def get_pots():
    pots: list[Pot] = [
        Pot(name="Savings", target=2000, total=159),
        Pot(name="Gift", target=150, total=110),
        Pot(name="Concert Ticket", target=150, total=110),
        Pot(name="New Laptop", target=1000, total=10),
        Pot(name="Holiday", target=1440, total=531),
    ]
    return pots
