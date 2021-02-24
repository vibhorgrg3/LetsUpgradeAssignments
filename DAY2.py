#!/usr/bin/env python
# coding: utf-8



'''
What is the time, space complexity of following code:


int a = 0, b = 0;     --------------------- O(1)
for (i = 0; i < N; i++) {------------------ O(N+1)
a = a + 1;--------------------------------- O(N)
}
for (j = 0; j < M; j++) {------------------ O(M+1)
b = b + j; -------------------------------- O(M)
}
'''
# hence overall time complexity = 2(M+N) + 3 
# For Big -O analysis we take O(MAX(M,N))
# where MAX(A,B) returns larger of A and B 





"""What does it mean when we say that an algorithm X is asymptotically more efficient than Y?
a)X will be a better choice for all inputs
b)X will be a better choice for all inputs except possibly small inputs
c)X will be a better choice for all inputs except possibly large inputs
d)Y will be a better choice for small inputs
"""

# Ans = b)X will be a better choice for all inputs except possibly small inputs







