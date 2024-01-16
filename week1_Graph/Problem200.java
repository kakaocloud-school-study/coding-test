class Solution {
    int[] drArr = {0, 1, 0, -1};
    int[] dcArr = {1, 0, -1, 0};

    public int numIslands(char[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];

        int count = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (visited[i][j] == true || grid[i][j] == '0') {
                    continue;
                }
                count++;
                search(grid, visited, i, j);
            }
        }

        return count;
    }

    private void search(char[][] grid, boolean[][] visited, int i, int j) {
        for (int d = 0; d < 4; d++) {
            int dr = drArr[d];
            int dc = dcArr[d];

            int ni = i + dr;
            int nj = j + dc;

            if (ni < 0 || ni >= grid.length || nj < 0 || nj >= grid[ni].length || visited[ni][nj] == true || grid[ni][nj] == '0') {
                continue;
            }

            visited[ni][nj] = true;
            search(grid, visited, ni, nj);
        }
    }
}