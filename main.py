#Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple
#Create a tuple with different datatypes
tuple1=(10,"catherine", 3.14, True)
print("my tuple:", tuple1)
tuple2=(5,6,7,8,10)
tuple2=tuple2+(9,)
print("the tuple after adding 9 is:",tuple2)
tuple3=(10,10,20,50,10,30,40)
print("the count of 10 in the tuple is:",tuple1.count(10))
print("from tuple 3 :",tuple3[1:4])