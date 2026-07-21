class Solution {

    public String encode(List<String> strs) {
        StringBuilder solution  = new StringBuilder();

        for (String s: strs) {
            solution.append(s.length());
            solution.append("#");
            solution.append(s);
        }

        return solution.toString();
    }

    public List<String> decode(String str) {
        System.out.println(str);
        List<String> solution = new ArrayList<>();

        int i = 0;

        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }

            int stringLength = Integer.parseInt(str.substring(i, j));
            System.out.println(stringLength);

            i = j + 1;

            String extract = str.substring(i, i + stringLength);
            System.out.println(extract);
            solution.add(extract);
            i = i + stringLength;
            System.out.println("End of word-------------------");
        }

        return solution;
    }
}
