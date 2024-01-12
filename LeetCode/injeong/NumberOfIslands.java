package LeetCode.injeong;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

/*200.섬의 개수*/

public class NumberOfIslands {
    public static void main(String[] args) throws IOException {
        //BufferedReader는 Scanner에 비해 성능이 빠르다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String line = br.readLine(); // 전체 입력을 한줄로 받음.
        line = line.substring(1,line.length()-1); //양끝에 대괄호 제거함.
        String[] rows = line.split("\\],\\["); //],[을 기준으로 행을 구분한다.
        String[][] grid = new String[rows.length][]; // 행의 수에 맞게 그리드 초기화
        int row = 0; //행
        int col = 0; //열

        for(String rowData : rows){
            rowData = rowData.replace("\"",""); //쌍따옴표 제거
            String[] cols = rowData.split(","); //쉼표로 열 구분
            grid[row] = cols; // 행데이터를 그리드에 할당
            row++; //
        }
        int x = grid.length;//행의 수
        int y = grid[0].length; //열의 수

        int islandCount = countIslands(grid, x, y);//섬의 개수를 계산하는 메서드를 호출한다.

        bw.write(String.valueOf(islandCount)); //섬의 개수 출력
        //write메서드는 문자열을 인자로 받기때문에 int타입은 String으로 변환해줘야한다.
        bw.newLine(); //새 줄을 시작한다.

        br.close();//BufferedReader객체를 닫는다.
        bw.close();//BufferedWriter객체를 닫는다.
        //왜?
    }

    private static int countIslands(String[][] grid, int rows, int cols) {
        int count = 0;//섬의 개수를 세는 변수를 초기화한다.
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j].equals("1")) {//현재 위치가 '1'(육지)라면,
                    dfs(grid, i, j, rows, cols);//dfs를 실행시킨다.
                    count++; //섬의 개수를 증가시킨다. 1이 있으면 일단 무조건 섬은 최소 1개니까..! 바로 ++해줘버림
                }
            }
        }
        return count; //반복문이 끝나면 계산된 섬의 총 개수가 나온다.
    }

    private static void dfs(String[][] grid, int i, int j, int rows, int cols) {
        if (i < 0 || i >= rows || j < 0 || j >= cols || grid[i][j].equals("0")) {
            //i: 행 인덱스, j:열 인덱스
            //배열의 경계를 넘어가거나,물("0")을 만나면 return한다.
            return;
        }

        grid[i][j] = "0"; // 현재의 위치를 '0'으로 표시하여 방문했음을 나타낸다.

        //인접한 네 방향으로 dfs를 재귀호출한다.
        dfs(grid, i - 1, j, rows, cols);
        dfs(grid, i + 1, j, rows, cols);
        dfs(grid, i, j - 1, rows, cols);
        dfs(grid, i, j + 1, rows, cols);
    }
}