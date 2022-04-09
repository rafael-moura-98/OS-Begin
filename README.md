# Download

Download the zip file [HERE](https://github.com/rafael-moura-98/OS-Begin/archive/refs/heads/main.zip).

# Português

## Sobre

Este é um script que foi criado para agilizar a instalação de programas do Rafael, vulgo eu. Ele foi inteiramente pensado para minha necessidade mas contém algumas modificações que podem faze-lo ser util para outras pessoas. 

Antes de executar o script, uma explicação do que ele fará. Ele irá mudar a variável do Windows "Get-ExecutionPolicy" como "AllSigned" para baixar e instalar o Chocolatey, um gerenciador e instalador de pacotes por linha de comando. O chocolatey nos permitirá baixar o Python e todos os programas que estão listados em "download.txt".

## Como usar

Este programa permite três tipos de execução: criação de diretórios, download de programas e execução completa.

No CMD ou Powershell como **administrador**, execute a opção abaixo que mais lhe agradar.

### Criação de Diretórios

O Python será baixado e toda a arvore de arquivos abaixo será criada na pasta raiz onde se encontra este projeto.

Desktop\
|--------Drives And Tools\
|--------Edition-Creation\
|--------Games\
|--------|--------4Fun\
|--------|--------Platforms\
|--------|--------Story\
|--------Programming\
|--------Utils

Para executar apenas a criação de diretórios, adicione o parâmetro "-d" ou "--directories", sem as aspas, após o "set_choco_python.bat".

```
.\set_choco_python.bat -d
```

### Download de Programas (Default)

Além do Python será baixado também todos os programas listados no arquivo "download.txt". Cada linha deve conter apenas um nome de programa.

Para obter o nome exato de cada programa de acordo com o chocolatey, acesse seu [repositório](https://community.chocolatey.org/packages) de pacotes e cheque se está disponível.

Caso queira que um programa listado não seja baixado, acrescente "#" em qualquer posição da linha.

**ATENÇÃO**
>Insira o nome do pacote exatamente como está no chocolatey. Por exemplo, Steam não é apenas "steam", e sim "steam-client"; do contrário o pacote não irá baixar ou será baixado incorretamente.

*Para executar apenas o download dos arquivos, nenhum parâmetro é necessário.*

```
.\set_choco_python.bat
```

### Execução Completa 

Tanto a criação de diretórios quanto o download dos arquivos serão executados.

Para realizar a execução completa, adicione o parâmetro "-a" ou "--all", sem as aspas, após o "set_choco_python.bat".

```
.\set_choco_python.bat -a
```



# English

## About

This is a script that was created to speed up the installation of Rafael's programs, aka me. It was entirely designed for my needs but contains some modifications that can make it useful for other people.

Before running the script, an explanation of what it will do. It will change the Windows variable "Get-ExecutionPolicy" to "AllSigned" to download and install Chocolatey, a command-line package manager and installer. Chocolatey will allow us to download Python and all the programs that are listed in "download.txt".

## How to use

This program allows three types of execution: creating directories, downloading programs and running full.

In CMD or Powershell as **administrator**, run the option below that suits you best.

### Creating Directories

Python will be downloaded and the entire file tree below will be created in the root folder where this project is located.

Desktop\
|--------Drives And Tools\
|--------Edition-Creation\
|--------Games\
|--------|--------4Fun\
|--------|--------Platforms\
|--------|--------Story\
|--------Programming\
|--------Utils

To perform directory creation only, add the parameter "-d" or "--directories", without quotes, after "set_choco_python.bat".

```
.\set_choco_python.bat -d
```

### Download Programs (Default)

In addition to Python, all programs listed in the "download.txt" file will also be downloaded. Each line must contain only one program name.

For the exact name of each program according to chocolatey, go to your [repository](https://community.chocolatey.org/packages) and check if it is available.

If you want a listed program not to be downloaded, add "#" anywhere on the line.

**ATTENTION**
>Enter the package name exactly as it is on the chocolatey. For example, Steam is not just "steam", but "steam-client"; otherwise the package will not download or will download incorrectly.

*To perform only the download of files, no parameters are needed.*

```
.\set_choco_python.bat
```

### Complete Execution

Both directory creation and file download will be performed.

To perform the complete execution, add the parameter "-a" or "--all", without the quotes, after the "set_choco_python.bat".

```
.\set_choco_python.bat -a
```
