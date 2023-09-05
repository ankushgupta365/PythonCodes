# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        #serializing in preorder
        res = []
        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res) #making string from array of strings with a comma after every value

            
        

    def deserialize(self, data):
        #deserializing in preorder
        vals = data.split(",") #array of strings from comma separated input single string
        self.i = 0  #global incrementor variable
        def dfs():
            if vals[self.i] == "N":
                self.i +=1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i+=1  
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))