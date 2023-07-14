import smtplib
import ssl
import email.message
t = 'funciona'

msg = email.message.Message()
msg['Subject'] = f"Teste disparando email: {t} :)"

body = """
Ola, mensagem de teste
"""

msg['From'] = 'bulletplayer01@gmail.com'
msg['To'] = 'Bullet@1234'
passaword = 'bulletplayer01@gmail.com'
msg.add_header('Contect - Type', 'text/html')
msg.set_payload(body)


context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', '587') as conexao:
    conexao.ehlo()
    conexao.starttls(context=context)
    conexao.login(msg['From'], passaword)
    conexao.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
