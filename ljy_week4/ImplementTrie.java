// 교재 풀이
class TrieNode {
    // 단어 완성 여부
    boolean word;
    TrieNode[] children;

    public TrieNode() {
        // 문제 제약 조건에 따라 소문자 알파벳으록 구성되므로 자식 노드는 알파벳의 개수인 26개까지 가능
        children = new TrieNode[26];
        word = false;
    }
}

class Trie {

    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        // 루트 노드부터 시작
        TrieNode cur = root;
        // 단어 문자를 차례대로 반복하며 자식 노드 구성
        for (char c : word.toCharArray()) {
            // 해당 문자의 자식 노드가 존재하지 않으면 신규 트라이 노드 생성
            if (cur.children[c - 'a'] == null) {
                cur.children[c - 'a'] = new TrieNode();
            }
            // 자식 노드를 현재 노드로 교체
            cur = cur.children[c - 'a'];
        }
        cur.word = true;
    }

    public boolean search(String word) {
        // 루트부터 시작
        TrieNode cur = root;
        // 단어의 문자를 차례대로 반복하며 자식 노드 구성
        for (char c : word.toCharArray()) {
            // 자식 노드가 존재하지 않으면 false 리턴
            if (cur.children[c - 'a'] == null) return false;
            cur = cur.children[c - 'a'];
        }
        // 탐색이 종료된 후 단어 완성 여부를 리턴
        return cur.word == true;
    }

    public boolean startsWith(String prefix) {
        // 루트부터 시작
        TrieNode cur = root;
        // 단어의 문자를 차례대로 반복하며 자식 노드 구성
        for (char c : prefix.toCharArray()) {
            if (cur.children[c - 'a'] == null) return false;
            cur = cur.children[c - 'a'];
        }
        // 탐색이 종료되면 항상 true 리턴, 시작 여부만 판별하면 되므로 단어 완성 여부가 false여도 상관없음
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */