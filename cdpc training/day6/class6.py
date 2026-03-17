




#Input:
#First line contains L.
#Second line contains N, number of photos.
#Following N lines each contains two space separated integers W and H.
L = int(input())


N = int(input())

for i in range(N):
    W, H = map(int, input().split())

    if W < L or H < L:
        print("UPLOAD ANOTHER")

    elif W == H:
        print("ACCEPTED")

    else:
        print("CROP IT")
    #Input:
#The first line will consists of one integer T denoting the number of test cases.
#For each test case:
#1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
#2) The next line consists of N space separated integers , denoting the elements of the array A.

T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    K = K % N  
    

    result = A[-K:] + A[:-K]
    
    print(*result)
