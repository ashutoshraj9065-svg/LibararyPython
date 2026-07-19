# numbers = [10, 20, 30, 40, 50]
# count=0
# sum=0
# largest=numbers[0]

# for i in numbers:
#     count=count+1
# print(count)

# for i in numbers:
#     sum=sum+i
# print(sum)
 
# for i in numbers:
#     if i>largest:
#         largest=i

# print(largest)


# numbers = [18, 7, 25, 3, 12]
# smallest=numbers[0]

# for i in numbers:
#     if smallest>i:
#         smallest=i
# print(smallest)

numbers = [10, 20, 30, 40, 50]
largest=numbers[0]
secondlargest=numbers[0]

for i in numbers:
    if i>largest:
         secondlargest=largest
         largest=i
      
print(secondlargest)
print("error")