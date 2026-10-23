scores = list(map(int, input("Enter scores separated by spaces: ").split()))

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Scores:", scores)
print("Sum:", total)
print("Average:", average)
print("Maximum score:", maximum)
print("Minimum score:", minimum)
