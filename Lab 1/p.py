#
#
#
# def bubbleSort(arr):
#     n = len(arr)
#     print n
#
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# str = raw_input()
# strArr = list(str)
# print strArr
# bubbleSort(strArr)
#
# sortedStr = ''.join(strArr)
#
# print strArr
# print sortedStr


mat = [[0, 0, 1, 0, 0],
       [0, 0, 1, 1, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 1, 0],
       [0, 0, 1, 0, 0],
      ]
print mat

length = len(mat)
count = 0
level = 1

for i in range(length):
    print "count", count
    for j in range(length):
        if( ((i>0)and(j>0))and((i<length-1)and(j<length-1)) ):
            if mat[i][j] == 1:
                print i , j
                print "i-level:", i-level
                print "i+level:", i+level
                print "j-level:", j-level
                print "j+level:", j+level
                print "(i-level >= 0 and i+level >= length-1 and j-level >= 0 and j+level >= length-1 )", (i-level >= 0 and i+level >= length-1 and j-level >= 0 and j+level >= length-1 )

                print ""
                while(i-level >= 0 and i+level <= length-1 and j-level >= 0 and j+level <= length-1 ):
                    print "(mat[i-level][j] and mat[i+level][j])and(mat[i][j-level] and mat[i][j+level])", (mat[i-level][j] and mat[i+level][j])and(mat[i][j-level] and mat[i][j+level])
                    if((mat[i-level][j] and mat[i+level][j])and(mat[i][j-level] and mat[i][j+level])):
                        count+=1
                        level+=1
                    else:
                        level = 1
                        break

print count
