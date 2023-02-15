# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação do Python para uma pasta no caminho escolhido.
#  - geralmente a versão do Python utilizada para criar o AV, vai ser a versão instalada no AV.
# Ao ativar um ambiente virtual, a instalação do ambiente virtual será usada.
# venv é o módulo usado para criar ambientes virtuais.
# Pode-se ter qualquer nome, mas os mais comuns são:
# venv env .venv .env

# pra criar um AV:
# python -m venv venv

# como ativar:
# No Win: venv\Scripts\activate
# No Linux: source venv/bin/activate OU . venv/bin/activate

# qnd vc instala coisas com um AV ativo, as instalações vão pra esse AV

# pypi.org

# instalando pymysql:
# pip install pymysql

# desinstalando:
# pip uninstall pymysql

# pip freeze - mostra todas as coisas instaladas nesse AV - usado p/ criar requirements.txt
# requirements.txt - usado pra recriar esse AV
# pip freeze > requirements.txt - p/ criar esse arquivo

# pra usar o requirements:
# pip install -r .\requirements.txt