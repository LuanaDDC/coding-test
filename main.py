#!/usr/local/bin/python3.7
import sys
from src.models import Basket, Item, SpecialOffer


def main():
    if (len(sys.argv) - 1) % 2 != 0 or (len(sys.argv) - 1) == 0:
        print(
            f"Usage: {sys.argv[0]} `item` `quantity`"
            + " [`item` `quantity` `item` `quantity`]"
        )
        print(f"Example: {sys.argv[0]} Apple 4 Orange 3 Watermelon 5")
    else:
        basket = Basket()
        items = {
            "Apple": Item(
                "Apple",
                0.20,
                SpecialOffer("Buy One Get One Free on Apples", 2)
            ),
            "Orange": Item(
                "Orange",
                0.50
            ),
            "Watermelon": Item(
                "Watermelon",
                0.80,
                SpecialOffer("Three For The Price Of Two on Watermelons", 3),
            ),
        }
        n = 1
        for _ in range((len(sys.argv) - 1) // 2):
            try:
                basket.add(items[sys.argv[n]], int(sys.argv[n + 1]))
            except KeyError:
                print(f"Item {sys.argv[n]} not found")
            n += 2
        basket.show()
        basket.apply_special_offers()


if __name__ == "__main__":
    main()
