from loteria	 import *

aposta = Aposta(6, 10)

assert aposta.get_qtd_dezenas() == 6
assert aposta.get_total_jogos() == 10


l = [1, 2, 3, 4, 5, 6]
aposta.set_resultado(l)
assert aposta.get_resultado() == l

jogos = [[1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9]]
aposta.set_jogos(jogos)
assert aposta.get_jogos() == jogos

print(aposta.get_html_result())

print('Teste finalizado com sucesso.')