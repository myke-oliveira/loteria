from random import sample

class Aposta():

	# __qtd_dezenas, int entre 6 e 10
	# __resultado
	# __total_jogos, int
	# __jogos

	def __init__(self, qtd_dezenas, total_jogos):
		self.set_qtd_dezenas(qtd_dezenas)
		self.set_total_jogos(total_jogos)

	def get_qtd_dezenas(self):
		return self.__qtd_dezenas

	def set_qtd_dezenas(self, qtd_dezenas):
		if type(qtd_dezenas) != int:
			raise TypeError('O tipo de quantidade de dezenas deve ser inteiro.')
		if 6 <= qtd_dezenas <= 10:
			self.__qtd_dezenas = qtd_dezenas
		else:
			raise ValueError('A quantidade de dezenas deve estar entre 6 e 10.')

	def get_resultado(self):
		return self.__resultado

	def set_resultado(self, resultado):
		if type(resultado) != list:
			raise TypeError('O tipo de resultado deve ser lista.')
		if any(type(e) != int for e in resultado):
			raise TypeError('Os tipo dos elementos de resultado devem ser inteiros.')
		if len(resultado) != 6:
			raise ValueError('O resultado deve ter seis elementos.')
		self.__resultado = resultado

	def get_total_jogos(self):
		return self.__total_jogos

	def set_total_jogos(self, total_jogos):
		if type(total_jogos) != int:
			raise TypeError('O tipo de total de jogos deve ser inteiro.')
		self.__total_jogos = total_jogos

	def get_jogos(self):
		return self.__jogos

	def set_jogos(self, jogos):
		if type(jogos) != list:
			raise TypeError('O tipo de jogos deve ser lista.')
		if any(type(jogo) != list for jogo in jogos):
			raise TypeError('Cada jogos de jogos deve ser lista.')
		self.__jogos = jogos

	def __get_array(self):
		return sample(range(1, 61), self.get_qtd_dezenas())

	def __gerar_jogos(self):
		self.__jogos = [self.__get_array() for i in range(self.get_total_jogos())]

	def __gerar_resultado(self):
		self.__resultado = sample(range(1, 61), 6)
		self.__resultado.sort()

	def get_html_result(self):
		if not '__jogos' in vars(self):
			self.__gerar_jogos()
		if not '__resultado' in vars(self):
			self.__gerar_resultado()
		html = '<table><tr><th>Jogo</th><th>Quantidade de Dezenas Sorteadas</th></tr>\n'
		for i, jogo in enumerate(self.__jogos, 1):
			qtd_dezenas_sorteadas = sum(escolha == dezena
				for escolha in jogo for dezena in self.__resultado)
			html += '<tr><td>{}</td><td>{}</td></tr>\n'.format(i, qtd_dezenas_sorteadas)
		html += '</table>'
		return html
