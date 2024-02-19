package codingTestStudy.week5.binarySearch

fun singleNumber(nums: IntArray): Int {
    var result = 0;
    for (i in nums) {
        result = result xor i
    }
    return result
}
fun main() {
        val array = intArrayOf(1, 1, 3, 2, 2)
        search(array)
}
