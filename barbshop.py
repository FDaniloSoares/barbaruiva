from flask import Flask, render_template, flash, request

#parte para enviar email
from flask_mail import Mail, Message

from forms import ReusableForm

app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


app.config.update(
	DEBUG= False,
	#EMAIL SETTINGS
	MAIL_SERVER= 'smtp.gmail.com',
	MAIL_PORT= 465,
	MAIL_USE_TLS= False,
	MAIL_USE_SSL= True,
	MAIL_USERNAME= 'fdanilosoares.mail@gmail.com' ,
	MAIL_PASSWORD= '********'
	)
mail = Mail(app)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/produtos/')
def produtos():
	return render_template("Produtos.html")

@app.route('/contatos/', methods=['GET', 'POST'])
def contatos():
	form = ReusableForm(request.form)
	if request.method == 'POST':
		name=request.form['name']
		email=request.form['email']
		mobile_phone=request.form['mobile_phone']
		mensagem=request.form['mensagem']
	
	if form.validate():
		try:
			msg = Message("Mensagem da Barbearia",
		  		sender="fdanilosoares.mail@gmail.com",
		  		recipients=["fdanilosoares@gmail.com"])
			msg.body = 'Cliente:'+name+'\nE_mail:'+email+'\nContato:'+mobile_phone+'\n' + mensagem
			mail.send(msg)
		except Exception:
			pass
		flash('Mensagam Enviada, Aguarde contato')
	else:
		flash(' ')
	
	return render_template("Contatos.html", form=form)

if __name__ == '__main__':
	app.run(debug = False)

