class Solution {
    public int reverseDegree(String s) {
    int c = 0;
    for(int i =0;i<s.length();i++){
        int f='z'-s.charAt(i)+1;
        int pos=i+1;
        c+=f*pos;
        }
        return c;
    }
}