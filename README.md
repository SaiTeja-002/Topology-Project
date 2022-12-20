# Topology-Project

### Problem Statement

Given any input simplicial complex (up to 3-dimensional), compute β2 using the
boundary matrix method.

### Theory

Betti numbers are used to distinguish topological figures on the basis of the
connectivity of the n-dimensional simplicial complexes. A pth Betti number refers
to the number of pth dimensional holes.
- 0 ⇒ Number of connected components.
- 1 ⇒ Number of tunnels (One-Dimensional holes).
- 2 ⇒ Number of voids (Two-Dimensional holes).

`Hp(K) = Ker(მp) / Im(მ(p+1))` <br>
`p = dim(Hp(K)) = dim(Ker(მp)) - dim(Im(მ(p+1)))`


### Algorithm
1. `H2(K) = Ker(მ2) / Im(მ3)`
2. The formula used to calculate β2 is : <br>
<t> `β2 = dim(H2(K)) = dim(Ker(მ2)) - dim(Im(მ3))`
3. We take the values of the vertices, edges, faces, and tetrahedrons from the given “.gts” file and compute the მ2 and მ3 matrices.
4.  We then compute the rank of მ2 and მ3 matrices. These are the values of dim(Im( მ2 )) and dim(Im( მ3 )) respectively.
5. From the Rank Nullity theorem, we know that `dim(C2(K)) = dim(Ker(მ2)) + dim(Im(მ2))`. So from this, we get the dim(Ker(მ2)) value, and then we can find the value of 2 for the given figure using the formula mentioned in (2).


### Implementation
1. Extract the number of vertices, edges, faces, and tetrahedrons. And then extract the edges, faces, and tetrahedrons from the given “.gts” file.
2. Compute the მ2 and მ3 matrices using the vertices, edges, faces, and tetrahedrons data obtained in step-I.
3. Find the ranks of მ2 and მ3 matrices.
4. Compute the value of 2 using the formula.


### System Requirements
Pre-installed numpy and python3 are required to run the program.
To install the required libraries, execute the following command in the terminal
- `pip3 install numpy`


### Steps To Run The Program
To run the program, execute the following command in the terminal
- `python3 betti2.py` <br>
<p> Then enter the name of the “.gts” file that is to be taken as the input. </p>


### References
1. http://gts.sourceforge.net/samples.html
2. https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html#:~:text=Rank%20of%20the%20array%20is,that%20are%20greater%20than%20tol.&text=Input%20vector%20or%20stack%20of%20matrices.&text=Threshold%20below%20which%20SVD%20values,tol%20is%20set%20to%20S.
3. https://en.wikipedia.org/wiki/Rank%E2%80%93nullity_theorem#:~:text=The%20rank%E2%80%93nullity%20theorem%20is,the%20dimension%20of%20its%20kernel).
