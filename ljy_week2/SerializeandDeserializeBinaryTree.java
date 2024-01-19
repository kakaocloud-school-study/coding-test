public class Codec {
    // 교재 풀이
    // Solve fail
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return ""; // 예외 처리

        // bfs를 위한 큐 선언
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        // 직렬화 결과 변수
        StringBuilder sb = new StringBuilder();
        sb.append(String.valueOf("[" + root.val));

        // bfs
        while(!q.isEmpty()) {
            // 현재 노드 추출
            TreeNode node = q.poll();

            // 큐 삽입
            if (node.left != null) {
                q.add(node.left);
                sb.append(","+node.left.val);
            } else {
                sb.append(",null");
            }

            if (node.right != null) {
                q.add(node.right);
                sb.append(","+node.right.val);
            } else {
                sb.append(",null");
            }
        }

        sb.append("]");
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.equals("")) return null; // 예외 처리

        // 문자열 자르기
        String[] nodes = data.substring(1, data.length() - 1).split(",");
        // 인덱스 0번이 루트
        TreeNode root = new TreeNode(Integer.parseInt(nodes[0]));
        // 직렬화와 동일하게 BFS로 역직렬화 처리 위한 큐 선언
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        // 루트를 제외하고 인덱스 1번부터 시작
        int index = 1;

        while (!q.isEmpty()) {
            // 노드 추출
            TreeNode node = q.poll();

            // 인덱스가 null이 아니면 왼쪽, 오른쪽 자식 노드로 설정하고 큐에 추가. 각각 인덱스 ++1;
            if (!nodes[index].equals("null")) {
                node.left = new TreeNode(Integer.parseInt(nodes[index]));
                q.add(node.left);
            }

            index++;

            if (!nodes[index].equals("null")) {
                node.right = new TreeNode(Integer.parseInt(node[index]));
                q.add(node.right);
            }

            index++;
        }

        return root;
    }

    // Definition for a binary tree node.
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
}



    // Your Codec object will be instantiated and called as such:
    Codec ser = new Codec();
    Codec deser = new Codec();
    Codec.TreeNode ans = deser.deserialize(ser.serialize(root));