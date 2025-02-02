# Errata
Nous décrivons une liste de corrections du livre :

Michaël Baudin _« Introduction aux méthodes numériques. Théorie, algorithmes, implémentations et applications en Python »_. Dunod. Collection Sciences Sup. (2023)

Nous avons hiérarchisé les erreurs en fonction de leur nature :
- typographie (terrible) ;
- mathématique (horrible) ;
- grammaire ou orthographe (grave) ;
- esthétique (dramatique).

## Description
- Page 8 (typographie) : L'espace est trop long entre https et le symbole « : » dans la note en bas de page.
- Page 9 : La ligne : « x Vecteur: lettre latine [...] » apparaît deux fois dans la Table 5.
- Page 40 (mathématiques) : Dans l'équation (3.2), la dérivée i-ème de f s’applique au point a et non en x.
  Il faut lire :
```math
P_{n}(x) = \sum_{i=0}^{n} \frac{f^{(i)}(a)}{i!} (x-a)^{i}
```
- Page 197 (mathématiques) : Le théorème 8.11 est faux. Le théorème de Jackson indique que la meilleure approximation polynomiale permet d'attendre l'ordre $O(n^{-r})$, mais ne concerne pas les polynômes de Chebyshev. 
- Page 198 (mathématiques) : La phrase : "En appliquant ce théorème avec $r = 0$, on peut aussi comprendre la convergence de l'interpolation de Chebyshev sur une fonction discontinue de variation bornée." est fausse.
- Page 207 : Dans la section 8.12, il manque le mot "figure" entre [81] et 3 en bas à droite de la page. De plus, il manque le lien vers des références issues de Wikimedia Commons: File:Interpolation Data.svg, File:Piecewise constant.svg, File:Interpolation example linear.svg et File:Interpolation example polynomial.svg dont les figures 8.2 page 178 et 8.3 page 179 sont inspirées et adaptées par un portage en Python.
- Page 229 (grammaire) : Dans le paragraphe en bas de la page, il faut lire : « \[...\] pour la plupart 
  des formules de différences finies puisqu'elles ont des structures très similaires. »
  et non pas « \[...\] _sont_ des structures \[...\] ».
- Page 230 : Dans le paragraphe en haut de la page, la seconde apparition de « dominent »
  ne devrait pas s'y trouver. Il faut lire « Puisque les perturbations qui dominent le calcul
  sont les erreurs d'arrondi associées à la valeur de la fonction ~~dominent~~, ».
- Page 265 (mathématiques) : Le dénominateur de $\overline{t}$ est $\frac{1}{m}$ et non pas $\frac{1}{n}$.
  Le dénominateur de $\hat{\sigma}$ est $\frac{1}{m}$ et non pas $\frac{1}{n}$. 
- Page 265 (typographie) : La date minimale est $t_{\min}$ et non pas $t_{min}$ (typographie).
- Page 266 (grammaire) : Il faut lire « Pour comprendre pourquoi la méthode des équations normales etc. » et non pas « méthodes ».
- Page 267 (grammaire) : Il faut lire : « Par exemple, le conditionnement de la matrice de
  conception associé aux polynômes de Chebyshev que nous avons introduits dans
  la section etc. » au lieu de : « introduit ».
- Page 267 : Il faut lire : « [...] c'est pourquoi on devrait plutôt utiliser des polynômes
  de degré faible etc. » (doublure de plutôt)
- Page 268 (grammaire) : Il faut lire : « [...] la méthode de Gram-Schmidt permet de 
  déterminer $n$ vecteurs colonnes orthogonaux » au lieu de « orthogonales ».
- Page 271 (mathématiques) : Il faut lire : « Le coefficient de résistivité, noté $\alpha$, est tel que 
  $\rho(T)=\beta_2(1 + \alpha T)$ [...] » et non pas « $\rho(T)=\beta_1(1 + \alpha T)$ ».
- Page 275 (esthétique) : La taille de la figure 10.7 est trop grande.
- Page 391 (typographie) : Dans l'équation 14.7, il faut lire : « $c_{\min}(x)$ » et non pas « $c_{min}(x)$ ».
- Page 392 (mathématiques) : Dans le théorème 14.7, il faut lire : « Soit $x \neq 0$ un nombre réel
  tel que $f(x) \neq 0$, $f'(x) = 0$ et $f''(x) > 0$. ».

## Remerciements
- Vincent Breton
- Clément Roussel
