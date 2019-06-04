class SpecialOffer(object):
    """
    A class used to represent a Special offer
    Attributes
    ----------
    title : str
        title of the offer
    count : int
        minimal number of item to activate the special offer
    """

    def __init__(self, title: str, count: int):
        self.title = title
        self.count = count

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title


class Item(object):
    """
    A class used to represent a Item
    Attributes
    ----------
    __item_count : int
        number of item
    name : int
        name of the item
    price : int
        price of the item
    special_offer : SpecialOffer
        special offer linked to the item
    item_id : int
        the id of the item
    Methods
    -------
    has_offer()
        return true if the item has a special offer, false if not
    """

    __item_count = 1

    def __init__(self, name: str, price: float,
                 special_offer: SpecialOffer = None):
        """
        Parameters
        ----------
        name : str
            The name of the Item
        price : int
            The price of the Item
        special_offer : SpecialOffer, optional
            Special offer linked to the Item (default is None)
        """
        self.name = name
        self.price = price
        self.special_offer = special_offer
        self.item_id = Item.__item_count
        Item.__item_count += 1

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def has_offer(self) -> bool:
        return True if self.special_offer else False


class Basket(object):
    """
    A class used to represent a Basket
    Attributes
    ----------
    content: dict
        The content of the basket
    total: int
        The price of the basket
    """
    def __init__(self):
        self.content = {}
        self.total = 0

    def add(self, item: Item, quantity: int) -> None:
        """
        Add an item to the basket
        Parameters
        ----------
        item: Item
            The item to add
        quantity: int
            Number of item to add
        """
        if quantity > 0:
            if self.content.get(item):
                self.content[item] += quantity
            else:
                self.content[item] = quantity

    def show(self) -> None:
        """
        Display the content of the basket
        """
        for item, quantity in self.content.items():
            print(f"{item} * {quantity} =>" +
                  f" {(item.price * quantity):.2f}£")

    def calculate_price(self) -> None:
        """
        Calculate the price of the basket
        """
        self.total = 0
        for item, quantity in self.content.items():
            self.total += item.price * (quantity)

    def get_price(self) -> int:
        """
        Return the price of the basket
        """
        return self.total

    def apply_special_offers(self) -> None:
        """
        Apply Special Offers and update the price of the basket
        """
        self.calculate_price()
        print("----------")
        print("Special offer(s):")
        for item, quantity in self.content.items():
            free_item = 0
            if item.has_offer() and item.special_offer.count <= quantity:
                free_item = quantity // item.special_offer.count
                special_offer = free_item * item.price
                self.total -= special_offer
                print(f"{item.special_offer.title}: " +
                      f"-{special_offer:.2f}£ ({free_item} free)")
        print("----------")
        print(f"Total: {self.total:.2f}£")
