class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        StringBuilder s_builder = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);

            if (Character.isLetterOrDigit(c)) {
                s_builder.append(c);
            } 
        }

        return s_builder.toString().equals(
            s_builder.reverse().toString()
        );
        
    }
}
