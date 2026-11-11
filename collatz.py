"""Print the Collatz sequence starting from 27 and its step count."""


def collatz(n):
    """Return the Collatz sequence from n through the first occurrence of 1."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz(27)
    for value in sequence:
        print(value)
    print(f"Steps: {len(sequence) - 1}")


if __name__ == "__main__":
    main()
