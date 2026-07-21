class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        System.out.println(map);

        for (int i = 0; i < nums.length; i++) {
            int find = target - nums[i];

            if (map.containsKey(find) && map.get(find) != i) {
                int index1 = i,
                index2 = map.get(find);

                return new int[]{index1, index2};
            }
        }

        return new int[0];
    }
}
