class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (Integer i: stones) {
            maxHeap.add(i);
        }

        System.out.println(maxHeap);

        while (maxHeap.size() > 1) {
            int x = maxHeap.poll();
            int y = maxHeap.poll();

            System.out.println(x);
            System.out.println(y);

            if (x < y) {
                int newVal = y - x;
                maxHeap.add(newVal);
            } else if (x > y) {
                int newVal = x - y;
                maxHeap.add(newVal);
            }

        }

        if (maxHeap.size() == 0) {
            return 0;
        }

        return maxHeap.peek();
    }
}
