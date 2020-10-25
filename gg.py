
#40697639
def counttriangle(A):
    n=len(A)
    count=0
    for i in range(n-2):
        # j=n-2-i
        # count+=(n-i+2)*i
        # count+=(i)*n
        for j in range(i+1,n):
            k = min(i+j+1,n)
            print(i,j,k,count)
            count+=k-j-1
    print(count)



tests= int(input())
for i in range(tests):
    n = int(input())
    array = [_+1 for _ in range(n)]
    counttriangle(array)
