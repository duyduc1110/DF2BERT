# note

2019-12-19

3.2 Feature extraction

It is common to reduce the number of terms used in text classification. To increase classification accuracy by eliminating noise features. A noise feature is kind of that when added to the document representation, increase the classification error on new data. For example, the Bernoulli model is sensitive to noise features. 

There are five different feature utility measures, Chi-square test, likelihood ratio, pointwise mutual information, expected mutual information, and frequency based approaches.

Another approach to hypothesis testing also known as log likelihood ratio (LLR). LLR has the advantage that the statistic we are computing is more interpretable than the $χ2$ statistic. It is a number of likelihood ratio of two hypotheses: $Hypothesis \:1: P(t|c) = P(t|not \:c) = p_t$. It is a formalization of independence；$Hypothesis \:2: P(t|c) = p_1 ≠ p_2 = P(t|not \:c)$. It is a formalization of dependence. We are interested in $-2logλ = -2log(L(H1) / L(H2))$. We use maximum likelihood estimation (MLE) for $p_t$, $p_1$, and $p_2$. Then, we treat the corpus as binomial experiments.

<img src="C:\Users\Weber\Documents\GitHub\jpconf2020\Capture.1PNG.PNG" style="zoom: 33%;" />

For H1, the likelihood of n11 on-topic documents and n01 off-topic documents having term t is :
$$
C^{n_{11}+n_{10}}_{n_{11}}\big(\frac{n_{11}+n_{01}}{N}\big)^{n_{11}}\big(1-\frac{n_{11}+n_{01}}{N}\big)^{n_{10}}*C^{n_{01}+n_{00}}_{n_{01}}\big(\frac{n_{11}+n_{01}}{N}\big)^{n_{01}}\big(1-\frac{n_{11}+n_{01}}{N}\big)^{n_{00}}
$$
For H2, the likelihood is:
$$
C^{n_{11}+n_{10}}_{n_{11}}\big(\frac{n_{11}}{n_{11}+n_{10}}\big)^{n_{11}}\big(1-\frac{n_{11}}{n_{11}+n_{10}}\big)^{n_{10}}*C^{n_{01}+n_{00}}_{n_{01}}\big(\frac{n_{01}}{n_{01}+n_{00}}\big)^{n_{01}}\big(1-\frac{n_{01}}{n_{01}+n_{00}}\big)^{n_{00}}
$$
Then : $-2logλ = -2log(L(H1) / L(H2))$
$$
= -2log\frac{C^{n_{11}+n_{10}}_{n_{11}}\big(\frac{n_{11}+n_{01}}{N}\big)^{n_{11}}\big(1-\frac{n_{11}+n_{01}}{N}\big)^{n_{10}}*C^{n_{01}+n_{00}}_{n_{01}}\big(\frac{n_{11}+n_{01}}{N}\big)^{n_{01}}\big(1-\frac{n_{11}+n_{01}}{N}\big)^{n_{00}}}{C^{n_{11}+n_{10}}_{n_{11}}\big(\frac{n_{11}}{n_{11}+n_{10}}\big)^{n_{11}}\big(1-\frac{n_{11}}{n_{11}+n_{10}}\big)^{n_{10}}*C^{n_{01}+n_{00}}_{n_{01}}\big(\frac{n_{01}}{n_{01}+n_{00}}\big)^{n_{01}}\big(1-\frac{n_{01}}{n_{01}+n_{00}}\big)^{n_{00}}}
$$

$$
= -2log\frac{\big(\frac{n_{11}+n_{01}}{N}\big)^{n_{11}}\big(1-\frac{n_{11}+n_{01}}{N}\big)^{n_{10}}*\big(\frac{n_{11}+n_{01}}{N}\big)^{n_{01}}\big(1-\frac{n_{11}+n_{01}}{N}\big)^{n_{00}}}{\big(\frac{n_{11}}{n_{11}+n_{10}}\big)^{n_{11}}\big(1-\frac{n_{11}}{n_{11}+n_{10}}\big)^{n_{10}}*\big(\frac{n_{01}}{n_{01}+n_{00}}\big)^{n_{01}}\big(1-\frac{n_{01}}{n_{01}+n_{00}}\big)^{n_{00}}}
$$

The quantity $-2logλ$ has a clear intuitive interpretation (than the score of $χ2$ test). For example, if $-2logλ = 82.96$, then term $t$ is $e^{82.96/2}≈1.3\times10^{18}$ times more likely under the hypothesis that they are not independent than the independent hypothesis.[Mood et al. 1974] has shown that the quantity -2logλ is asymptotically $χ2$ distributed. So we can check the table of the $χ2$ distribution to test the null hypothesis H1 against the alternative hypothesis H2. [Dunning 1993] has also shown that for sparse data the likelihood ratio test can be more appropriate than the $χ2$ test.



Mood, A., Graybill, F., & Boes, D. Introduction to the Theory of Statistics–3rd Edition”, 1974.

Dunning, T. (1993). Accurate methods for the statistics of surprise and coincidence. *Computational linguistics*, *19*(1), 61-74.



12-20

---

+ Corpus


In order to evalute the flexibility of our model, introducing PTT (Chinese movie reviews) and Reader emotion (Yahoo Chinese news) is aimed to evaluate the multi-lingual flexibility of our model. And we want to test our method from binary and multiple class issues.