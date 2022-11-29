set up venv:
$   virtualenv env

activate it:
$   source env/bin/activate

install ipython in it:
$   pip3 install ipython

Output your dependencies to a file called requirements.txt...
...console should look like this...type some of these commands:
(env) melon-raffle % touch requirements.txt 
(env) melon-raffle % pip3 freeze > requirements.txt 
(env) melon-raffle % cat requirements.txt

create this readME w/ instructions:
$   touch readME.md