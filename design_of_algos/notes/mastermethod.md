## Master method

Master method describes the time complexity of recursive divide and conquer algorithms.
Assumes that each subproblem of the recursion is of the same size. Here $a$ is the
number of subproblems, $\dfrac{n}{b}$ is the size of each subproblem and $O(n^d)$ is the
work done for each subproblem.

See [Stanford lectures](https://www.youtube.com/watch?v=rXiojCN9nIs&list=PLEAYkSg4uSQ37A6_NrUnTHEKp6EkAxTMa&index=20).

$$
T(n) = a \times T \left(\dfrac{n}{b}\right) + O(n^d)
$$

$$
    T(n) = 
\begin{cases}
    O(n^d \log(n)),& \text{if } a = b^d \\
    O(n^d),              & \text{if } a \lt b^d \\
    O(n^{log_{b}^a}),              & \text{if } a \gt b^d 
\end{cases}
$$