# A renowned organisation is in the process of incrememnt the salary of the employees. This increment is done based on their salary and their performance appraisal rating.
# 1. If the appraisal rating is between 1 and 3, the increment is 10% of the salary.
# 2. If the appraisal rating is betwwn 3.1 and 4, the increment is 25% of the salary.
# 3. If the appraisal rating is between 4.1 and 5, the increment is 30% of the salary.
# If either the salary is 0 or negative (or) if the appraisal rating is not in the range 1 to 5(inclusive), then the output should be "Invalid Input".

import sys
s=int(input("Enter the salary"));
a=float(input("Enter the performanceappraisal rating ")):
if(s<=0 or a<1 or a>5):
    print("Invalid Input")
elif (a>=1 and a<=3):
     i=s+((0.1)*s)
     print(i)
elif (a>=3.1 and a<=4):
     i=s+((0.25)*s)
     print(i)
elif(a>=4.1 and a<=5):
    i=s+((0.3)*s)
    print(i)

     
    
