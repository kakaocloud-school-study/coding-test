package codingTestStudy.week1
class Solution {
    val alphabet = mapOf(
        '0' to arrayOf(),
        '1' to arrayOf(),
        '2' to arrayOf('a', 'b', 'c'),
        '3' to arrayOf('d', 'e', 'f'),
        '4' to arrayOf('g', 'h', 'i'),
        '5' to arrayOf('j', 'k', 'l'),
        '6' to arrayOf('m', 'n', 'o'),
        '7' to arrayOf('p', 'q', 'r', 's'),
        '8' to arrayOf('t', 'u', 'v'),
        '9' to arrayOf('w', 'x', 'y', 'z'),
    )

    var result: MutableList<String> = mutableListOf()
    fun letterCombinations(digits: String): List<String> {
        if (digits.isEmpty()) {
            return result
        }
        var str = StringBuilder()
        bfs(0, digits, str)
        return result
    }

    fun bfs(index: Int, digits: String, str: StringBuilder) {
        if (index == digits.length) {
            result.add(str.toString().trim())
            return
        }
        for (i in alphabet[digits[index]]!!) {
            bfs(index + 1, digits, StringBuilder(str).append(i))
        }
    }
}
