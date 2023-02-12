"""
Interpretador do Python

python mod.py    (executa o mod) - ex.: python aula.py
python -u        (unbuffered)
python -m mod    (lib mod como script) - ex.: python -m venv ambiente
python -c 'cmd'  (comando) - ex.: python -c 'print("oi")'
python -i mod.py (iterativo com mod) - ex.: python -i aula57.py (no modo interativo)
python --help

The Zen of Python, por Tim Peters (python -c 'import this')

* Bonito é melhor que feio.
* Explícito é melhor que implícito.
* Simples é melhor que complexo.
* Complexo é melhor que complicado.
* Plano é melhor que aglomerado.
* Esparso é melhor que denso.
* Legibilidade conta.
* Casos especiais não são especiais o bastante para quebrar as regras.
* Embora a praticidade vença a pureza.
* Erros nunca devem passar silenciosamente:
    try:
        código
    except:
        ...
    - isso é um grande erro
    
* A menos que sejam explicitamente silenciados.
* Diante da ambiguidade, recuse a tentação de adivinhar.
* Deve haver só um -- e só um -- modo óbvio de fazer algo.
* Embora esse modo possa não ser óbvio à primeira vista a menos ue você seja holandês.
* Agora é melhor que nunca.
* Embora nunca frequentemente seja melhor que *exatamente* agora.
* Se a implementação é difícil de explicar, é uma má ideia.
* Se a implementação é fácil de explicar, pode ser uma boa ideia.
* Namespaces são uma grande ideia -- vamos fazer mais dessas!
"""

# quando há a necessidade de colocar vários comandos na mesma linha, pode-se usar ; para separar os comandos
print(1 + 1); print(2 + 2); print(3 + 3); print(4 + 4)
