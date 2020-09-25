name: Christmas Tree Garden
author: parthkgh24

category: Easy

description: |
  Problem Statement:
  It is almost the holiday season, and you want to grow a garden of Christmas trees. You have two types of seeds which create two different sizes of trees, each planted alternately in your rectangular garden. A tree of size 3 should look like this, with a single centered asterisk for the trunk:
   *
  ***
 *****
   *
Write a program to take input the number of rows and columns in your garden, along with the sizes of your two trees. Print your garden in the alternate manner as mentioned above, with the smaller tree appearing first in every row.
  Input Format:
  First line contains an integer r which is the number of rows.
  Second line contains an integer c which is number of columns.
  Third line contains the size of the smaller tree.
  Fourth line contains the size of the bigger tree. 
  Output Format:
  Print the garden that would be formed in the pattern of small tree followed by big tree.
  Constraints:
  1<=n<=10^4 
  Sample Input:
  2
  2
  3
  4
  Sample Output:
                                                                                                                                             
         *                                                                                                                                    
  *     ***                                                                                                                                   
 ***   *****                                                                                                                                  
***** *******                                                                                                                                 
  *      *                                                                                                                                    
                                                                                                                                              
         *                                                                                                                                    
  *     ***                                                                                                                                   
 ***   *****                                                                                                                                  
***** *******                                                                                                                                 
  *      *        
  Explanation:
  The first two lines indicate the size of the garden, which is 2 rows and 2 columns. The next two lines are the size of the trees, 3 and 4. The output shows a garden of size 2x2 with trees grown as shown in the question of sizes 3 and 4.
points: 500

test_cases: 
  sample:
    1:
      input: |
        2
        2
        3
        4
        
      output: |
                                                                                                                                             
         *                                                                                                                                    
  *     ***                                                                                                                                   
 ***   *****                                                                                                                                  
***** *******                                                                                                                                 
  *      *                                                                                                                                    
                                                                                                                                              
         *                                                                                                                                    
  *     ***                                                                                                                                   
 ***   *****                                                                                                                                  
***** *******                                                                                                                                 
  *      *        
  hidden:
    1:
      input:
        file: ./input1.txt
      output:
        file: ./output1.txt
    2:
      input:
        file: ./input2.txt
      output:
        file: ./output2.txt   

round: 1

visibility: hidden