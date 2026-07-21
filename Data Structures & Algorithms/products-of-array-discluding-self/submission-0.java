class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        int[] postfix = new int[nums.length];
        int[] solution = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                prefix[i] = 1;
                continue;
            }
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        for (int i = nums.length - 1; i >= 0; i--) {
            if (i == nums.length - 1) {
                postfix[i] = 1;
                continue;
            }
            postfix[i] = postfix[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < nums.length; i++) {
            solution[i] = prefix[i] * postfix[i];
        }

        return solution;
    }
}  
