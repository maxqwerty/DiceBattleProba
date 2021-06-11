# Dice Battle result Probability
Measurements of probability to win in DnD-style battle

## Rules
The most of d20-based systems uses next rule:
* throw d20 and add modificators to attack an attribute;
* throw d20 and add modificators to calc the defence;
* compare:
    * if attack is more - attack wins
    * if attack is equal or less than defence - defence wins

This repository contains some scripts with logic to calculate probability for attacker to win against a defender with defined dice parameters.

## Formulas
Probability to win the attak:


<img src="https://render.githubusercontent.com/render/math?math=D1*\sum_{i=D1_{min}}^{D1_{max}}p(D2 < i)" />

Probability to roll less than:


<img src="https://render.githubusercontent.com/render/math?math=p(D2<i)=\sum_{j=1}^{j<i}p(D2=j)" />

Probability to roll exactly:


<img src="https://render.githubusercontent.com/render/math?math=p(D2==j)=\left\{\begin{matrix}0,%26%26D2_{max}<j||j<D2_{min}\\1/D2%26%26\end{matrix}\right." />
