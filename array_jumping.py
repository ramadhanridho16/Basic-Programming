# -*- coding: utf-8 -*-
"""
Have the function ArrayJumping(arr) take the array of numbers stored in arr
and first determine the largest element in the array,
and then determine whether or not you can reach that same element within
the array by moving left or right continuously according to whatever integer
is in the current spot. If you can reach the same spot within the array,
then your program should output the least amount of jumps it took.

For example: if the input is [2, 3, 5, 6, 1] you'll start at the spot where
6 is and if you jump 6 spaces to the right while looping around the array you
end up at the last element where the 1 is. Then from here you jump 1 space to
the left and you're back where you started, so your program should output 2.
If it's impossible to end up back at the largest element in the array your
program should output -1. The largest element in the array will never equal
the number of elements in the array. The largest element will be unique. 

Input:1,2,3,4,2
Output:3

Input:1,7,1,1,1,1
Output:2
"""
#Assume max is unique
#Max doesn't equal len(arr) >- output > 1
#Positive integers only

def ArrayJumping(arr):
    
    ht = {}     # hash table
    max_index = arr.index(max(arr)) # Letak nilai terbesar dalam array
    print("max_index :", max_index)
    L = len(arr)        # panjang array
    
    for i in range(L):      # iterable i dari panjang L dimulai dari 0 < L
        print("This is L(length) variable : ", L)
        print("This is i(index) variable : ", i)
        print("This is arr[i](number) variable : ", arr[i])
        ht[i] = (left(L,i,arr[i]),right(L,i,arr[i]))    # Inisialisasi variable 2 digit
        print("This is ht[i] : ", ht[i])
        print("-----------------")

    if max_index in ht[max_index]:
        print("max_index : ", max_index)
        print("ht[max_index] : ", ht[max_index])
        return 1
    # print("-----------------")
    travel_set = set(ht[max_index])  
    print("Travel_set : ", travel_set)
    
    for step in range(2,L+1):
        print("Step variable : ", step)
        for val in tuple(travel_set):
            print("val variable : ", val)
            travel_set.add(ht[val][0])
            travel_set.add(ht[val][1])
        print("Travel_set_finale : ", travel_set)
        if max_index in travel_set:
            return step
    return -1
        

def left(length,index,number):
    left = number % length      # inisialisasi variable left, number modulo panjang karakter
    print("This is left variable : ", left) 
    if left > index:            # jika varialbe left > index maka panjang + index - kiri
        result = length + index - left
    else:
        result = index - left
    print("result of left function ", result)
    return result

def right(length,index,number):
    right = number % length
    print("This is right variable : ", right)
    if right > length - index - 1:
        result = right + index - length
    else:
        result = right + index
    print("result of right function ", result)
    return result

# print("This information that contain in this code are: ", ArrayJumping([9, 5, 0, 0, 0, 6]))
print("This information that contain in this code are: ",
      ArrayJumping([0, 2, 1, 2, 0, 0]))
# print("This information that contain in this code are: ",
#       ArrayJumping([1, 7, 1, 9, 4, 5]))
# print("This information that contain in this code are: ", ArrayJumping([1, 2, 1, 4]))
