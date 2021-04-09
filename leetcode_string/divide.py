class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor==0 :
            return None
        if abs(divisor)==abs(dividend):
            if dividend<0 and divisor<0:
                return 1
            if dividend<0 or divisor<0:
                return -1
            return 1
        if abs(divisor)==1:
            if divisor<0 and dividend<0:
                return abs(dividend)
            elif dividend<0 or divisor<0:
                return dividend*-1
            return dividend
       
        tmp_div=abs(dividend)
        count_mins=0
        flag=False
        count_mins_loop=abs(divisor)
        if dividend<0 or divisor<0:
            flag=True
        for i in range(0,dividend):
            if tmp_div<count_mins_loop:
                break
            tmp_div-=count_mins_loop
            count_mins+=1
        if divisor<0 and dividend<0:

            return int(count_mins)
        if flag:
         return int(count_mins)*-1
       
        return int(count_mins)
if __name__=="__main__":
    s=Solution()
    print(s.divide(-2147483648,-1))