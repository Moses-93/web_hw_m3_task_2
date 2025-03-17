from concurrent.futures import ProcessPoolExecutor
import time
from multiprocessing import cpu_count


def factorize(number):
    """
    This A function for calculating the factors of a single number.

    Parameters:
    number (int): The number for which to calculate the factors.

    Returns:
    tuple: A tuple containing the original number and a sorted list of its factors.
    """
    factors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    return number, sorted(factors)


start_time = time.time()


def processing(*numbers):
    """
    This function processes a list of numbers by calculating their factors using multiprocessing.

    Parameters:
    *numbers (int): Variable length argument list of numbers to process.

    Returns:
    None
    """
    start_time = time.time()
    with ProcessPoolExecutor(cpu_count()) as executor:
        results = executor.map(factorize, numbers)
    end_time = time.time()
    for number, factors in results:
        print(f"The factors of {number} are: {factors}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]
    processing(*numbers)
