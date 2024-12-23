from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    bigNumber = max(candies)
    return [candy + extraCandies >= bigNumber for candy in candies]

print(kidsWithCandies([2,3,5,1,3],3)) #Output: [true,true,true,false,true] 
print(kidsWithCandies( [4,2,1,1,2],1)) #Output: [true,false,false,false,false] 