# Cérbero Mercosul

## Sobre

A aplicação Cerbero-Mercosul é um sistema para detecção de placas veiculares. O Cérbero foi projetado como um software para desktop desenvolvivo em Python, no qual realiza a detecção dos veículos e salva em um banco de dados PostgreSQL.

A consulta dos dados ocorre por meio de uma interface Web, desenvolvido em PHP, no qual usuários com acesso podem verificar a placa do veículo, o horário da captura, juntamente com a imagem do veículo no momento da captura.

## Projeto

O projeto contém tanto a parte Desktop quanto a parte Web.

Para consultar informações referente a parte Web, e visualizar uma demostração do seu uso, acesse a subpasta ``web``, la contém o README detalhando o desenvolvimento e as tecnologias utilizadas para essa parte. Para consultar informações referente a parte Desktop, e visualizar uma demostração do seu uso, acesse a subpasta ``desktop``, la contém o README detalhando o desenvolvimento e as tecnologias utilizadas para essa parte.

Uma reepresentação da arquitetura de pastas do projeto pode ser visto na estrutura abaixo:

```bash

📁desktop
    ┗ 📁detection_cerbero
        ┗ 📜__init__.py
        ┗ 📜detection.py
    ┗ 📁images
        ┗ 📜background.jpg
    ┗ 📁interface_cerbero
        ┗ 📜__init__.py
        ┗ 📜interface.py
    ┗ 📁model_onnx
        ┗ 📜plate.onnx
    ┗ 📜README.md
    ┗ 📜main.py
    ┗ 📜requirements.txt
📁web
    ┗ 📁cerbero-web
        ┗ 📁assets
        ┗ 📁commands
        ┗ 📁config
        ┗ 📁controllers
        ┗ 📁mail
        ┗ 📁migrations
        ┗ 📁models
        ┗ 📁runtime
        ┗ 📁tests
        ┗ 📁vagrant
        ┗ 📁views
        ┗ 📁web
        ┗ 📁widgets
        ┗ 📜Vagrantfile
        ┗ 📜codeception.yml
        ┗ 📜composer.json
        ┗ 📜docker-compose.yml
        ┗ 📜requirements.php
        ┗ 📜yii
        ┗ 📜yii.bat
    ┗ 📜README.md
    
```

## Clone do projeto
**Importante**
Para utilizar o repositório é necessário ter:
* **Python 3** : utilizado o Python 3.10.8

    * Download [Versão 3.10.8 64bits](https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe)
    
    * Download [última versão](https://www.python.org/downloads/)
    
*  **PHP 8** : utilizado o PHP 8.1.12

     * Download [Versão PHP 8.1.12 64bits](https://windows.php.net/downloads/releases/php-8.1.12-nts-Win32-vs16-x64.zip)
     
    * Download [última versão](https://www.php.net/downloads.php)
    
*  **PostgreSQL** : utilizado PostgreSQL Version 15

     * Download [Versão 15 64bits](https://www.enterprisedb.com/postgresql-tutorial-resources-training?uuid=7ce7e93f-e1eb-4e42-85fa-84c0c98859ee&campaignId=7012J000001h3GiQAI)
     
    * Download [última versão](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
    
* **Composer** :: utilizado versão Composer 2.4.4

    * Download [Versão  2.4.4 64bits](https://getcomposer.org/Composer-Setup.exe)
    
    * Download [última versão](https://getcomposer.org/download/)

Após instalado essas ferramentas, é necessário realizar o clone do repositório e instalar suas dependências.

```
git clone https://github.com/RToramaru/cerbero-mercosul.git

cd desktop
pip install -r requirements.txt

cd ..
cd web/cerbero-web
php composer.phar install

```
  

## Configuração do projeto

Após intalado todas as dependências, é necessário realizar algumas configurações em relação ao banco de dados.

Acesse o arquivo ``detection.py`` localizado no diretório ``cerbero-mercosul/desktop/detection_cerbero/`` e altere a linha 38 ``
self.con = psycopg2.connect(host='localhost', database='cerbero', user='postgres', password='1234')
`` para a configuração do seu banco de dados.

Configure também o banco na versão Web, aletrando o arquivo ``db.php`` no diretório ``cerbero-mercosul/web/cerbero-web/config/``

Após configurado o banco execute as migrations, acessando o caminho ``cerbero-mercosul/web/cerbero-web/`` e executando o comando:
```
 ./yii migration
 
 y 
```

  
## Executando

Para executar o projeto desktop naveque até o diretório ``cerbero-mercosul/desktop`` e execute o comando:

```
python main.py
```

Para executar o projeto web inicie o servidor PHP através do comando:

```
php -S localhost:8080
```
e navegue até o diretorio ``cerbero-mercosul/web/cerbero-web/web`` partindo do endereço `` http://localhost/``


### Demonstração

![](/screens/1.png)
![](/screens/2.png)
![](/screens/3.png)
![](/screens/4.png)


``@author Rafael Almeida``
