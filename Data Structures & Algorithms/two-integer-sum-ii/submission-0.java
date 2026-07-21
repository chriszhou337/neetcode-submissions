class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int index1 = 0, index2 = numbers.length - 1;

        while (index1 < index2) {
            int test = numbers[index1] + numbers[index2];

            if (test == target) {
                break;
            }
            else if (test < target) {
                index1++;
            }
            else if (test > target) {
                index2--;
            }
        }

        return new int[] {index1 + 1, index2 + 1};
        
    }
}
