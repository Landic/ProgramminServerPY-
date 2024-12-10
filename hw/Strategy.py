from math import prod

def arithmeticMean(data):
    return sum(data) / len(data)

def geometricMean(data):
    return prod(data) ** (1 / len(data))

def harmonicMean(data):
    return len(data) / sum(1 / x for x in data)

def calculateAverage(data, strategy):
    return strategy(data)

def writeResultsToFile(filename, data, results, max_result, min_result):
    with open(filename, "w") as file:
        file.write(f"Data: {data}\n")
        for name, result in results.items():
            file.write(f"{name}: {result:.2f}\n")
        file.write(f"Maximum result: {max_result:.2f}\n")
        file.write(f"Minimum result: {min_result:.2f}\n")
    print(f"Results have been written to '{filename}'.")

def main():
    data = [10, 20, 30, 40, 50]
    print("Data:", data)

    strategies = {
        "Arithmetic Mean": arithmeticMean,
        "Geometric Mean": geometricMean,
        "Harmonic Mean": harmonicMean
    }

    results = {}

    for name, strategy in strategies.items():
        result = calculateAverage(data, strategy)
        results[name] = result
        print(f"{name}: {result:.2f}")

    max_result = max(results.values())
    min_result = min(results.values())

    print(f"Maximum result: {max_result:.2f}")
    print(f"Minimum result: {min_result:.2f}")

    writeResultsToFile("res.txt", data, results, max_result, min_result)

if __name__ == "__main__":
    main()
