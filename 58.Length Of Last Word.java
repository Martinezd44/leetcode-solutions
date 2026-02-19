class Solution {
    public int lengthOfLastWord(String s) {
        int count =0; //count for last String word
        int i = s.length()-1; //backtracks to the end of the string

        while(i>=0 && s.charAt(i)==' '){//while loop going through the spaces
            i--;
        }

        while(i>=0 && s.charAt(i) !=' '){//goes through and checks for noncharacters
            count++;
            i--;
        }
        return count;



        }
        
    }
    