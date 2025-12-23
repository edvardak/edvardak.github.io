---
tags: post
title:  "Manifolds: Topological, Smooth, Complex, Kähler (Work in Progress)"
layout: base.njk
---

# Manifolds: Topological, Smooth, Complex, Kähler (Work in Progresss)

In this post, we aspire to define some main classes of manifolds, as well as to give an intuitive understanding of how they are related.

## Topological manifolds

Manifolds are spaces that "locally" look like $\mathbb{R}^n$. A motivating example can be the surface of the Earth which locally looks flat but has a global shape vastly different from the plane.

> An **$n$-dimensional topological manifold** $M$ or just **$n$-manifold** is a second countable Hausdorff topological space, such that each point $x\in M$ has an open neighbourhood $U$ which is homeomorphic to $\mathbb{R}^n$.

<!-- - Why Hausdorff? If there are points which cannot be separated, then intuition breaks down.  -->
<!-- - Why second countable? Otherwise, it is not clear that the manifold can be embedded in any Euclidean space, and when we want to do analysis on our manifold, it is not clear that this will work. -->

Moreover, one can add structures to a manifold:
> An <b>atlas</b> on an $n$-manifold is a set 
>
> $$
> \mathcal{A} = \{(U_\alpha,f_\alpha)\}_{\alpha \in I}
> $$
>
> such that each $U_\alpha$ is open and they form a covering 
> $$
> M = \cup_{\alpha \in I} U_\alpha,
> $$
> and 
>
> $$
> f_\alpha \colon U_\alpha \to \mathbb{R}^n
> $$ 
>
> is a homeomorphism.

<img src="" alt="# Insert atlas illustration" />

> Using the unifying theme of atlases, one can then add structure to the maps $f_\alpha$ to add more "rigidity" to the manifold. Here it will be good to recall the "hierarchy of smoothness", see for instance Wikipedia.

## Smooth manifolds

Topological manifolds are good generalisations of the euclidean spaces $\mathbb{R}^n$, but they are limited in the same manner that continuous functions are limited. You may recall that the absolute value function is continuous and in fact has a derivative, but the derivative is not itself continuous. This somewhat reduces your capacity for analysis since the the derivative is not a topological manifold anymore.

<img src="" alt="Insert absolute value function." />

To circumvent this, we can restrict our attention to functions whose derivatives always exist, namely the smooth functions:

1. A function $f\colon \mathbb{R} \to \mathbb{R}$ is <b>smooth or $C^\infty$</b> if it is continuous and all the derivatives $\frac{d^i f}{dx^i}$ exist for $i \geq 0$.
2.  Generalising, $f\colon \mathbb{R}^n \to \mathbb{R}$ is smooth if all the partial derivatives $\frac{\partial^{\alpha} f}{\partial x_1^{\alpha_1} \partial x_2^{\alpha_2} \cdots \partial x_n^{\alpha_n} }$, $\alpha = \sum_i \alpha_i$, exist.
3. Finally, $f\colon \mathbb{R}^n \to \mathbb{R}^m$ is smooth if all the coordinate functions $f_1,f_2, \dots, f_n$ are smooth. 

Using these new types of functions, we can create manifolds with a lot more structure.


> A <b>$C^\infty$-structure</b> on an $n$-manifold $M$ is an atlas of 
>
> $$
> \mathcal{A} = \{(U_\alpha,f_\alpha)\}_{\alpha \in I}
> $$
>
> such that \[ f_\beta \circ f_\alpha^{-1} \colon f_\alpha(U_\alpha \cap U_\beta) \subseteq \mathbb{R}^n \to f_\beta(U_\alpha \cap U_\beta) \subseteq \mathbb{R}^n \] is a 
>
> $$
> C^\infty
> $$ 
>
> function, i.e. a smooth function, for all $\alpha, \beta$. A manifold with a $C^\infty$-structure is called a <b>$C^\infty$ or smooth manifold</b>.

Are all topological manifolds also smooth manifolds? No, but the smallest example of a topological manifold which does not have a smooth structure is in dimension $7$. 

## Complex Manifolds

A <b>complex structure</b> on a $2n$-manifold $M$ is a collection 

$$
\{(U_\alpha, f_\alpha)\}_{\alpha \in U}
$$ 

such that the $U_\alpha$ form a covering, but now 

$$ 
f_\alpha \colon U_\alpha \to \mathbb{C}^n
$$

and 

$$ 
f_\beta \circ f_\alpha^{-1} \colon f_\alpha(U_\alpha \cap U_\beta) \subseteq \mathbb{C}^n \to f_\beta(U_\alpha \cap U_\beta) \subseteq \mathbb{C}^n
$$

is a holomorphic function, for all $\alpha, \beta$.

A $2n$-manifold with a complex structure is called a <b>complex manifold of dimension $n$</b>, where the dimension halving is because we now think of the manifold as locally being $\mathbb{C}^n$ instead of $\mathbb{R}^n$. 

Given a point $p\in M$, using the atlas, we can find an open set $U$ with $p\in U$, and use the function $f\colon U \to \mathbb{C}^n$ to give us complex coordinates $(z_1,...,z_n)\in \mathbb{C}^n$ locally, allowing us to pretend that we actually are in $\mathbb{C}^n$ instead of our manifold $M$.

<img src="" alt="# insert image of a local chart" />

Now we want to talk about tangents on our manifold. There are three possible <b>tangent space</b> we could consider:

- The <b>real tangent space</b> $T_{\mathbb{R},p} M$ is all the real directions along our manifold, imagine a real hyperplane lying tangent to the space.
- The <b>complex tangent space</b> $T_{\mathbb{C},p} M$ is all the complex directions along our manifold, imagine a complex hyperplane lying tangent to the space. 
- The <b>holomorphic tangent space</b> $T_{p}' M$ is all the holomorphic directions along our manifold, so that the differentials vanish on antiholomorphic functions. 

