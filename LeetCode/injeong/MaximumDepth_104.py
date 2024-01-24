# Definition for a binary tree node.
#__init__은 파이썬 클래스의 생성자 함수.
#객체가 생성될 떄 자동호출됨
#'__init__'함수는 첫번째 인자로 항상 'self'를 받음
#self는 클래스의 인스턴스를 참조하는 변수
#클래스 내부의 메소드를 정의할때, 첫번째 인자로 self를 명시해줘야함.

#LeetCode에서는 내부에서 이진트리를 만들어주지만, IDE에서는 직접 이진트리를 구축해서 확인해야됨.
#공부할겸, 이진트리 구축코드 이해해보기.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """이진트리 깊이 탐색"""
    def maxDepth(self, root):
        def dfs(node):
            if not node:
                #현재 노드가 없으면 깊이 0 반환
                return 0
            #max(x1,x2,x3...) -> 가장 큰 인자값을 반환함.
            print(dfs(node.left))
            print(dfs(node.right))
            return 1 + max(dfs(node.left), dfs(node.right))

        return dfs(root)

def buildTree(level_order):
    # 리스트가 비어있으면 None을 반환하여 빈 트리를 나타냄.
    # 다른 언어에서 null이 파이썬에서는 None이다.
    if not level_order:
        return None

    #리스트의 첫번째 원소가 root노드의 값
    root = TreeNode(level_order[0])
    #큐를 초기화하고 처음엔 루트노드만 포함한다.
    queue = [root]
    #리스트의 두번째 원소부터 시작하도록 함. 첫번째원소는 root로 지정해줬으니까.
    i = 1


    while i < len(level_order):
        #큐는 FIFO구조다. 먼저들어간 요소가 가장 먼저 나온다.
        # 큐에서 현재 노드를 꺼낸다.
        current = queue.pop(0)

        #왼쪽 자식 노드 추가
        if i < len(level_order) and level_order[i] is not None:
            current.left = TreeNode(level_order[i])
            queue.append(current.left)
        #다음 원소로 이동
        i += 1

        #오른쪽 자식 노드 추가
        if i < len(level_order) and level_order[i] is not None:
            current.right = TreeNode(level_order[i])
            queue.append(current.right)
        i += 1

    #
    return root

# 입력값
input_list = [3, 9, 20, None, None, 15, 7]

# 이진 트리 구축
root = buildTree(input_list)

# Solution 클래스의 인스턴스 생성
sol = Solution()

# 최대 깊이 계산 및 출력
print(sol.maxDepth(root))
