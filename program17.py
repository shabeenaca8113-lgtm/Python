colors=input("Enter color names separated by commas:").split(",")
colors=[color.strip() for color in colors]
print("first color:",colors[0])
print("Last color:",colors[-1])
