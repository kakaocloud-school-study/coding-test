package codingTestStudy.week6.slidingWindow;

class Solution {
    fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
        var maxIndex = -1
        var max = nums[0]-1
        val size = nums.size-k
        var result = IntArray(size+1)
        for (i in 0 ..size){
            if (maxIndex<i) {
                max = nums[i]
                for (j in i+1 until i + k) {
                    if (max<nums[j]) {
                        max = nums[j]
                        maxIndex=j
                    }
                }
            }else{
                var num = i+k-1
                if (max<nums[num]){
                    max = nums[num]
                    maxIndex = num
                }
            }
            result[i] = max
        }
        return result
    }
}