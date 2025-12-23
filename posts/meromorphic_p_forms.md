---
tags: post
title: What is the sheaf of meromorphic p-forms?
date: 2022-06-10
layout: base.njk
---

# What is the sheaf of *meromorphic $p$-forms* $\Omega_X^k(*D)$?

2022-06-10

I was recently reading about **Grothendieck's Algebraic de Rham Theorem** in Griffiths and Harris [GH78, p. 453], which states that, for $X$ a complex manifold and $D$ a simple normal crossing divisor on $X$, the complex cohomology of $U:= X\setminus D$ can be computed as $$H^k(U;\mathbb{C}) = \mathbb{H}^k (X,\Omega_X^\bullet(\log(D))),$$ i.e. it is the hypercohomology of the so called **logarithmic de Rham complex** $\Omega_X^\bullet(\log(D))$ of sheaves on $X$.

This is a complex of sheaves whose $p$-th term is the sheaf $\Omega_X^p (\log(D))$, which in turn is defined as the subsheaf of the sheaf $\Omega_X^i(*D)$ of **meromorphic $p$-forms that are holomorphic on $X\setminus D$**. Then $\Omega_X^1 (\log(D))$ is stated to be locally free, and [PT08] gives the description, for $p\in D$ and $(V,z_1,\dots,z_n)$ on $X$ containing $p$ such that $D$ has equation $z_1\dots z_k =0$, that 

<div>
$$
\Omega_X^1(\log(D))_p=\mathcal{O}_{X,p}\frac{dz_1}{z_1}\oplus \dots \oplus \mathcal{O}_{X,p}\frac{dz_k}{z_k} \oplus \mathcal{O}_{X,p}dz_{k+1}\oplus \dots \oplus \mathcal{O}_{X,p}dz_{n}.
$$
</div>

Then the sheaf $\Omega_X^q (\log (D))$ is defined to be the $q$-th wedge $\bigwedge^q \Omega_X^1 (\log (D))$. While one can have a certain intuition about what this sheaf is, I find it unclear what relation it has to the sheaf $\Omega_X^i(\ast D)$. On page 135 of [GH78], there is a definition of a meromorphic section of a line bundle, and it would be tempting to define meromorphic forms as such sections of $\Omega_X^p$, but this is not exactly what we want as $\Omega_X^p$ is not a line bundle.

Chasing through the literature, Deligne uses the complex  $\Omega_X^\bullet(\log(D))$ in [De71] to define a mixed Hodge structure on the cohomology of $U$, and cites [Del70, Section II.3.1-7] for proofs. Going there however, the definition of meromorphic sections given on page 66 is also quite cryptic. Going back to what I believe is the original source of the theorem by Grothendieck [Gr66, p. 97], we find a completely satisfactory definition in a footnote (which is, in retrospect, the one given by Deligne).

We reproduce the definition here, and encourage the reader to refer back to the original paper, where the statement is given in terms of complex analytic spaces.

> **Definition [Gr66,p. 97]**
>
> Let $\mathscr{F}$ be a coherent sheaf on $U$. Suppose that $\mathscr{F}$ on $U$ can be extended, on an open neighbourhood $W_y$ in $X$ of any point $y\in D$, into a coherent sheaf $\mathscr{G}$.
>
> Then the **sheaf $\mathscr{F}(\ast D)$ of meromorphic sections of $\mathscr{F}$ that are holomorphic on $U$** is the subsheaf of $f_\ast(\mathscr{F})$ whose sections on an open set $V$, are the sections $\omega$ of $\mathscr{F}$ on $V\cap U$ such that, for every $y\in V\cap D$, there exists an open neighbourhood $W\subset W_y \cap V$ of $y$, a section $\omega'$ of $\mathscr{G}$, and an integer $n$, such that $\omega\vert_{W\cap U} = (\omega'/(\phi')^n)\vert_{W\cap U}$, where $\omega'$ is the defining equation of $Y$ in $X$.
>
> It can be checked that these $\omega$ indeed are the sections of a subsheaf $\mathscr{F}(\*D)$ of $f_\* (\mathscr{F})$, and that this subsheaf does not depend on the choices performed.


It is stated that when $\mathscr{F}$ can be extended globally to a coherent sheaf $\mathscr{G}$ on $X$, there is a natural isomorphism $$\mathscr{F}(*D)\cong {\lim_{\longrightarrow}} \mathscr{H}\kern -3.5pt \mathit{om}_{\mathscr{O}_X}(\mathscr{I}^n, \mathscr{G}),$$ where $\mathscr{I}$ is a coherent sheaf of ideals on $X$ defining $D$.

Then finally, in the case of the sheaf of holomorphic $p$-forms $\Omega_U^p$ on $U$, one can take $\mathscr{G}=\Omega_X^p$. This gives a complete definition of what the sheaf $\Omega_X^p (*D)$ is.

It would be very interesting to see if any other sheaves have interesting meromorphic sections that are holomorphic on $U$. If you know of any, feel free to share them with me by mail, and I'll post them below.


## Bibliography:

- [De70] Deligne, <b>Équations différentielles à points singuliers réguliers</b>, Lecture Notes in Mathematics, Vol. 163, Springer, 1970                        
- [De71] Deligne, <b>Théorie de Hodge. II </b>, Inst. Hautes Études Sci. Publ. Math., 1971
- [GH78] Griffiths and Harris, <b>Principles of algebraic geometry</b>, Wiley-Interscience, John Wiley & Sons, New York, 1978
- [Gr66] Grothendieck, <b>On the de Rham cohomology of algebraic varieties</b>, Inst. Hautes Études Sci. Publ. Math., 1966
- [PS08] Peters and Steenbrink, <b>Mixed Hodge structures</b>, Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge., Springer, 2008


