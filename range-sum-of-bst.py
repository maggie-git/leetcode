class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def cal(root,res):
            if root.val >= L and root.val <= R:
                res.append(root.val)
            if root.val <= L and root.right:
                cal(root.right,res)
            elif root.val >= R and root.left:
                cal(root.left,res)
            else:
                if root.right:
                    cal(root.right,res)
                if root.left:
                    cal(root.left, res)
                    

        if not root:
            return 0
        res = []
        cal(root,res)
        return sum(res)
