package ljy_week2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Baekjoon2644 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 전체 사람의 수
        String[] two = br.readLine().split(" "); // 촌수 계산해야하는 두 사람
        int m = Integer.parseInt(br.readLine()); // 부모 자식 관계 수

        List<String[]> pcList = new ArrayList<>(); // 부모 자식 관계를 담을 리스트

        for (int i = 0; i < m; i++) {
            String[] pc = br.readLine().split(" ");
            pcList.add(pc);
        }

        // 그래프를 만들 맵
        HashMap<Integer, List<Integer>> map = new HashMap<>();

        for (String[] pc : pcList) {
            int p = Integer.parseInt(pc[0]);
            int c = Integer.parseInt(pc[1]);

            map.putIfAbsent(p, new ArrayList<>());
            map.putIfAbsent(c, new ArrayList<>());

            map.get(p).add(c);
            map.get(c).add(p);

        }

        System.out.println(getDiv(map, new ArrayList<>(), Integer.parseInt(two[0]), Integer.parseInt(two[1])));
    }

    private static int getDiv(HashMap<Integer, List<Integer>> map, List<Integer> visited, int start, int end) {
        // 시작과 끝이 같을 경우 0 반환
        if (start == end) return 0;
        // 방문한 리스트에 시작 추가
        visited.add(start);
        // 시작과 연결된 노드 순회
        // 방문한 경우 넘어간다.
        // 방문하지 않은 경우 경로가 있는 지 확인하고 있다면 경로 + 1.
        for (int num : map.get(start)) {
            if (visited.contains(num)) continue;
            int d = getDiv(map, visited, num, end);
            if (d != -1) return d + 1;
        }
        // 경로가 없는 경우 -1 반환
        return -1;
    }
}
