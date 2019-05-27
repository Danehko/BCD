from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    print('Exemplo 2')

    engine = create_engine("sqlite:///lab05-ex02.sqlite")

    Session = sessionmaker(bind=engine)
    session = Session()

    Base = automap_base()
    Base.prepare(engine, reflect=True)

    #Tabelas existentes no meu banco
    Pessoa = Base.classes.Pessoa
    Telefones = Base.classes.Telefones

    #
    resultado = session.query(Pessoa).all()
    for linha in resultado:
        print('Id: {}, name: {}'.format(linha.idPessoa, linha.nome))

    ### filtrando
    resultado = session.query(Pessoa).filter(Pessoa.nome.ilike('J%')).all()
    for linha in resultado:
        print('Id: {}, name: {}'.format(linha.idPessoa, linha.nome))

    ### join
    resultado = session.query(Pessoa).join(Telefones).all()
    for linha in resultado:
        print('Id: {}, name: {}'.format(linha.idPessoa, linha.nome))
        for tel in linha.telefones_collection:
            print('tel: {}'.format(tel.numero))

    ### join usando filtes
    resultado = session.query(Pessoa).join(Telefones).all()
    for linha in resultado:
        print('Id: {}, name: {}'.format(linha.idPessoa, linha.nome))
        resultado = session.query(Telefones).filter(Telefones.idPessoa == linha.idPessoa).all()
        for tel in linha.telefones_collection:
            print('tel: {}'.format(tel.numero))