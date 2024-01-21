import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

lateinit var visit: IntArray
lateinit var arr:Array<BooleanArray>
fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
    val numOfp = br.readLine().toInt()
    visit = IntArray(numOfp+1)
    val finds = br.readLine().split(" ").map { it.toInt() }.toIntArray()
    val numOfRelation = br.readLine().toInt()
    arr = Array(numOfp+1){BooleanArray(numOfp+1)}
    for (i in 0..<numOfRelation){
        val relation = br.readLine().split(" ").map { it.toInt()}.toIntArray()
        arr[relation[0]][relation[1]] = true
        arr[relation[1]][relation[0]]= true
    }
    br.close()
    numberOfRelatives(arr, finds[0],0, numOfp)
    if(visit[finds[1]]!=0){
        println(visit[finds[1]])
    }else{
        println(-1)
    }
}

fun numberOfRelatives(array: Array<BooleanArray>,num:Int, count:Int, end:Int){
    for (i in 1..end){
        if (array[num][i]){
            array[i][num] = false
            if (visit[i]!=0){
                visit[i]=min(visit[i], count+1)
            }else {
                visit[i] = count+1
            }
            numberOfRelatives(array, i, count+1, end)
        }
    }
}