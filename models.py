from peewee import *

# Importando o banco de dados ao código
meu_bd = SqliteDatabase("meus_dados.db")

# Classe modelo com o BD
class BaseModel(Model):
    class Meta:
        database = meu_bd

# Representa o Tipo de Doce com seus atributos (classificacao(bolo, bombom, eclair, etc...), 
#                                               sabor(limão, chocolate, etc..),  
#                                               tipo de preço(por unidade ou kg),
#                                               preço e 
#                                               se está disponível ou não).
class TipoDoce(BaseModel):
    classificacao = CharField()
    sabor = CharField()
    tipoPreco = BooleanField()
    preco = DoubleField()
    disponivel = BooleanField()

# Representa o doce que stá sendo vendido, como 50g (peso) de Bolo(tipo.classificacao) de Chocolate(tipo.sabor) 
#                                               preço por kg(False)/unidade(True) (tipo.tipoPreco) R$9,99 (tipo.preco)
#                                               Não está Disponível.(False)/Está Disponível!(True) (tipo.disponivel).
class Doce(BaseModel):
    peso = DoubleField()
    tipo = ForeignKeyField(TipoDoce)

# Criar todas as classes e depois criar BD e tabelas
meu_bd.connect()
meu_bd.create_tables([Doce, TipoDoce])

