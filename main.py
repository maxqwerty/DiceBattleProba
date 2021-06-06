from dice_proba import Dice, prob_win


def main():
    d1 = Dice(4, 1, 2)
    d2 = Dice(4, 1, 1)
    print(f"Tests {d1} against {d2}")
    print(prob_win(d1, d2))


if __name__ == '__main__':
    main()
