class Solution(object):
    def subtractProductAndSum(self, c):
        t=1
        k=0
        sum=0
        while(c!=0):
            k=c%10
            t*=k
            sum+=k
            c/=10
        return t-sum
        


        
