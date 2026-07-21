class DynamicArray {
    private int[] arr;
    private int length;
    private int capacity;

    public DynamicArray(int capacity) {
        arr = new int[capacity];
        int length = 0;
        this.capacity = capacity;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (length == capacity) {
            resize();
        }

        arr[length] = n;
        length++;
    }

    public int popback() {
        int temp = arr[length - 1];
        arr[length - 1] = 0;
        length--;
        return temp;
    }

    private void resize() {
        int[] newArr = new int[capacity * 2];
        capacity = capacity * 2;

        for (int i = 0; i < arr.length; i++) {
            newArr[i] = arr[i];
        }

        arr = newArr;
    }

    public int getSize() {
        return length;
    }

    public int getCapacity() {
        return capacity;
    }
}
