class TreeNode:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


class BinarySearchTree:
    def __init__(self):
        self.head=None

    def inorder(self,root):
        if self.head==None:
            print("Empty Tree")
            return
        if root!=None:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.data,end=" ")
    def insertfunc(self,value):
        def insert(value,root=self.head):
            if root==None:
                root=TreeNode(value)
            elif root.data>value:
                root.left=insert(value,root.left)
            elif root.data<value:
                root.right=insert(value,root.right)
            else:
                print("Element already inserted, duplicates are not allowed!!")
            return root
        self.head=insert(value)
    def deletefunc(self,value):
        def delete(value,root=self.head):
            if root==None:
                return root
            elif root.data<value:
                root.right=delete(value,root.right)
            elif root.data>value:
                root.left=delete(value,root.left)
            else:
                if root.left==None and root.right==None:
                    root=None
                elif root.left and not root.right:
                    root=root.left
                elif root.right and not root.left:
                    root=root.right
                else:
                    temp=root
                    temp=temp.right
                    while temp.left!=None:
                        temp=temp.left
                    root.data=temp.data
                    val=temp.data
                    root.right=delete(val,root.right)
            return root
        self.head=delete(value)


tree=BinarySearchTree()
tree.inorder(tree.head)
tree.insertfunc(5)
tree.insertfunc(1)
tree.insertfunc(2)
tree.insertfunc(8)
tree.insertfunc(7)
tree.insertfunc(4)
tree.insertfunc(4)
tree.inorder(tree.head)
print()
tree.deletefunc(5)
tree.inorder(tree.head)







