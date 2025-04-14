# name=["akash","ali","zahid","nouman"]
# ls=[]

# for x in name:
#     ls.insert(0,x)

# print(ls)
# name=["akash","ali","zahid","nouman"]
# name.reverse()
# new_names=[]
# for i in name:
#      new_names.append(i[0:1].upper()+i[1:-1].lower()+i[-1].upper())
     
# print(new_names)
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
# numbers = []
# for i in list:
#     numbers.append(i)  

# print(numbers)
# Print numbers (1 to 10 )
# for i in range(1,10):
#    print(i)
# for i in range(-1, -10, -1):
#    print(i)
# odd Numbers 
# for i in range(1,10,2):
#     print(i)
# for i in range (0,11,2):
#     print(i)s
# sum of Even Numbers 
# sum=0
# for i in range(1,101):
#     sum=sum+i

# print(sum)
# square=0
# for i in range(1,11):
#     square=i**2
#     print(square)
# cube=0
# for i in range(1,10):
#     cube=i**3
#     print(cube)
# Create the Table using loop 
# numbers=int(input("Enter the numbers:"))

# for i in range(1,10):
#     print(numbers,"*",i,"=",numbers*i)
# num=int(input("Enter the number:"))
# factorail=1
# for i in range(1,num+1):
#     factorail=factorail*i

# print(factorail)
# list=[1,2,3,4,5,6,7,8]
# sum=0      
# for i in range(len(list)+1):
#     sum=sum+i

# print(sum)
# print('Hello World')
# print("Hello World")
# Even Numbers
# list=[1,2,3,4,5,6,7,8]
# for i in list:
#     if i % 2==0:
#        print("Even Numbers :",i)
# tuple
# tuple=("Hello" ," World")  
# print(tuple)  
# indexing in python 
# Tuple=("hello","world")
# print(Tuple[1])
# Tuple=("hello","world")
# print(Tuple[0])   
# tuple=(1,2,3,4,5,6,7,8,9,10)
# print((tuple)[1:])
# Tuple=("hello","world")
# print(Tuple[3:5])
# Constructor 
# tp=tuple(("Hello",))

# ls=list((tp))

# print(ls)
# tp=tuple(("Hello"))

# ls=list((tp))

# print(ls)
# tp=tuple(("Hello",))
# ls=list((tp))
# ls.append("guru99")
# print(ls)
# Cities_name=tuple(("lahore","karachi","bhakkar"))
# ls=list((Cities_name))
# list=[]
# for i in ls:
#     p=(i[0:1].upper()+i[1:].lower())
#     list.append(p)
# print(tuple((list)))
# tup1=("Faisslabad","Jaranwala","Lahore")

# tup2=(1,2,3,4,5,6)    

# temp= tup1
# tup1=tup2
# tup2=temp

# print(tup2+tup1)    
# tup1=("Faisslabad","Jaranwala","Lahore")
# tup2=(1,2,3,4,5,6) 
# tup3=tup2+tup1
# print(tup3)
# tup3=(tup3[6:]+tup3[0:6])
# print(tup3)
# # Remove the Duplication in the list
# list=[1,2,3,4,5,6,7,8,8,9,9]
# UniqueList=[]
# for i in list:
#     if i not in UniqueList:
#       UniqueList.append(i)
# print(UniqueList)
# Dictionary in the python
# info={
#     "name":"Nouman",
#     "Age":"21",
#     "Father_name":"Abdul Rasheed"
# }
# print(info)
# Funcation 
# def sqrt(x):

#     for i in range(1000):
#         if i*i == x:
#             return i
        
#     return 'Not found'

# print(sqrt(1200))
# def climbStairs(n):
#     totalWays=0
#     n1=1
#     n2=1
#     # totalWays=n1+n2
#     if n==1:
#         return 1
#     else:
#         for i in range(1,n):
#             totalWays= (n1+n2)
#             print(n1,n2,totalWays)
#             n1=n2
#             n2=totalWays
   
#     return totalWays

# print(climbStairs(1))
#  list=[1,2,3,4,5,6,7,8,9,10]
#  print(list[0:-1])
# st="Hello class of Ai"
# print(st.split("Hello"))
# st=st.split(" ")
# newst= [word.capitalize() for word in st]
# print(newst)

# def sum(a,b,ls):
#     result= a+b

#     print(result,ls)
    

# sum(2,4,[2,3,4,5])

# sum(5,3,[4,5,4])

# ls=[2,3,4]

# print(ls[2:1])

# lp=('hello'),

# print(type(lp))

# str="hellow world"
# a=4
# b=3
# st='hello my name is {} and I live in {}. I\'ve {} books '.format('ali',"Lahore",9)
# st='hello my name is {0} and I live in {0}. I\'ve books '.format('ali',"Lahore",9)
# pi=3.14345
# st=f'pi value: {pi: .2f}'
# print(st)
# ls=str.split(" ")

# ls=[list(x) for x in ls ]
# print(ls)

# _first_name= 'ali'
# Funcation
# def sum():

#  a=10
#  b=20
#  print(a+b)

# sum()
# def sum (a,b):
#     print(a+b)

# sum(30,40)    
# class father:
#     def fath(self) :
#         print("Father Classes")    
# class mother:
#     def mot(self):
#         print("mother class")
# class Child(father,mother): 
#      pass

# ab=Child()      
# ab.fath()
# class Grandpa:
#    def gp(self):
#          print("Grandpa Class")
# class Parent(Grandpa):
#      def par(self):
#            print("Parent class")
# class child(Parent):
#         pass
# ab=child() 
# ab.par()   
# ab.gp()
# Single Inheritance
# class Grandpa:
#        def gp(self):
#                print("Grandpa Classes")
# class parent(Grandpa):  
#           pass

# ab=parent()    
# ab.gp()  
# multiple inheritance
# class Grandpa:
#         def gp(self):
#                 print("Granpa Classes")
# class Parent:  
#         def par(self):
#                 print("Parent Classes")             
# class child(Grandpa,Parent):
#         pass
# ab=child()
# ab.gp()
# ab.par()

# ab = slice(1,5,2)
# ls=[1,2,3,4,5,6,7,8,9,10]

# print(ls[ab])