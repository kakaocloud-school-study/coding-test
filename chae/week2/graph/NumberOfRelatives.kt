import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

lateinit var visit: IntArray
lateinit var arr:Array<BooleanArray>
fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
    //총 인원 저장
    val numOfp = br.readLine().toInt()
    visit = IntArray(numOfp+1)
    //촌수를 구할 대상1와 대상2 저장배열
    val finds = br.readLine().split(" ").map { it.toInt() }.toIntArray()
    //부모와 자식 관계 갯수
    val numOfRelation = br.readLine().toInt()
    //부모와 자식임 관계임을 저장할 array
    arr = Array(numOfp+1){BooleanArray(numOfp+1)}
    for (i in 0..<numOfRelation){
        //부모와 자식 노드를 true로 변경
        val relation = br.readLine().split(" ").map { it.toInt()}.toIntArray()
        arr[relation[0]][relation[1]] = true
        arr[relation[1]][relation[0]]= true
    }
    br.close()
    //대상1에서 시작
    numberOfRelatives(arr, finds[0],0, numOfp)
    //대상2에 도달했다면(0이 아님) 값 출력 못했다면 -1 출력
    if(visit[finds[1]]!=0){
        println(visit[finds[1]])
    }else{
        println(-1)
    }
}

fun numberOfRelatives(array: Array<BooleanArray>,num:Int, count:Int, end:Int){
    for (i in 1..end){
        //for문을 돌며 촌수를 맺어진 대상을 찾음
        if (array[num][i]){
            array[i][num] = false
            if (visit[i]!=0){
                visit[i]=min(visit[i], count+1)
            }else {
                visit[i] = count+1
            }
            // 촌수 맺어진 대상과 촌수 맺은 대상을 찾아다님
            numberOfRelatives(array, i, count+1, end)
        }
    }
}