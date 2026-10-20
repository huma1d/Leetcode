class Solution {
    public boolean isPalindrome(int x) {
        int number = x;
        int numberog = x;
        int rev = 0;
        if (numberog<0){
            return false;
        }
        else {
        while (number!=0){
            int nm = number%10;
            rev = (rev*10)+nm;
            number=number/10;
        }
        return rev == numberog;
        }
    }
}