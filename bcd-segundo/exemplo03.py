from base import Session, engine, Base
from pessoa import Pessoa
from telefone import Telefone

if __name__ == '__main__':
    print('Exemplo 03')

    #Gerando o esquema do BD
    #Base.metadata.create_all(engine)

    session = Session()

    juca    = Pessoa('Juca')
    ana     = Pessoa('Ana')

    session.add(juca)
    session.add(ana)

    tel_juca = Telefone('33812800', juca)
    tel_juca_cel = Telefone('998812800', juca)

    session.add(tel_juca)
    session.add(tel_juca_cel)

    session.commit()
    session.close()