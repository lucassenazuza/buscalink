import app
from flask import render_template, request, redirect, url_for
from models.form import LoginForm
from services.functions import Services, Popular
from models.tables import Element, Link
from app import app
from app import db


# funciona para roteamento da aplicação

@app.route('/', methods=['GET', "POST"])
def index():
    form = LoginForm()
    return render_template("index.html", form=form)


@app.route('/showall', methods=["GET"])
def showall():
    try:
        all_elements = Element.query.all()
        all_links = Link.query.all()
    except:
        print('Erro na busca')
    # print(all_elements)
    # print(all_links)
    return render_template("showall.html", all_elements=all_elements, all_links=all_links)


@app.route('/search', methods=['POST', 'GET'])
def list():
    if request.method == 'POST':
        searchName = request.form['searchName']
        service = Services(searchName, 10)
        try:
            element = Element(searchName)
            try:
                db.session.add(element)
                db.session.commit()
            except:
                print(f'Erro Salvar {searchName} Elemento no banco de dados')
        except:
            print('Erro Criar Elemento')
            # Salvando os links no BD
        lista = service.search_name()
        for link_url in lista:
            try:
                link = Link(link_url, element.id)
                try:
                    db.session.add(link)
                    db.session.commit()
                except:
                    print(f'Erro Salvar {link_url}  no banco de dados')
            except:
                print('Erro Criar Elemento')
                return redirect(url_for('index'))

        return render_template('list.html', lista=lista, name=searchName)
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:id>',methods=['GET'])
def delete(id):
    link = Link.query.get(id)
    db.session.delete(link)
    db.session.commit()
    return redirect(url_for('showall'))



@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')


@app.route('/statistic', methods=["GET"])
def statistic():
    try:
        all_elements = [element.elementName for element in Element.query.all()]
        all_links = [link.link for link in Link.query.all()]
    except:
        print('Erro na busca')
        return render_template("index.html")

    number_elements = len(all_elements)
    number_links = len(all_links)
    try:
        if (number_elements > 0):
            popular = Popular(all_elements)
            most_popular = popular.find_popular()
            return render_template("statistic.html", number_elements=number_elements, number_links=number_links,
                                    most_popular=most_popular)
        else:
            return render_template("statistic.html", number_elements=0, number_links=0,
                                   most_popular='none')
    except:
        print('Erro buscar mais popular')
    return render_template("index.html")
