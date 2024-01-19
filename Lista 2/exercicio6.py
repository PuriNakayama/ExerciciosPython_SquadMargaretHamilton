#funcao autenticacao do usuario
def autenticacao_usuario():
   login = input('Digite o seu login: ')
   senha = input('Digite a sua senha: ')

   if login == 'admin' and senha == 'admin123':
       print('Bem-vindo(a), admin!')
   else:
       print('Login ou senha incorretos. Acesso negado.')

autenticacao_usuario()