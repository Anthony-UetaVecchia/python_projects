from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_requiem = Restaurante("Giorno's Dream Pizzaria", 'italiana')
bebida_suco = Bebida('Suco de Melância', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pão na Chapa', 3.0, 'Pão francês com manteiga tostado na chapa')
prato_paozinho.aplicar_desconto()
restaurante_requiem.adicionar_no_cardapio(bebida_suco)
restaurante_requiem.adicionar_no_cardapio(prato_paozinho)


def main():
    restaurante_requiem.exibir_cardapio

if __name__ == '__main__':
    main()