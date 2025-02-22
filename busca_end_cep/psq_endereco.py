from brazilcep import get_address_from_cep

try:
    endereco = get_address_from_cep('00000-000')  # Exemplo de CEP inválido
    print(endereco)
except Exception as e:
    print(f"Erro ao buscar CEP: {e}")