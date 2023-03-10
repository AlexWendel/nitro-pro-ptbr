### Tradução Nitro Pro
Tradução não oficial para Português do Brasil do Software Nitro Pro.Tradução não oficial para Português do Brasil do Software Nitro Pro.
<!--
##### Progresso da tradução:

| Arquivo | Traduzido | Revisado | Finalizado |
| :-------: | :---------: | :--------: | :----------: |
| np_page_edit.dll | Sim | Não | Não | 


#### Como gerar os arquivos traduzidos
##### Manualmente:

>OBS: Para compilar os scripts e gerar as traduções é necessário o Software [Resource Hacker](http://www.angusj.com/resourcehacker/)

Copiar todos os arquivos das pastas:  "MUI Files", "RC Files" e "BIN Files" para um diretório em comum, temporário, onde ficará os arquivos compilados e arquivos de saída.

Para cada arquivo de recurso (.rc) presente na pasta comum, compilar o resource usando o comando:

```ResourceHacker.exe  -open <nome_do_arquivo>.rc -save <nome_do_arquivo>.res -action compile -log CON```

Para cada arquivo .res presente na pasta comum, criar um script à partir do seguinte template:

```
[FILENAMES]
Exe=<nome_do_arquivo>.mui
SaveAs=output/<nome_do_arquivo>.dll.mui
Log=logs/<nome_do_arquivo>.dll.mui.log
[COMMANDS]
-addoverwrite     <nome_do_arquivo>.res
```

##### Usando Python:
Para compilar todos os arquivos de recursos:
```python scripts/compile.py``` -->