# # #============List================
# # # # # # # alist=[2.5,True,"a",'b']
# # # # # # # print(alist)
# # # # # # s="how are you"
# # # # # #
# # # # # # print(s[4:10])
# # # # # #
# # # # # #
# # # # # #
# # # # # slist=['praveen','tushar','sumit']
# # # # # print(slist[2])
# # # # # slist=['praveen','tushar','sumit']
# # # # # slist[1]="vishal"
# # # # # print(slist)
# # # # # slist=['praveen','tushar','sumit']
# # # # # slist.append("vishal")# append only add any word in last
# # # # # print(slist)
# # # # slist=['praveen','tushar','sumit']
# # # # slist.insert(2,'amit') #insert add any data type in any place in list
# # # # print(slist)
# # # #nested list
# # # # s=[1,2,3,[4,5,6],7,8,]
# # # # s[3].insert(2,"hlo")
# # # # print(s)
# # # # s=[1,2,3,[4,5,6],7,8,]
# # # # del s[2] # delete element form index number used
# # # # print(s)
# # # # s=[1,2,3,[4,5,6],7,8,]
# # # # s.remove(8)# delete element not give the index number
# # # # print(s)
# # # # s=[1,2,3,[4,5,6],7,8,]
# # # #
# # # # # print(len(s))#find length of your list
# # # # s=[1,2,3,[4,5,6],1,1,]
# # # # s.count(1)# count the number of repid number
# # # # print(s.count(1))
# # #============Tuple =====================
# # # # s=(1,2,3,4,6,5)#tuple() tuple are not ussed any types of operater
# # # # s1=(9,8,7)
# # # # step1=(s)+(s1)# add tow tuple in single line
# # # # print(step1)
# # # # num=(input("Enter the number"))
# # # # num=num+2
# # # # print(num)
# # # #step 2 add the tow tuple
# # # # s=(1,2,3,4,5)
# # # # s=list(s)
# # # # print(s)
# # # # s.append("15")
# # # # print(s)
# # # # s=tuple(s)
# # # # print(s)
# # # num=[1,2,3,4,6]
# # # num2=(111,122,113,41,35,)
# # # s1=len(num)
# # # print(s1)
# # #
# # # s2=len(num2)
# # # print(s2)
# # # if s1<s2:
# # #     print("This is a list")
# # # else:
# # #     print("This is a tuple")
# # #========qustion list==========
# # # s=[1,2,3,5,7,8,]
# # # print(s)
# # #
# # # print(s.index(5))
# # # s[3]=200
# # # print(s)
# # # s=int(input("Enter the number"))
# # # count=0
# # #
# # # while s !=0:
# # #     s//=10
# # #     count+=1
# # # print("Total number",count)
# # # s=[1,2,3,5,6]
# # # len(s)
# # # print(s)
# # # start=len(s)-1
# # # step=-1
# # # stop=-1
# # # for i in range(start,step,stop):
# # #     print(s[i])
# # # for i in range(-10,0,1):
# # #     print(i)
# # # print("Your qustion")
# # # num=int(input("Enter the number"))
# # # fact=1
# # # if num<0:
# # #     print("Your number")
# # # elif num==0:
# # #     print("Result are nout found")
# # #
# # # else:
# # #     for i in range(1,num+1):
# # #         fact=fact*i
# # #     print(fact)
# # # l=[1,2,3,4,5,6]
# # #
# # # for i in l[1::2]:
# # #     print("This is your odd number",i)
# #
# # # num=int(input("Enter the number"))
# # # cube=1
# # # if num<0:
# # #     print("Your number")
# # # elif num==0:
# # #     print("Result are nout found")
# # #
# # # else:
# # #     for i in range(1,num+2):
# # #         cube=cube*i
# # #     print(cube)
# # #
# # #
# # num1=int(input("Enter the number"))
# # num2=3
# # num3=num1**num2
# # print(num3)
# #
# # num=input("type yor qustion")
# # num1 =num.split()
# #
# # print(num1)
# # num3=[]
# # for i in range(len(num1)):
# #     num1[i]=int(num1[i])
# #     num3.append(num1[i])
# # print(num3)
#
# # 3 fizz , 5 buzz, 3 and 5 both fizz buzz
# # num= int(input("Enter your number"))
# #
# # for num in range (int(num)):
# #   if num%3==0:
# #     print("Fizz")
# #   elif num%5==0:
# #     print("Buzz")
# #   elif num%3 ==0 and num% 5==0:
# #     print("fizz buzz")
# #   else:
# #     print(num)
# # print(num)
# # list program squre of the list
# l=input("Enter your list")
# num=list(l)
# print(num)
# # num1=l*2
# print(len(num)*2)
#
# for num in range (len(l)*2):
#     print(num)
# l=[1,2, 3]
# print(l)
# l=[x*x for x in l]
# print(l)
#
# l=[1,2, 3]
# print(l)
# l=[x*x for x in l]
# print(l)

l=["hello","i"]
l1=["dear","am"]

l2=[l,l1]
print(l2)

# for i in range (l,l1):
#
#     print(i)
