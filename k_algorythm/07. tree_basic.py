# 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
# 변수
node1 = TreeNode()
node1.data = "민지"

node2 = TreeNode()
node2.data = "혜린"
node1.left = node2

node3 = TreeNode()
node3.data = "해인"
node1.right = node3

node4 = TreeNode()
node4.data = "다니엘"
node2.left = node4

node5 = TreeNode()
node5.data = "나연"
node2.right = node5

node6 = TreeNode()
node6.data = "모모"
node3.left = node6
# 메인

# 출력

root = node1

print(root.data)
print(root.left.data, root.right.data)
print(root.left.left.data, root.left.right.data, root.right.left.data)