class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int n = s.length();

        HashMap<Character, Integer> map_s = new HashMap<>();
        HashMap<Character, Integer> map_t = new HashMap<>();

        for (int i = 0; i < n; i++) {
            Character sChar = s.charAt(i);
            map_s.put(sChar, map_s.getOrDefault(sChar, 0) + 1);

            Character tChar = t.charAt(i);
            map_t.put(tChar, map_t.getOrDefault(tChar, 0) + 1);
        }

        System.out.println(map_s);
        System.out.println(map_t);

        return map_s.equals(map_t);
    }
}
