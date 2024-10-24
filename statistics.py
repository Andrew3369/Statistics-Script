import statistics

def insertNumbers(numArray):
    while True:
        user_input = input("Enter the data set with a number, followed by an 'x' if you want to stop: ")
        if user_input.lower() == 'x':
            break
        try:
            number = float(user_input)
            numArray.append(number)
        except ValueError:
            print("enter a integer or 'x' to stop.")

def numFrequencies(numArray):
    frequency_map = {}
    for num in numArray:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    print("Frequency of All numbers inside the list")
    print("Number\tFrequency")
    print("-" * 10)
    for num, freq in frequency_map.items():
        print(f"{num}\t{freq}")

def meanOfNums(numArray):
    return sum(numArray) / len(numArray)


#starts here
numbers = []
insertNumbers(numbers)
if len(numbers) == 0:
    print("No numbers entered")
    exit(-1)
numbers.sort()
print("Sorted Numbers: ")
print(numbers)

# Frequency of numbers list
numFrequencies(numbers)

#mean
print("Mean: ")
print(meanOfNums(numbers))

#Median
print("Median: ")
# print(medianOfNums(numbers))
print(statistics.median(numbers))

# standard deviation
print("Standard Deviation: ")
print(statistics.stdev(numbers))

print("Variance: ")
print(statistics.variance(numbers))
