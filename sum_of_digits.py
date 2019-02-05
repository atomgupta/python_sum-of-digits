{
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        print(digitsSum(a))
        testcases-=1
        
if __name__=='__main__':
    main()
}


def digitsSum(n):
    sum1=0
    while(n!=0):
        rem=n%10
        sum1+=rem
        n=n//10
    return sum1