class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        p=len(arr)
        arr.sort()
        if p<2:
            return True
        r=abs(arr[0]-arr[1])
        print(r,p)
        for i in range(p-1):
            d=abs(arr[i]-arr[i+1])
            print(d,"r",r)
            if d!=r:
                print("a")
                return False
        return True
