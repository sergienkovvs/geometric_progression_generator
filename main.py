def geometric_progression_generator(first_element=1, element_step=1.5):
    while True:
        first_element *= element_step
        yield first_element


if __name__ == "__main__":
    progression = geometric_progression_generator(1, 0.5)
    print(next(progression))
    print(next(progression))
    print(next(progression))
    print(next(progression))
    print(next(progression))
    print(next(progression))
    print(next(progression))
