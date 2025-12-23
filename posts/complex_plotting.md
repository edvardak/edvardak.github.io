---
tags: post
layout: base.njk
title: Plotting complex functions with Julia
date: 2021-03-27
---

# Plotting complex functions with Julia

2021-03-27

> TLDR: scroll down for cool 3D plots.

## Mathematical introduction

In this post we wish to visualize complex valued functions of a single complex variable, i.e. functions $f : \mathbb{C} \to \mathbb{C}$ taking a complex number $z$ to $f(z)$, e.g. $f(z)=z^2$. The usual manner of visualisation for a real function $g : \mathbb{R} \to \mathbb{R}$ is to look at its graph 

$$ \Gamma_g = \set{(x,g(x))\mid x\in \mathbb{R}}\subset \mathbb{R}\times \mathbb{R}, $$

that is look at e::ach number $x \in \mathbb{R}$ and place a point at height $g(x)$ over it. For instance, for $g(x)=\sin(x)$, we get the usual graph:

<img src="/posts/complex_plotting_plots/sin.png" alt="graph_of_sin_function">


How can we do this for complex valued functions?


Recall that a complex number $z$ can be written uniquely as in terms of its real and imaginary parts $z=a+ib$, for $a,b \in \mathbb{R}$. Therefore, we can in some sense identify the complex numbers $\mathbb{C}$ with pairs of real numbers $\mathbb{R}^2$. If we rewrite our complex function $f : \mathbb{C} \to \mathbb{C}$ instead as a function $f : \mathbb{R}^2 \to \mathbb{R}^2$, we see that the graph of the function $$\Gamma_f = \set{(v,g(v)))\mid v\in \mathbb{R}^2}\subset \mathbb{R}^2\times \mathbb{R}^2,$$
lives in a 4-dimensional space, hence we cannot visualize it!


While we can't see the whole graph of the function, we can still get part of the way there. One approach to visualizing a complex function is using [domain coloring](https://en.wikipedia.org/wiki/Domain_coloring). In this post, we will aim to instead visualize the modulus of a complex function.


Recall that for any complex number $z=a+ib\in \mathbb{C}$, we have the modulus $|z|=\sqrt{a^2 +b^2} \in \mathbb{R}$. This gives us a new function $|\cdot|:\mathbb{C}\to \mathbb{R}$, which we will call the modulus function. By composing the original function $f$ with $|\cdot|$, we get a new function
$$|f| : \mathbb{C}\xrightarrow{f} \mathbb{C} \xrightarrow{|\cdot|} \mathbb{R}.$$
Now this can be viewed as a function $|f| : \mathbb{R}^2 \to \mathbb{R} $, and so its graph is 
$$\Gamma_{|f|} = \set{(v,|f(v)|)\mid v\in \mathbb{R}^2}\subset \mathbb{R}^2\times \mathbb{R},$$
which lives in a 3-dimensional space and can therefore be visualized!

## Using Julia for plotting

Since we now know that for a complex function $f : \mathbb{C} \to \mathbb{C}$ we can plot its modulus $|f| \colon \mathbb{R}^2 \to \mathbb{R}$ (where we identified $\mathbb{C}$ and $\mathbb{R}^2$). We will do this using the programming language [Julia](https://julialang.org/). Julia has two advantages in the current context:

1. It supports complex numbers for the complex valued functions we will want to visualize (e.g. sums, exponents, $\sin, \exp,$ ...), and 
2. it can use [plotly](https://plotly.com/) to create nice interactive 3D plots that can be shared in the browser.

See [here](https://techytok.com/lesson-plotting/) for an introduction to plotting with Julia.

One last comment before we get to the plotting: taking the modulus can result in very large numbers, making it hard to see the structure for smaller values, we therefore plot scaled versions using $\ln(1+|f(z)|)$ or $\min(|f(z)|,4)$ instead. All code can be found [here](https://github.com/edvardak/complex_plotting). Let's get plotting!



1. First we plot the modulus of the polynomial $f(z)=z^6 -2z+5$, or rather $\ln(1+|f(z)|)$, giving the following 3D graphic:
<div style="text-align: center;">
    <iframe width="100%" height="600px" frameborder="0" scrolling="no" src="/posts/complex_plotting_plots/polynomial.html"></iframe>
</div>

Recognize the 6 zeros of the function, as we would expect from the [fundamental theorem of algebra](https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra).

2. Next we plot the [meromorphic](https://en.wikipedia.org/wiki/Meromorphic_function)  function $f(z)=(z^2+2)(z^2-3)/(z^2)$:
<div style="text-align: center;">
    <iframe width="100%" height="600px" frameborder="0" scrolling="no" src="/posts/complex_plotting_plots/meromorphic.html"></iframe>
</div>
Notice the pole (of order 2) at 0, and the 4 roots of the polynomial.

3. Now we turn to $f(z)=e^{-1/z}$:
<div style="text-align: center;">
    <iframe width="100%" height="600px" frameborder="0" scrolling="no" src="/posts/complex_plotting_plots/e_z_inv.html"></iframe>
</div>

Notice the [essential singularity](https://en.wikipedia.org/wiki/Essential_singularity) at $z=0$.

4. Next let's look at $f(z)=\sin(z)$:
<div style="text-align: center;">
    <iframe width="100%" height="600px" frameborder="0" scrolling="no" src="/posts/complex_plotting_plots/sin.html"></iframe>
</div>

where we can see that, while the zeros along the real line repeat with period $\pi$, the modulus grows fast in the imaginary direction.

5. We can also plot the [Gamma function](https://en.wikipedia.org/wiki/Gamma_function) $ \Gamma(z)$:
<div style="text-align: center;">
    <iframe width="100%" height="600px" frameborder="0" scrolling="no" src="/posts/complex_plotting_plots/gamma.html"></iframe>
</div>
Here you can see the first few poles of $\Gamma$ along the non-positive integers.

6. Finally, we visualize the [Riemann zeta function](https://en.wikipedia.org/wiki/Riemann_zeta_function) $\zeta(s)$:
<div style="text-align: center;">
    <iframe width="100%" height="600px" frameborder="0" scrolling="no" src="/posts/complex_plotting_plots/zeta.html"></iframe>
</div>

Notice the zeros lining up on the $x=\mathfrak{Re}(s)=1/2$ line, as predicted by the famous [Riemann hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis)!


We've now seen many 3D plots of the modulus of a complex function. Hopefully this should give you some sort of new intuition for how complex valued functions behave. To really complete the vizualisations done here, one should also plot the argument $\theta(f)$ of the function. If you looked at the [domain coloring](https://en.wikipedia.org/wiki/Domain_coloring) technique from above, you saw that this could be visualized using coloring, which is the next natural step to do. However, we have not found a satisfacory way to do so with Julia and plotly so far.


If the visualisation of complex functions interest you, you may consider checking out the following links:

- [Domain coloring with Python](https://nbviewer.jupyter.org/github/empet/Math/blob/master/DomainColoring.ipynb)
- [Hans Lundmark's complex analysis pages ](https://users.mai.liu.se/hanlu09/complex)/
- [Phase Plots of Complex Functions: A Journey in Illustration](https://www.ams.org/notices/201106/rtx110600768p.pdf)

