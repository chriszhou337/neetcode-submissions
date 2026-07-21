class KthLargest {
    private ArrayList<Integer> nums;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.nums = new ArrayList<>();
        for (Integer i: nums) {
            this.nums.add(i);
        }
        this.k = k;
    }
    
    public int add(int val) {
        nums.add(val);
        Collections.sort(nums);
        return nums.get(nums.size() - k);
    }
}
