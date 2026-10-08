list1=list(map(int,input("Enter first list of integers:").split()))
list2=list(map(int,input("Enter second list of integers:").split()))
if len(list1)==len(list2):
   print("Both lists have the same length")
else:
    print("Both lists do not have the same length")
if sum(list1)==sum(list2):
   print("Both lists have the same sum")
else:
    print("Both lists do not have the same sum.")
if any(value in list2 for value in list1):
   print("atleast one value occurs in both lists.")
else:
   print("No value occurs in both lists.")
