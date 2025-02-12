# Automacao de Processos

Este projeto automatiza a inserção de códigos em um sistema, utilizando PyAutoGUI para interação com a interface gráfica e pandas para manipulação de arquivos Excel.

## 📌 Requisitos

Certifique-se de ter o Python instalado e instale as dependências necessárias:

```bash
pip install pyautogui pyperclip pandas openpyxl customtkinter
```

## 🔧 Como Usar

1. **Execute o script**

   ```bash
   python script.py
   ```

2. **Selecione um arquivo Excel**

   - Clique no botão "Abrir arquivo" e escolha um arquivo `.xlsx` contendo os códigos.

3. **Inicie a automação**

   - Pressione o botão "Começar" e, em seguida, abra o sistema onde deseja inserir os códigos.
   - O script aguardará 5 segundos antes de iniciar.

4. **O que o script faz?**

   - Lê os códigos do arquivo Excel.
   - Cola cada código no sistema e executa as ações necessárias.
   - Move o arquivo processado para a pasta `C:/Users/henri/Desktop/consulta precos/CONCLUIDOS`.

## 📂 Estrutura do Projeto

```
/consulta_precos
|-- CONCLUIDOS
|-- EMPRESAS
│-- locate_mouse.py
│-- requirements.txt
|-- script.py
```

## ⚠️ Observações

- O script utiliza **coordenadas fixas** do mouse. Se a interface do sistema mudar, será necessário ajustar as posições dos cliques.
- O código do Excel é convertido para uma string com 6 dígitos, adicionando `0` se necessário.
- O arquivo `locate_mouse.py` serve para reconhecer as coordenadas do mouse, ou seja, ele vai passar as coordenadas de `x` e `y` para o `pyautogui.click(x, y)`.



## 📝 Licença

Este projeto é de código aberto e pode ser modificado conforme necessário.

