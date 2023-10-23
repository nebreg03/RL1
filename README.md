# RL1
Primera prova de RL

Hi ha un arxiu config.ini on es pot ficar el valor de tots els parametres. A excepció de:
 - Casella d'inici (run.py)
La politica que seguira per cada casella es definieix en un .txt on s'introdueix cada casella la probabilitat (entre 0 i 1) de cada moviment (U:up, D:down, L:left, R:right)

Per executar cal correr 'python run.py' dins la carpeta /prova. L'ouput mostra la graella que s'ha creat i el viatge del personatge

i.e:

Començant a: (1, 0)
| (0.0,     -    ) | (0.0,     -    ) | (0.0,     -    ) |
| (-1.0,  prohibit) | (0.0,     -    ) | (0.0,     -    ) |
| (0.0,     -    ) | (0.0,     -    ) | (1.0,   final  ) |

El primer valor marca la recompensa d'aquella casella, el segon el tipus de casella que es.

El personatge es moura fins sortir del mapa o bé quan arribi al final. T'anirà explicant tot el que fa, primer anunciarà que es mou, després agafara la recompensa de la seva casella, després mirarà la policy de la casella i la probabilitat de fer cada moviment. Després t'anuncia on es troba i on tria moure's, et diu on arribarà i dirà que s'ha mogut.

i.e:
Vaig a moure'm!
He sumat -1.0 a la recompensa
Llegint policy...
{'U': 0.0, 'D': 1.0, 'R': 0.0, 'L': 0.0}
Estava a 1 0
He triat  D
Aniré a 2 0
Pasa feta!

Finalment mostrarà la recompensa acomulada i la descomptada (des_rew=r1+r2\*gamma^1+r3\*gamma\*\*2...)

Si es fa python script.py s'executarà el run.py començant cada cop a una casella diferent. Un cop fet troba la millor casella per començar i executa un nou run amb el resultat optimitzat, és a dir apren i fa!