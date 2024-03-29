class Solution {
    static class TrieNode {
        // 단어 ID를 저장하는 변수
        int wordId;
        // 트라이의 자식 노드들
        TrieNode[] children;
        // 팰린드롬인 단어 ID를 목록으로 저장하는 변수
        List<Integer> palindromeWordIds;

        public TrieNode() {
            // 단어 ID의 초깃값은 의미 없는 값으로 선언
            wordId = -1;
            children = new TrieNode[26];
            palindromeWordIds = new ArrayList<>();
        }
    }

    static class Trie {
        TrieNode root;

        public Trie() {
            root = new TrieNode();
        }

        // 인덱스를 받아 팰린드롬 여부를 판단하는 메소드
        public boolean isPalindrome(String str, int start, int end) {
            while (start < end) {
                if (str.charAt(start++) != str.charAt(end--)) return false;
            }
            return true;
        }

        public void insert(int index, String word) {
            TrieNode cur = root;
            // 단어를 뒤집어서 트라이로 저장
            for (int i = word.length() - 1; i >= 0; i--) {
                // 단어에서 해당 위치의 문자 추출
                char c = word.charAt(i);
                // 정방향으로 해당 위치까지 팰린드롬인 경우 단어의 인덱스 저장(그림에서 p로 표시)
                if (isPalindrome(word, 0, i)) {
                    cur.palindromeWordIds.add(index);
                }
                // 해당 문자의 자식 노드가 존재하지 않으면 신규 트라이 노드 생성
                if (cur.children[c - 'a'] == null) {
                    cur.children[c - 'a'] = new TrieNode();
                }
                cur = cur.children[c - 'a'];
            }
            cur.wordId = index;
        }

        // 팰린드롬 여부 판별
        public List<List<Integer>> search(int index, String word) {
            TrieNode cur = root;
            List<List<Integer>> result = new ArrayList<>();

            // 단어의 문자를 차례대로 반복하며 처리
            for (int j = 0; j < word.length(); j++) {
                // 탐색 중에 단어 ID가 있고 나머지 문자가 팰린드롬인 경우
                if (cur.wordId >= 0 && isPalindrome(word, j, word.length() - 1)) {
                    result.add(Arrays.asList(new Integer[]{index, cur.wordId}));
                }
                // 자식 노드가 없으면 더 이상 팰린드롬이 아니므로 지금까지의 결과를 리턴하면서 중단
                if (cur.children[word.charAt(j) - 'a'] == null) {
                    return result;
                }
                // 자식 노드를 현재 노드로 교체
                cur = cur.children[word.charAt(j) - 'a'];
            }
            // 끝까지 탐색했을 때 단어 ID가 있는 경우
            if (cur.wordId >= 0 && cur.wordId != index) {
                result.add(Arrays.asList(new Integer[]{index, cur.wordId}));
            }
            // 끝까지 탐색했을 때 팰린드롬 단어 ID가 있는 경우
            for (int palindromeWordId : cur.palindromeWordIds) {
                result.add(Arrays.asList(new Integer[]{index, palindromeWordId}));
            }
            return result;
        }
    }
    public List<List<Integer>> palindromePairs(String[] words) {
        // 트라이 처리 클래스
        Trie t = new Trie();
        // 결과 리스트 변수
        List<List<Integer>> results = new ArrayList<>();
        // 단어 목록을 하나씩 트라이에 추가
        for (int i = 0; i < words.length; i++) {
            t.insert(i, words[i]);
        }
        // 단어 목록에서 하나씩 팰린드롬 여부를 판별하고 결과에 누적
        for (int i = 0; i < words.length; i++) {
            results.addAll(t.search(i, words[i]));
        }

        return results;
    }
}