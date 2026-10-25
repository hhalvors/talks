---
title: "Equivalence: A Program"
author: Hans Halvorson
date: Oslo, June 2026
---

# The same theory, presented differently

The **same content** under **different forms of presentation**

- date and place of presentation, font, language, notation, primitives

When human beings communicate, the content is wrapped up in various
forms.

- Could one presentation say "there are exactly two things" while
another presentation says "there are exactly three things"?

- Could one presentation (ZF) be based on a membership relation $x\in
  y$ while another presentation (ETCS) is based on morphisms $A\to B$
  between sets?

# Sixty years of technical work

\vspace{2em}

\begin{center}
\begin{tikzpicture}[every node/.style={font=\large}]

% the spectrum arrow (leaves room for pole labels)
\draw[<->, line width=1.4pt, color=nordiskFg] (-4.7,0) -- (4.7,0);

% poles, just beyond the arrowheads
\node[color=nordiskMuted, anchor=east] at (-5.0,0) {Zeno};
\node[color=nordiskMuted, anchor=west] at (5.0,0) {Heraclitus};

% tick marks
\foreach \x in {-2.4,0,2.4}{
  \draw[color=nordiskFg, line width=1pt] (\x,0.15) -- (\x,-0.15);
}

% criteria above the arrow
\node[color=nordiskAccent, anchor=south] at (-2.4,0.32) {categorical};
\node[color=nordiskAccent, anchor=south, font=\Large\bfseries] at (0,0.34) {Morita};
\node[color=nordiskAccent, anchor=south] at (2.4,0.32) {definitional};

\end{tikzpicture}
\end{center}

# Philosophical critics

sklar.jpg

> Whatever this structural "isomorphism" is to be, it cannot be a
> purely formal notion. It cannot be, that is, an interrelationship
> which can be determined to hold solely on the basis of the logical
> form of the theories in question.

--- Sklar 1982

# Philosophical critics
  
> According to one alternative—the second "extreme" approach to
> equivalence I want to discuss—we can say that theories are
> equivalent without saying why they are equivalent in terms of
> fundamentality and underlying third languages. (Sider 2020)
  
\vspace{1em}
  
> I investigate whether there is a defensible view according to
> which formal criteria have significant non-mathematical
> implications, of these sorts or any other, reaching a chiefly
> negative verdict. (Teitel 2021)

# Saving the program

1. Concession: No direct philosophical upshot of formal equivalence
   results.
   
2. Retrenchment: Equivalence results shed light on what combinations of
   philosophical commitments are tenable.
   
   - How much information transfers from one formulation to another
   
   - If you *insist* on one formulation, what does that say about your
     non-scientific philosophical commitments?   
   

## How logicians do it

# The logician's criteria

Relations between first-order theories:

- mutual interpretability
- definitional equivalence
- bi-interpretability

# But physics is not written in first-order logic

These criteria presuppose a linguistic (first-order) regimentation.

The most interesenting physical theories don't have canonical
regimentations -- general relativity uses Lorentzian manifolds, QFT
uses operator algebras, Hamiltonian mechanics uses symplectic
manifolds

# The semantic view of scientific theories 

In the 1960s and 70s, philosophers of science rejected the \emph{syntactic}
view of theories in favour of the \emph{semantic} view.

\vspace{1.2em}

\begin{center}
\begin{tikzpicture}[
  every node/.style={font=\large},
  era/.style={color=nordiskAccent, font=\large\bfseries, anchor=south},
  span/.style={line width=2pt},
  fig/.style={anchor=north, font=\normalsize},
  yr/.style={anchor=north, color=nordiskMuted, font=\footnotesize},
  idea/.style={anchor=north, color=nordiskAccent, font=\small\itshape}
]

% timeline axis
\draw[->, line width=1.4pt, color=nordiskFg] (-5.6,0) -- (5.9,0);

% era labels:  x_label/name
\foreach \xc/\name in {-3.7/syntactic, 2.6/semantic}{
  \node[era] at (\xc,1.55) {\name};
}
% era spans (semantic longer = tilt toward where we're going)
\draw[span, color=nordiskMuted!40] (-5.2,1.25) -- (-2.2,1.25);
\draw[span, color=nordiskAccent!55] (-0.3,1.25) -- (5.5,1.25);

% figures:  x / name / year  (x encodes date; semantic spread wider)
\foreach \x/\name/\yr in {%
  -4.6/Carnap/1928,
  -2.9/Hempel/1950s,
  0.3/Suppes/1960,
  4.4/{van Fraassen}/1980%
}{
  \draw[color=nordiskFg, line width=1pt] (\x,0.16) -- (\x,-0.16);
  \node[fig] at (\x,-0.25) {\name};
  \node[yr]  at (\x,-0.78) {\yr};
}

% one-word idea under each era:  x / word
\foreach \x/\word in {-3.75/sentences, 2.35/models}{
  \node[idea] at (\x,-1.25) {\word};
}

\end{tikzpicture}
\end{center}

# When are two classes of models the same?

\vspace{0.3em}

\begin{center}
\begin{tikzpicture}[
  every node/.style={font=\large},
  dot/.style={circle, fill=nordiskFg, inner sep=2.6pt},
  match/.style={color=nordiskMuted, line width=0.8pt},
  panelhd/.style={color=nordiskAccent, font=\large\bfseries},
  sub/.style={color=nordiskMuted, font=\small\itshape}
]

% rows at integer indices 1,2,3 -> y = (i-1)*0.9
% ===================== LEFT PANEL: Zeno =====================
\begin{scope}[shift={(0,0)}]
  \node[panelhd] at (1.5,3.5) {too Zeno};
  \node[sub] at (1.5,2.95) {bijection of models};

  \foreach \i in {1,2,3}{ \node[dot] (LA\i) at (0,{(\i-1)*0.9}) {}; }
  \foreach \i in {1,2,3}{ \node[dot] (LB\i) at (3,{(\i-1)*0.9}) {}; }
  % scrambled bijection -- stresses that opaque dots carry no constraint
  \draw[match] (LA1) -- (LB2);
  \draw[match] (LA2) -- (LB3);
  \draw[match] (LA3) -- (LB1);

  \node[sub] at (0,-0.8) {$\mathrm{Mod}(T)$};
  \node[sub] at (3,-0.8) {$\mathrm{Mod}(T')$};
\end{scope}

% divider
\draw[color=nordiskMuted!35, line width=0.6pt] (4.9,-1.05) -- (4.9,3.3);

% ===================== RIGHT PANEL: Heraclitus =====================
\begin{scope}[shift={(6.4,0)}]
  \node[panelhd] at (1.5,3.5) {too Heraclitus};
  \node[sub] at (1.5,2.95) {model-by-model isomorphism};

  \foreach \i in {1,2,3}{
    \node[circle, draw=nordiskFg, line width=0.7pt, inner sep=5pt] (RA\i) at (0,{(\i-1)*0.9}) {};
    \fill[nordiskAccent] ($(RA\i)+(-0.09,0.05)$) circle (0.6pt);
    \fill[nordiskAccent] ($(RA\i)+(0.09,-0.04)$) circle (0.6pt);
    \draw[nordiskAccent, line width=0.4pt] ($(RA\i)+(-0.09,0.05)$) -- ($(RA\i)+(0.09,-0.04)$);
  }
  \foreach \i in {1,2,3}{
    \node[circle, draw=nordiskFg, line width=0.7pt, inner sep=5pt] (RB\i) at (3,{(\i-1)*0.9}) {};
    \fill[nordiskAccent] ($(RB\i)+(-0.09,0.05)$) circle (0.6pt);
    \fill[nordiskAccent] ($(RB\i)+(0.09,-0.04)$) circle (0.6pt);
    \draw[nordiskAccent, line width=0.4pt] ($(RB\i)+(-0.09,0.05)$) -- ($(RB\i)+(0.09,-0.04)$);
  }
  % aligned matching, each carrying iso
  \foreach \i in {1,2,3}{
    \draw[match] (RA\i) -- (RB\i);
    \node[color=nordiskMuted, font=\footnotesize] at (1.5,{(\i-1)*0.9+0.18}) {$\cong$};
  }

  \node[sub] at (0,-0.8) {$\mathrm{Mod}(T)$};
  \node[sub] at (3,-0.8) {$\mathrm{Mod}(T')$};
\end{scope}

\end{tikzpicture}
\end{center}

## The categorical move

# A simple idea, naturally motivated by mathematical physics 

- Philosophers of science could have found more plausible answers by
  keeping up with logic (see: relative interpretability)
- I found my way there by working backwards: the collection of models
  of a theory is **structured**:
  1. Morphisms
  2. Topology

# A category

\begin{center}
\begin{tikzcd}[column sep=4em, row sep=3.2em]
A \arrow[r, shift left=0.8ex, "f"] \arrow[dr, "h"'] & B \arrow[l, shift left=0.8ex, "g"] \\
& C
\end{tikzcd}
\end{center}

\vspace{1em}

The morphisms are the point: a category remembers how its objects
relate.

# A functor

\begin{center}
\begin{tikzpicture}[every node/.style={font=\large}, >={Straight Barb[scale=0.9]}]

% ---- domain category C (left) ----
\node (A) at (0,2.6) {$A$};
\node (B) at (0,0.6) {$B$};
\node (C) at (0,-1.4) {$C$};
\draw[->] (A) to[bend right=25] node[left] {$f$} (B);
\draw[->] (A) to[bend left=25]  node[right] {$g$} (B);
\draw[->] (B) -- node[right] {$h$} (C);
\node[color=nordiskMuted] at (0,-2.6) {$\mathbf{C}$};

% ---- codomain category D (right) ----
\node (X) at (7,2.6) {$X$};
\node (Y) at (7,0.6) {$Y$};
\node (Z) at (7,-1.4) {$Z$};
\draw[->] (X) to[bend right=25] node[left] {$p$} (Y);
\draw[->] (X) to[bend left=25]  node[right] {$q$} (Y);
\node[color=nordiskMuted] at (7,-2.6) {$\mathbf{D}$};

% ---- object action (dotted) ----
\draw[->, dotted, thick, color=nordiskAccent!55] (A) -- (X);
\draw[->, dotted, thick, color=nordiskAccent!55] (B) -- (Y);
\draw[->, dotted, thick, color=nordiskAccent!55] (C) to[bend right=12] (Y);

% ---- functor label ----
\node[color=nordiskAccent] at (3.5,2.9) {$F$};

\end{tikzpicture}
\end{center}

# Natural transformations

\begin{center}
\begin{tikzpicture}[every node/.style={font=\large}, >={Straight Barb[scale=0.9]}]

% ---- domain category (left): A -> B ----
\node (A) at (0,0) {$A$};
\node (B) at (1.8,0) {$B$};
\draw[->] (A) -- (B);

% ---- codomain square (right) in D ----
\node (W) at (8.0,1.3) {$W$};
\node (X) at (10.3,1.3) {$X$};
\node (Y) at (8.0,-1.3) {$Y$};
\node (Z) at (10.3,-1.3) {$Z$};
\draw[->] (W) -- node[above] {$Ff$} (X);
\draw[->] (Y) -- node[below] {$Gf$} (Z);
\draw[->] (W) -- node[left] {$\eta_A$} (Y);
\draw[->] (X) -- node[right] {$\eta_B$} (Z);

% ---- the two functors F (upper) and G (lower), dashed ----
\draw[->, dashed, color=nordiskAccent!60] (1.4,0.5) to[bend left=18] node[above, color=nordiskAccent] {$F$} (W);
\draw[->, dashed, color=nordiskAccent!60] (1.4,-0.5) to[bend right=18] node[below, color=nordiskAccent] {$G$} (Y);

% ---- the natural transformation eta: double arrow between F and G ----
\draw[-{Straight Barb[scale=1.1]}, line width=2.2pt, color=nordiskAccent]
  (4.7,0.7) -- (4.7,-0.7);
\draw[-{Straight Barb[scale=1.1]}, line width=2.2pt, color=nordiskAccent]
  (5.0,0.7) -- (5.0,-0.7);
\node[color=nordiskAccent] at (5.5,0) {$\eta$};

\end{tikzpicture}
\end{center}

# Equivalent categories

Categories $\mathbf{C}$ and $\mathbf{D}$ are *equivalent* when there are
functors $F, G$ back and forth with $GF \cong 1_{\mathbf{C}}$ and
$FG \cong 1_{\mathbf{D}}$.

\begin{center}
\begin{tikzpicture}[every node/.style={font=\large}, >={Straight Barb[scale=0.9]}]

% ---- C (left): A -> B ----
\node (A) at (0,1.1) {$A$};
\node (B) at (0,-1.1) {$B$};
\draw[->] (A) -- node[left] {$u$} (B);
\node[color=nordiskMuted] at (0,-2.4) {$\mathbf{C}$};

% ---- D (right): the square, verticals are isomorphisms ----
\node (W) at (9.0,1.6) {$W$};
\node (X) at (11.2,1.6) {$X$};
\node (Y) at (9.0,-0.6) {$Y$};
\node (Z) at (11.2,-0.6) {$Z$};
\draw[->] (W) -- (X);
\draw[->] (Y) -- (Z);
\draw[<->] (W) -- node[left] {$\cong$} (Y);
\draw[<->] (X) -- node[right] {$\cong$} (Z);
\node[color=nordiskMuted] at (10.1,-1.8) {$\mathbf{D}$};

% ---- F (top) and G (bottom) as single labelled functor bands ----
\draw[->, line width=5pt, color=nordiskAccent!28] (1.6,0.7) -- (7.2,0.9);
\node[color=nordiskAccent] at (4.4,1.35) {$F$};
\draw[->, line width=5pt, color=nordiskAccent!28] (7.2,-0.6) -- (1.6,-0.9);
\node[color=nordiskAccent] at (4.4,-1.25) {$G$};

\end{tikzpicture}
\end{center}

Now "same theory" has a precise, standard answer.

# What is, and isn't, invariant

Preserved by categorical equivalence:

- categorical properties such as "has Cartesian products"
- relations between objects
- automorphism groups of objects 

Not preserved:

- internal structures of objects 
- number of objects 

# Categorical equivalence is too liberal

- Weatherall: physics depends on internal structure of models
- Hudetz: the equivalence should itself be definable
- A category doesn't **assert** anything

# No downstairs without upstairs

To adopt a theory is to make assertions about objects --- *downstairs*.

But it is also to commit, even if tacitly, to when a *different*
formulation would be saying the same thing.

- that commitment is a criterion of equivalence --- *upstairs*
- you cannot fix what you are asserting without it

There is no downstairs without an upstairs.

# Different practices call for different criteria of equivalence

The physicist is rightly indifferent about foundational issues that
the set-theorist is worried about. 

The set theorist might be rightly indifferent about foundational
issues that the philosopher of mathematics is worried about. - not different *tastes* — different objects of inquiry
- each criterion is the exact expression of what aspect of reality its
  practice is trying to understand

No single criterion reads off the one true ontology.

## Sharpening the criterion

# Categorical equivalence is too coarse

Distinct propositional theories can have equivalent (discrete)
categories of models — yet differ in Stone space.

\vspace{0.2em}

\begin{center}
\begin{tikzpicture}[
  every node/.style={font=\large},
  cantor/.style={line width=3pt, color=nordiskFg},
  panelhd/.style={color=nordiskAccent, font=\large\bfseries},
  sub/.style={color=nordiskMuted, font=\small\itshape}
]

% reusable Cantor middle-thirds drawing (4 iterations across width 5)
\newcommand{\cantorset}[2]{% (#1)=x-origin (#2)=y-origin
  \begin{scope}[shift={(#1,#2)}]
    \draw[cantor] (0,1.2) -- (5,1.2);
    \draw[cantor] (0,0.8) -- (1.667,0.8);
    \draw[cantor] (3.333,0.8) -- (5,0.8);
    \foreach \a/\b in {0/0.556, 1.111/1.667, 3.333/3.889, 4.444/5}{
      \draw[cantor] (\a,0.4) -- (\b,0.4);
    }
    \foreach \a/\b in {0/0.185, 0.370/0.556, 1.111/1.296, 1.481/1.667,
                       3.333/3.519, 3.704/3.889, 4.444/4.630, 4.815/5}{
      \draw[cantor] (\a,0) -- (\b,0);
    }
  \end{scope}
}

% ---- LEFT: Mod(T) = Cantor space ----
\node[panelhd] at (2.5,3.4) {$\mathrm{Mod}(T)$};
\node[sub]     at (2.5,2.9) {$p_0, p_1, \dots$ \ no axioms};
\cantorset{0}{0}
\node[sub] at (2.5,-0.7) {Cantor space};

% divider
\draw[color=nordiskMuted!35, line width=0.6pt] (6.3,-1.0) -- (6.3,3.2);

% ---- RIGHT: Mod(T') = Cantor space + isolated point ----
\node[panelhd] at (9.6,3.4) {$\mathrm{Mod}(T')$};
\node[sub]     at (9.6,2.9) {$q_i \to q_j \ (i \le j)$};
\cantorset{7}{0}
\fill[nordiskAccent] (12.8,0.6) circle (3pt);
\node[color=nordiskAccent, font=\small] at (12.8,1.15) {$[q_0]$};
\node[sub] at (9.9,-0.7) {Cantor space $\;\sqcup\;$ isolated point};

\end{tikzpicture}
\end{center}

# Makkai's repair

Add structure to the category of models that the bare category forgets:

- **ultracategories** — categories equipped with ultraproduct functors
- Makkai's reconstruction: a theory can be recovered, up to
  equivalence, from its ultracategory of models
- the relation this induces: $T$ and $T'$ have equivalent
  *syntactic categories* / classifying toposes $\mathrm{Sh}(C_T) \simeq
  \mathrm{Sh}(C_{T'})$

Heavy apparatus — but it determines an interesting relation on
first-order theories

# The heavy thing is Morita equivalence

Barrett–Halvorson-Tsementzis: Makkai's relation is *exactly* this —

$T$ and $T'$ have a **common definitional extension**, allowing
definitions of new **sorts** as well as new relation and function
symbols.

That is **Morita equivalence**.

- the topos-theoretic apparatus and the syntactic notion coincide
- definitions of sorts are what categorical equivalence was
  silently using all along

# Defining new sorts

\vspace{0.4em}

\begin{center}
\begin{tikzpicture}[
  every node/.style={font=\large},
  >={Straight Barb[scale=0.9]},
  lbl/.style={color=nordiskFg, font=\small},
  hd/.style={color=nordiskAccent, font=\large\bfseries}
]

% ===== Quotient (top left) =====
\node[hd] at (0,3.3) {Quotient};
\node (q1) at (0,2.4) {$\sigma$};
\node (q2) at (0,0.9) {$\sigma'$};
\draw[->] (q1) -- node[right, lbl] {$e$} (q2);

% ===== Subsort (top right) =====
\node[hd] at (6,3.3) {Subsort};
\node (s1) at (6,2.4) {$\sigma$};
\node (s2) at (6,0.9) {$\sigma'$};
\draw[->] (s2) -- node[right, lbl] {$i$} (s1);

% ===== Product (bottom left) =====
\node[hd] at (0,-0.7) {Product};
\node (p) at (0,-1.6) {$\sigma_0 \times \sigma_1$};
\node (p0) at (-1.5,-3.1) {$\sigma_0$};
\node (p1) at (1.5,-3.1) {$\sigma_1$};
\draw[->] (p) -- (p0);
\draw[->] (p) -- (p1);

% ===== Coproduct (bottom right) =====
\node[hd] at (6,-0.7) {Coproduct};
\node (c) at (6,-1.6) {$\sigma_0 \amalg \sigma_1$};
\node (c0) at (4.5,-3.1) {$\sigma_0$};
\node (c1) at (7.5,-3.1) {$\sigma_1$};
\draw[->] (c0) -- (c);
\draw[->] (c1) -- (c);

\end{tikzpicture}
\end{center}

# Discovered twice

The same criterion was reached from the other direction -- by
logicians using no category theory at all.

- Szczerba 1977: Interpretability of elementary theories
  - Hodges *Model Theory*
  - Friedman and Visser
- the *default* notion of **bi-interpretability** coincides with
  Morita equivalence
- first proven by Evan Washington (Princeton undergraduate thesis,
  2018); see *The Logic in Philosophy of Science*

Two approaches, one criterion.

# A spectrum of criteria

\vspace{2em}

\begin{center}
\begin{tikzpicture}[every node/.style={font=\large}]

% the spectrum arrow (leaves room for pole labels)
\draw[<->, line width=1.4pt, color=nordiskFg] (-4.7,0) -- (4.7,0);

% poles, just beyond the arrowheads
\node[color=nordiskMuted, anchor=east] at (-5.0,0) {Zeno};
\node[color=nordiskMuted, anchor=west] at (5.0,0) {Heraclitus};

% tick marks
\foreach \x in {-2.4,0,2.4}{
  \draw[color=nordiskFg, line width=1pt] (\x,0.15) -- (\x,-0.15);
}

% criteria above the arrow
\node[color=nordiskAccent, anchor=south] at (-2.4,0.32) {categorical};
\node[color=nordiskAccent, anchor=south, font=\Large\bfseries] at (0,0.34) {Morita};
\node[color=nordiskAccent, anchor=south] at (2.4,0.32) {definitional};

\end{tikzpicture}
\end{center}

# How much do these results show?

Most equivalence results in philosophy of physics are proved at the
categorical level:

- Hamiltonian and Lagrangian mechanics (Barrett 2019)
- general relativity and Einstein algebras (Rosenstock, Barrett &
  Weatherall 2015)

But if it's not sufficient for first-order theories, why assume it's sufficient for these theories?

# Two levels

Accepting a theory involves two distinct acts:

1. Downstairs: Assertions we make about objects
2. Upstairs: Attitude toward our assertions
   - confidence levels
   - tolerance for reformulation

Quine-style naturalism has only downstairs. That's why it cannot
understand what formal theories of equivalence are good for.

# A program

- Formal results about equivalence are part of the classic tradition
  of critical philosophy -- i.e. of reflecting on the rules that
  govern our scientific practice.
- Philosophers who don't recognize such rules are not going to find a
  relation of "equivalence" in the world.
- Kant said that scientific implies mathematical. That's why we want a
  "formal" account of equivalence; we want something that is
  intersubjectively accessible.
  - Make your theory explicit, and also make your criterion of
    equivalence explicit.

