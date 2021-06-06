import time


class Dice:
    def __init__(self, dim, coef=1, modif=0):
        self.dim = dim
        self.coef = coef
        self.modif = modif
        self.min = coef + modif
        self.max = coef * dim + modif

    def __repr__(self):
        return f"Dice {self.coef}d{self.dim}+{self.modif}"


def prob_equal(dice: Dice, value):
    if value < dice.min or value > dice.max:
        return 0
    return 1 / dice.dim


def prob_less(dice: Dice, value):
    return sum([prob_equal(dice, j) for j in range(1, value)])


def prob_win(dice_1: Dice, dice_2: Dice):
    return (1 / dice_1.dim) * sum([prob_less(dice_2, i) for i in range(dice_1.min, dice_1.max + 1)])


def main():
    d1 = Dice(4, 1, 2)
    d2 = Dice(4, 1, 1)
    print(f"Tests {d1} against {d2}")
    print(prob_win(d1, d2))


if __name__ == '__main__':
    main()
