# def bank(name,pwd,amt):
#     employee={"name":["ashu","badal","banty","virat"],"password":[121,213,321,432]}

#     for i in range(len(employee["name"])):
#         if employee["name"][i]==name and employee["password"][i]==pwd:
#             return "success"
#     else:
#         return "not match"
# print(bank("badal",213,2000))

n=int(input("enter a number"))
i=1
while i<=n:
  if(i<=n-1):
    print(i,end=",")
  else:
    print(i)
  i=i+1 

