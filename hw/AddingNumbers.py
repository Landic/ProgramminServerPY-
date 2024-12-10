def positiveNumber(message):
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("Value must be positive")
            else:
                return value
        except ValueError:
            print("Error! Enter the number")
        
def main():
    x = positiveNumber("Enter x -> ")
    y = positiveNumber("Enter y -> ")
    print(f"{x}+{y}={x + y}")

if __name__ == "__main__": main()