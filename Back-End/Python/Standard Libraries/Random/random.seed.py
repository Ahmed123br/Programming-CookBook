import random


def generate_random(seed=None):

    random.seed(seed)
    result = [random.randint(0, 5) for _ in range(5)]

    # Shuffle
    characters = ['a', 'b', 'c', 'd']
    random.shuffle(characters)
    result.append(characters)

    # Gaussian distribution
    result.extend(random.gauss(0, 1) for _ in range(5))
    return result


# print(generate_random())

print(generate_random(0))