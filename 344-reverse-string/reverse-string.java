class Solution {
    public void reverseString(char[] s) {
        char[] arr=s.clone();
        int c=s.length-1;
        for(int i=0;i<s.length;i++){
            s[i]=arr[c];
            c--;
        }
    }
}