import array as arr
#Write a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array. Also, print the reversed array.
arr_num= arr.array('i',[1, 3, 5, 3, 7, 9, 3])
print("The number of times 3 occurs in the array is ",arr_num.count(3))
arr_num.reverse()
print(str(arr_num))
