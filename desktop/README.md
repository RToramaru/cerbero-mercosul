# Cérbero Mercosul Versão desktop

## Sobre

Nessa parte do processamento, é realizado a detecção de placas veiculares, para realizar tal tarefa o software foi divido em quatro partes. A seguir discutiremos sobre cada uma delas.

1. Detecção da região da placa.
    * Para a detecção é utlizado um modelo ONNX obtido pelo treiamento da rede convolucional [YOLOv7](https://github.com/WongKinYiu/yolov7) com os dados de veículos com placas do Mercosul de [Silvano, et al. 2020](https://data.mendeley.com/datasets/nx9xbs4rgx). Ao concluir a etapa de extração da placa, essa região é isolada e passada para as etapas seguintes.
2. Obter caracteres das placas.
    * Nessa etapa é aplicada um limiar na imagem para obter apenas os contornos na imagem, esses contornos são filtrados e agrupados somente os caractreres em uma nova imagem.
3. Reconhecimento dos caracteres.
    * A imagem dos caracteres é processada pelo algoritmo [EasyOCR
](https://github.com/JaidedAI/EasyOCR), que retorna uma string com o texto na imagem.
4. Armazenamento no banco de dados.
    * Com o texto da imagem, o texto da placa é armazena no banco de dados juntamente com a data atual, e a imagem da placa salva em base64.
5. Interface gráfica.
    * Para interface do aplicativo foi utilizado a biblioteca [PySide2](https://pypi.org/project/PySide2/).

## Demostração



``@author Rafael Almeida``