# Deixar isso daqui, poderia servir como um meio de criar o logger a parte da aplicação
# e a parte de todas as visualizações chamando apenas funçoes específicas para que fornecam
# o log necessário, e de maneira limpa.
from flask import current_app
from datetime import datetime

class Log:

	@staticmethod 
	def get_log_time():
		return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

	@staticmethod
	def cadastro_de_usuario(request):
		current_app.logger.info(f"= {Log.get_log_time()} {'=' * 50}\nCadastro do usuário com informações:\nName: {request.form['name']}\nEmail: {request.form['email']}")

	@staticmethod
	def cadastro_de_mesa():
		current_app.logger.info(f"= {Log.get_log_time()} {'=' * 50}\n")


	@staticmethod
	def cadastro_de_personagem():
		current_app.logger.info(f"= {Log.get_log_time()} {'=' * 50}\n")





