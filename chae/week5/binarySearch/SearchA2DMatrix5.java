package codingTestStudy.week5.binarySearch;

public class SearchA2DMatrix5 {
    public boolean searchMatrix(int[][] matrix, int target) {
        int arrayRow = matrix.length;
        int row = 0;
        int col = matrix[0].length-1;
        while (row<arrayRow && col>=0){
            int value = matrix[row][col];
            if (value ==target){
                return true;
            }else if (value <target){
                row++;
            }else {
                col--;
            }
        }
        return false;
    }
}
