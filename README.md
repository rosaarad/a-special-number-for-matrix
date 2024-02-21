In this question, two numbers n and m inputs are given and then n numbers are entered in sequence.
You first need to create matrices with different dimensions which can be formed by those n numbers.
For example, if n is equal to 4, these matrices can be created: 4X1 2X2 1X4
Then you need to calculate the sum of the numbers of each row as well as each column. Now measure all these numbers in "mod m" and add "1" so that the interval [1,m] is placed.
Now, consider the maximum among the numbers related to the column sum and the minimum among the numbers related to the row sum and multiply these two values ​​together to reach the specific number of that matrix.
Finally, you need to output the sum of these special numbers for different matrices that can be created.
