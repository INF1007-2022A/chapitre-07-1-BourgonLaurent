#!/usr/bin/env python

import math
import turtle

# Exercice 1
def calculate_volume_mass_of_ellipsoid(
    a: float = 1,
    b: float = 2,
    c: float = 3,
    masse_vol: float = 4,
) -> tuple[float, float]:
    volume = math.pi * a * b * c * 4 / 3
    masse = volume * masse_vol

    return volume, masse


# Exercice 2

# Pris de chapitre-06-1
def frequence(sentence: str) -> dict[str, int]:
    letter_count: dict[str, int] = {}
    for char in sentence:
        letter_count[char] = letter_count.get(char, 0) + 1

    # Reverse sort by value
    sorted_count: list[tuple[str, int]] = sorted(
        letter_count.items(),
        key=lambda x: x[1],
        reverse=True,
    )

    for char, freq in sorted_count:
        if freq >= 5:
            print(f"{char}: {freq}")

    return letter_count


max_letter = lambda phrase: sorted(
    f := frequence(phrase),
    key=f.__getitem__,
    reverse=True,
)[0]


# Exercice 3
def draw_branch(length: int, width: int, angle: int) -> None:
    if (l := length - 10) > 0:
        turtle.pensize(width)
        turtle.forward(length)
        turtle.left(angle)
        draw_branch(l, width - 1, angle - 10)
        turtle.right(angle * 2)
        draw_branch(l, width - 1, angle - 10)
        turtle.left(angle)
        turtle.backward(length)


def draw_tree() -> None:
    turtle.color("green")
    turtle.setheading(90)
    draw_branch(70, 5, 30)
    turtle.done()


# Exercice 4
def get_input(ask: str) -> str:
    return input(f"{ask} : ")


class DNA(list):
    keys = set("atgc")

    def __init__(self):
        super().__init__()

    def is_valid(self) -> bool:
        return set(self).issubset(set("atgc"))

    def set_sequence(self, seq: list[str]) -> None:
        self.extend(seq)

        if not self.is_valid():
            raise ValueError

    def get_ratio(self, seq: str) -> float:
        return "".join(self).count(seq) / len(self)

    def print_ratio(self, seq: str) -> None:
        a = self.get_ratio(seq)
        print(f'Il y a {a:.2%} de "{seq}"')

    @classmethod
    def from_string(cls, dna_chain: str) -> "DNA":
        d = cls()
        d.set_sequence(list(dna_chain))
        return d


if __name__ == "__main__":
    print(calculate_volume_mass_of_ellipsoid())
    print(calculate_volume_mass_of_ellipsoid(2, 4, 6, 8))

    print(max_letter("bonjour"))
    draw_tree()

    d = DNA.from_string("attgcaatggtggtacatg")
    print(d.is_valid())

    e = DNA.from_string(get_input("chaîne"))
    e.print_ratio(get_input("séquence"))
