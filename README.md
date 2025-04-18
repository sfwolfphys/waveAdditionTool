# Wave Addition Tool

This is a repository for my wave addition tool for my physics 2360 class. This is a Shiny App to help students understand wave addition.  The idea here is to assume that there are a series of waves as below:

$$
f(x) = \sum_{i=0}^{N-1} \sin\left(2\pi(x+i\delta)\right)
$$

The tool allows you to adjust the parameters $N$ and $\delta$. It then plots the individual waves:

$$
f_i(x) = \sin\left(2\pi(x+i\delta)\right)
$$

as well as the total wave $f(x)$. 