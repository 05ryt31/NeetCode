package Trees;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> levelOrder(TreeNode root) {
        traverse(root, 0);
        return res;
    }

    private void traverse(TreeNode node, int depth) {
        if (node == null) {
            return;
        }

        if (res.size() == depth) {
            res.add(new ArrayList<>());
        }

        res.get(depth).add(node.val);
        traverse(node.left, depth + 1);
        traverse(node.right, depth + 1);
    }

    
}
