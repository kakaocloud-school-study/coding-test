package codingTestStudy.week5.binarySearch

fun search(nums: IntArray, target: Int): Int {
    var start = 0
    var end = nums.size
    while (start <= end) {
        val mid = (start + end) / 2
        val num = nums[mid]
        if (num == target) {
            return mid
        } else if (num > target) {
            start = mid-1
        } else {
            end =  mid-1
        }
    }
    return -1
}

fun main() {
    val array = intArrayOf(1, 0, 3, 5, 9, 12)
    search(array, 9)
}