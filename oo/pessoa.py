class Pessoa:
    def __init__(self, nome=None, idade=30):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Olá mundo'

if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())
    p.nome = 'Tiago'
    print(p.nome)
    print(p.idade)