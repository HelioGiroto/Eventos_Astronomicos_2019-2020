#!/usr/bin python3
#!/usr/bin/env python3
# coding: utf-8
# Author: Helio Giroto
# Date: 21/03/2020

######## SCRIPT PARA CALCULAR A DISTÂNCIA ENTRE O PLANETA TERRA E VÊNUS NO ANO DE 2020 ########
'''
	"Eu, Jesus, enviei o meu anjo, para vos testificar estas coisas nas igrejas.
	 Eu sou a raiz e a geração de Davi, a resplandecente estrela da manhã."
	 			    (Apoc 22:16)
'''

from skyfield.api import load
# para instalar este módulo acima, digite no Terminal: 
# (no CMD do Windows, omitir sudo):
# sudo python3 -m pip install -U skyfield --user

# chama catálogo de planetas:
planets = load('de421.bsp')

# define planetas:
terra = planets['earth']
venus = planets['venus']

# chama método de tempo:
ts = load.timescale()

# define ano para busca:
ano = 2020

# laço aninhado para mes e dia:
for mes in range(1, 13):
	for dia in range(1, 32):
		terra_venus = terra.at(ts.utc(ano, mes, dia)).observe(venus)
		# o valor da distancia entre os dois planetas (em U.A.) é o item [2]:
		# para receber valores: ra ou dec; basta testar os items [0] e/ou [1] respectivamente.
		ua = terra_venus.radec()[2]
		# Será impresso na tela:
		print(str(dia) + '/' + str(mes) + '/' + str(ano) + ' - ' + str(ua))


########### RESULTADO ##############

'''
$ python3 2020_terra_venus_distancia.py 

1/1/2020 - 1.27803 au
2/1/2020 - 1.27238 au
3/1/2020 - 1.26671 au
4/1/2020 - 1.261 au
5/1/2020 - 1.25527 au
6/1/2020 - 1.2495 au
7/1/2020 - 1.24371 au
8/1/2020 - 1.23789 au
9/1/2020 - 1.23203 au
10/1/2020 - 1.22615 au
11/1/2020 - 1.22025 au
12/1/2020 - 1.21431 au
13/1/2020 - 1.20835 au
14/1/2020 - 1.20235 au
15/1/2020 - 1.19634 au
16/1/2020 - 1.19029 au
17/1/2020 - 1.18421 au
18/1/2020 - 1.17811 au
19/1/2020 - 1.17198 au
20/1/2020 - 1.16582 au
21/1/2020 - 1.15963 au
22/1/2020 - 1.15342 au
23/1/2020 - 1.14717 au
24/1/2020 - 1.14089 au
25/1/2020 - 1.13459 au
26/1/2020 - 1.12825 au
27/1/2020 - 1.12189 au
28/1/2020 - 1.11549 au
29/1/2020 - 1.10907 au
30/1/2020 - 1.10261 au
31/1/2020 - 1.09613 au
1/2/2020 - 1.08961 au
2/2/2020 - 1.08307 au
3/2/2020 - 1.07649 au
4/2/2020 - 1.06989 au
5/2/2020 - 1.06326 au
6/2/2020 - 1.0566 au
7/2/2020 - 1.04991 au
8/2/2020 - 1.0432 au
9/2/2020 - 1.03646 au
10/2/2020 - 1.02969 au
11/2/2020 - 1.02289 au
12/2/2020 - 1.01607 au
13/2/2020 - 1.00922 au
14/2/2020 - 1.00235 au
15/2/2020 - 0.995453 au
16/2/2020 - 0.988529 au
17/2/2020 - 0.981579 au
18/2/2020 - 0.974603 au
19/2/2020 - 0.967601 au
20/2/2020 - 0.960573 au
21/2/2020 - 0.953519 au
22/2/2020 - 0.946439 au
23/2/2020 - 0.939333 au
24/2/2020 - 0.932201 au
25/2/2020 - 0.925043 au
26/2/2020 - 0.917859 au
27/2/2020 - 0.910649 au
28/2/2020 - 0.903415 au
29/2/2020 - 0.896155 au
30/2/2020 - 0.88887 au
31/2/2020 - 0.881561 au
1/3/2020 - 0.88887 au
2/3/2020 - 0.881561 au
3/3/2020 - 0.874228 au
4/3/2020 - 0.866872 au
5/3/2020 - 0.859492 au
6/3/2020 - 0.852091 au
7/3/2020 - 0.844668 au
8/3/2020 - 0.837225 au
9/3/2020 - 0.829762 au
10/3/2020 - 0.822279 au
11/3/2020 - 0.814779 au
12/3/2020 - 0.807261 au
13/3/2020 - 0.799726 au
14/3/2020 - 0.792175 au
15/3/2020 - 0.784608 au
16/3/2020 - 0.777026 au
17/3/2020 - 0.76943 au
18/3/2020 - 0.761819 au
19/3/2020 - 0.754193 au
20/3/2020 - 0.746555 au
21/3/2020 - 0.738903 au
22/3/2020 - 0.731239 au
23/3/2020 - 0.723563 au
24/3/2020 - 0.715876 au
25/3/2020 - 0.708178 au
26/3/2020 - 0.700471 au
27/3/2020 - 0.692754 au
28/3/2020 - 0.685029 au
29/3/2020 - 0.677297 au
30/3/2020 - 0.669559 au
31/3/2020 - 0.661816 au
1/4/2020 - 0.65407 au
2/4/2020 - 0.646321 au
3/4/2020 - 0.638571 au
4/4/2020 - 0.630821 au
5/4/2020 - 0.623074 au
6/4/2020 - 0.615331 au
7/4/2020 - 0.607594 au
8/4/2020 - 0.599865 au
9/4/2020 - 0.592146 au
10/4/2020 - 0.584439 au		###### PÁSCOA ######
11/4/2020 - 0.576746 au		###### PÁSCOA ######
12/4/2020 - 0.569069 au		###### PÁSCOA ######
13/4/2020 - 0.561409 au
14/4/2020 - 0.55377 au
15/4/2020 - 0.546152 au
16/4/2020 - 0.538558 au
17/4/2020 - 0.53099 au
18/4/2020 - 0.52345 au
19/4/2020 - 0.51594 au
20/4/2020 - 0.508464 au
21/4/2020 - 0.501023 au
22/4/2020 - 0.493621 au
23/4/2020 - 0.48626 au
24/4/2020 - 0.478944 au
25/4/2020 - 0.471675 au
26/4/2020 - 0.464458 au
27/4/2020 - 0.457296 au
28/4/2020 - 0.450193 au
29/4/2020 - 0.443154 au
30/4/2020 - 0.436183 au
31/4/2020 - 0.429285 au
1/5/2020 - 0.429285 au
2/5/2020 - 0.422465 au		### DATA LIMITE PARA SER VISÍVEL NO CÉU A NOITE EM SP: (2 de maio) ###
3/5/2020 - 0.415728 au
4/5/2020 - 0.409081 au
5/5/2020 - 0.40253 au
6/5/2020 - 0.396081 au
7/5/2020 - 0.38974 au
8/5/2020 - 0.383515 au
9/5/2020 - 0.377413 au
10/5/2020 - 0.371442 au
11/5/2020 - 0.365607 au
12/5/2020 - 0.359918 au
13/5/2020 - 0.354383 au
14/5/2020 - 0.349008 au
15/5/2020 - 0.343803 au
16/5/2020 - 0.338776 au
17/5/2020 - 0.333935 au
18/5/2020 - 0.32929 au
19/5/2020 - 0.324849 au
20/5/2020 - 0.320622 au
21/5/2020 - 0.316618 au
22/5/2020 - 0.312846 au
23/5/2020 - 0.309314 au
24/5/2020 - 0.306032 au
25/5/2020 - 0.303009 au
26/5/2020 - 0.300252 au
27/5/2020 - 0.297771 au
28/5/2020 - 0.295572 au
29/5/2020 - 0.293662 au
30/5/2020 - 0.292049 au
31/5/2020 - 0.290737 au		###### PENTECOSTES ######
1/6/2020 - 0.289732 au
2/6/2020 - 0.289037 au
3/6/2020 - 0.288656 au
4/6/2020 - 0.288589 au	   ######### MAIOR PROXIMIDADE #########
5/6/2020 - 0.288838 au
6/6/2020 - 0.289401 au
7/6/2020 - 0.290276 au
8/6/2020 - 0.291462 au
9/6/2020 - 0.292952 au
10/6/2020 - 0.294743 au
11/6/2020 - 0.296828 au
12/6/2020 - 0.299199 au		### VOLTA A SER VISÍVEL ÀS 6 DA MANHÃ NO LESTE ###
13/6/2020 - 0.301851 au
14/6/2020 - 0.304774 au
15/6/2020 - 0.30796 au
16/6/2020 - 0.311399 au
17/6/2020 - 0.315084 au
18/6/2020 - 0.319004 au
19/6/2020 - 0.32315 au
20/6/2020 - 0.327512 au
21/6/2020 - 0.332082 au
22/6/2020 - 0.33685 au
23/6/2020 - 0.341806 au		### A PARTIR DAS 5 DA MANHÃ É VISÍVEL À LESTE ###
24/6/2020 - 0.346943 au
25/6/2020 - 0.352252 au
26/6/2020 - 0.357724 au
27/6/2020 - 0.363351 au
28/6/2020 - 0.369127 au
29/6/2020 - 0.375043 au
30/6/2020 - 0.381092 au
31/6/2020 - 0.387268 au
1/7/2020 - 0.387268 au
2/7/2020 - 0.393563 au
3/7/2020 - 0.399972 au
4/7/2020 - 0.406487 au
5/7/2020 - 0.413103 au
6/7/2020 - 0.419813 au
7/7/2020 - 0.426613 au
8/7/2020 - 0.433496 au
9/7/2020 - 0.440457 au
10/7/2020 - 0.44749 au
11/7/2020 - 0.454593 au
12/7/2020 - 0.461758 au
13/7/2020 - 0.468983 au
14/7/2020 - 0.476264 au
15/7/2020 - 0.483596 au
16/7/2020 - 0.490975 au
17/7/2020 - 0.4984 au
18/7/2020 - 0.505865 au
19/7/2020 - 0.513368 au
20/7/2020 - 0.520907 au
21/7/2020 - 0.528478 au
22/7/2020 - 0.53608 au
23/7/2020 - 0.54371 au
24/7/2020 - 0.551366 au
25/7/2020 - 0.559047 au
26/7/2020 - 0.56675 au
27/7/2020 - 0.574474 au
28/7/2020 - 0.582217 au
29/7/2020 - 0.589978 au
30/7/2020 - 0.597754 au
31/7/2020 - 0.605546 au
1/8/2020 - 0.61335 au
2/8/2020 - 0.621165 au
3/8/2020 - 0.62899 au
4/8/2020 - 0.636823 au
5/8/2020 - 0.644662 au
6/8/2020 - 0.652506 au
7/8/2020 - 0.660353 au
8/8/2020 - 0.668202 au
9/8/2020 - 0.676052 au
10/8/2020 - 0.6839 au
11/8/2020 - 0.691747 au
12/8/2020 - 0.69959 au
13/8/2020 - 0.707428 au
14/8/2020 - 0.715261 au
15/8/2020 - 0.723087 au
16/8/2020 - 0.730905 au
17/8/2020 - 0.738714 au
18/8/2020 - 0.746514 au
19/8/2020 - 0.754304 au
20/8/2020 - 0.762084 au
21/8/2020 - 0.769852 au
22/8/2020 - 0.777608 au
23/8/2020 - 0.785353 au
24/8/2020 - 0.793085 au
25/8/2020 - 0.800805 au
26/8/2020 - 0.808512 au
27/8/2020 - 0.816205 au
28/8/2020 - 0.823885 au
29/8/2020 - 0.831551 au
30/8/2020 - 0.839202 au
31/8/2020 - 0.846837 au
1/9/2020 - 0.854457 au
2/9/2020 - 0.86206 au
3/9/2020 - 0.869646 au
4/9/2020 - 0.877213 au
5/9/2020 - 0.884762 au
6/9/2020 - 0.892291 au
7/9/2020 - 0.899801 au
8/9/2020 - 0.907289 au
9/9/2020 - 0.914756 au
10/9/2020 - 0.922201 au
11/9/2020 - 0.929624 au
12/9/2020 - 0.937022 au
13/9/2020 - 0.944397 au
14/9/2020 - 0.951748 au
15/9/2020 - 0.959074 au
16/9/2020 - 0.966374 au
17/9/2020 - 0.973648 au
18/9/2020 - 0.980897 au
19/9/2020 - 0.98812 au		######## TROMBETAS (5781) #######
20/9/2020 - 0.995316 au		######## TROMBETAS (5781) #######
21/9/2020 - 1.00249 au
22/9/2020 - 1.00963 au
23/9/2020 - 1.01675 au
24/9/2020 - 1.02384 au
25/9/2020 - 1.03091 au
26/9/2020 - 1.03795 au
27/9/2020 - 1.04497 au
28/9/2020 - 1.05195 au
29/9/2020 - 1.05891 au
30/9/2020 - 1.06585 au
31/9/2020 - 1.07275 au
1/10/2020 - 1.07275 au
2/10/2020 - 1.07963 au
3/10/2020 - 1.08648 au
4/10/2020 - 1.0933 au
5/10/2020 - 1.10009 au
6/10/2020 - 1.10686 au
7/10/2020 - 1.11359 au
8/10/2020 - 1.12029 au
9/10/2020 - 1.12696 au
10/10/2020 - 1.13359 au
11/10/2020 - 1.1402 au
12/10/2020 - 1.14677 au
13/10/2020 - 1.15331 au
14/10/2020 - 1.15982 au
15/10/2020 - 1.16629 au
16/10/2020 - 1.17273 au
17/10/2020 - 1.17913 au
18/10/2020 - 1.1855 au
19/10/2020 - 1.19184 au
20/10/2020 - 1.19814 au
21/10/2020 - 1.20441 au
22/10/2020 - 1.21064 au
23/10/2020 - 1.21684 au
24/10/2020 - 1.22301 au
25/10/2020 - 1.22915 au
26/10/2020 - 1.23525 au
27/10/2020 - 1.24131 au
28/10/2020 - 1.24735 au
29/10/2020 - 1.25335 au
30/10/2020 - 1.25931 au
31/10/2020 - 1.26524 au
1/11/2020 - 1.27114 au
2/11/2020 - 1.277 au
3/11/2020 - 1.28283 au
4/11/2020 - 1.28862 au
5/11/2020 - 1.29438 au
6/11/2020 - 1.3001 au
7/11/2020 - 1.30578 au
8/11/2020 - 1.31143 au
9/11/2020 - 1.31704 au
10/11/2020 - 1.32261 au
11/11/2020 - 1.32815 au
12/11/2020 - 1.33364 au
13/11/2020 - 1.3391 au
14/11/2020 - 1.34452 au
15/11/2020 - 1.3499 au
16/11/2020 - 1.35524 au
17/11/2020 - 1.36054 au
18/11/2020 - 1.36581 au
19/11/2020 - 1.37103 au
20/11/2020 - 1.37622 au
21/11/2020 - 1.38137 au
22/11/2020 - 1.38648 au
23/11/2020 - 1.39156 au
24/11/2020 - 1.3966 au
25/11/2020 - 1.4016 au
26/11/2020 - 1.40656 au
27/11/2020 - 1.41149 au
28/11/2020 - 1.41638 au
29/11/2020 - 1.42123 au
30/11/2020 - 1.42605 au
31/11/2020 - 1.43083 au
1/12/2020 - 1.43083 au
2/12/2020 - 1.43557 au
3/12/2020 - 1.44027 au
4/12/2020 - 1.44494 au
5/12/2020 - 1.44957 au
6/12/2020 - 1.45416 au
7/12/2020 - 1.45871 au
8/12/2020 - 1.46322 au
9/12/2020 - 1.4677 au
10/12/2020 - 1.47213 au
11/12/2020 - 1.47653 au
12/12/2020 - 1.48088 au
13/12/2020 - 1.4852 au
14/12/2020 - 1.48947 au
15/12/2020 - 1.49371 au
16/12/2020 - 1.4979 au
17/12/2020 - 1.50206 au
18/12/2020 - 1.50617 au
19/12/2020 - 1.51025 au
20/12/2020 - 1.51429 au
21/12/2020 - 1.51829 au
22/12/2020 - 1.52225 au
23/12/2020 - 1.52618 au
24/12/2020 - 1.53006 au
25/12/2020 - 1.53391 au
26/12/2020 - 1.53773 au
27/12/2020 - 1.5415 au
28/12/2020 - 1.54524 au
29/12/2020 - 1.54894 au
30/12/2020 - 1.5526 au
31/12/2020 - 1.55623 au


###############################################3

# DIAS FESTIVOS EM ISRAEL: 
# FESTAS 2020

$ hdate -H 2020
hdate: ALERT: time zone not entered, using system local time zone: -03, -3:0 UTC
hdate: ALERT: guessing... will use co-ordinates for Buenos Aires

2020:

January:
Tuesday, 7 January 2020, 10 Tevet 5780
Asara B'Tevet

February:
Monday, 10 February 2020, 15 Sh'vat 5780
Tu B'Shvat
Tuesday, 25 February 2020, 30 Sh'vat 5780
Family Day

March:
Monday, 9 March 2020, 13 Adar 5780
Ta'anit Esther
Tuesday, 10 March 2020, 14 Adar 5780
Purim
Wednesday, 11 March 2020, 15 Adar 5780
Shushan Purim


April:

############# PÁSCOA #####################
Thursday, 9 April 2020, 15 Nisan 5780
Pesach
Friday, 10 April 2020, 16 Nisan 5780
Hol hamoed Pesach
Saturday, 11 April 2020, 17 Nisan 5780
Hol hamoed Pesach
Sunday, 12 April 2020, 18 Nisan 5780
Hol hamoed Pesach

Monday, 13 April 2020, 19 Nisan 5780
Hol hamoed Pesach
Tuesday, 14 April 2020, 20 Nisan 5780
Hol hamoed Pesach
Wednesday, 15 April 2020, 21 Nisan 5780
Pesach VII
Tuesday, 21 April 2020, 27 Nisan 5780
Yom HaShoah
Tuesday, 28 April 2020, 4 Iyyar 5780
Yom HaZikaron
Wednesday, 29 April 2020, 5 Iyyar 5780
Yom HaAtzma'ut


May:
Tuesday, 12 May 2020, 18 Iyyar 5780
Lag B'Omer
Friday, 22 May 2020, 28 Iyyar 5780
Yom Yerushalayim
Thursday, 28 May 2020, 5 Sivan 5780
Erev Shavuot

################ PENTECOSTES ##################
Friday, 29 May 2020, 6 Sivan 5780
Shavuot


June:


July:
Thursday, 9 July 2020, 17 Tammuz 5780
Tzom Tammuz
Tuesday, 21 July 2020, 29 Tammuz 5780
Zeev Zhabotinsky day
Thursday, 30 July 2020, 9 Av 5780
Tish'a B'Av

August:
Wednesday, 5 August 2020, 15 Av 5780
Tu B'Av


September:

################ TROMBETAS #################
Saturday, 19 September 2020, 1 Tishrei 5781
Rosh Hashana I
Sunday, 20 September 2020, 2 Tishrei 5781
Rosh Hashana II

Monday, 21 September 2020, 3 Tishrei 5781
Tzom Gedaliah
Sunday, 27 September 2020, 9 Tishrei 5781
Erev Yom Kippur
Monday, 28 September 2020, 10 Tishrei 5781
Yom Kippur

October:
Saturday, 3 October 2020, 15 Tishrei 5781
Sukkot
Sunday, 4 October 2020, 16 Tishrei 5781
Hol hamoed Sukkot
Monday, 5 October 2020, 17 Tishrei 5781
Hol hamoed Sukkot
Tuesday, 6 October 2020, 18 Tishrei 5781
Hol hamoed Sukkot
Wednesday, 7 October 2020, 19 Tishrei 5781
Hol hamoed Sukkot
Thursday, 8 October 2020, 20 Tishrei 5781
Hol hamoed Sukkot
Friday, 9 October 2020, 21 Tishrei 5781
Hoshana raba
Saturday, 10 October 2020, 22 Tishrei 5781
Shmini Atzeret
Thursday, 29 October 2020, 11 Cheshvan 5781
Yitzhak Rabin memorial day

November:

December:
Friday, 11 December 2020, 25 Kislev 5781
Chanukah
Saturday, 12 December 2020, 26 Kislev 5781
Chanukah
Sunday, 13 December 2020, 27 Kislev 5781
Chanukah
Monday, 14 December 2020, 28 Kislev 5781
Chanukah
Tuesday, 15 December 2020, 29 Kislev 5781
Chanukah
Wednesday, 16 December 2020, 1 Tevet 5781
Chanukah
Thursday, 17 December 2020, 2 Tevet 5781
Chanukah
Friday, 18 December 2020, 3 Tevet 5781
Chanukah
Friday, 25 December 2020, 10 Tevet 5781
Asara B'Tevet


'''
