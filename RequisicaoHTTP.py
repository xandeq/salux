import asyncio
import aiohttp

async def obter_conteudo(sessao, endereco):
    async with sessao.get(endereco) as resposta:
        return await resposta.text()

async def obter_multiplos_conteudos(enderecos: list):
    async with aiohttp.ClientSession() as sessao:
        tarefas = [obter_conteudo(sessao, endereco) for endereco in enderecos]
        return await asyncio.gather(*tarefas)

if __name__ == "__main__":
    lista_enderecos = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.github.com"
    ]
    
    resultados = asyncio.run(obter_multiplos_conteudos(lista_enderecos))
    
    for i, conteudo in enumerate(resultados, 1):
        print(f"Conteúdo {i}:", conteudo[:200], "\n")
