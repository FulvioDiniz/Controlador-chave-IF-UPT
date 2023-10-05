# Criar Classe

Na pasta backend crie outra pasta de nome filter.py e insira os codigos abaixo:

```python
from pydantic import BaseModel

class Chave(BaseModel):
  id: int
  nome: str
  situacao: str
  status:boolean

class Servidor(BaseModel):
  id: int
  nome: str
  cpf: str
  contato:int
  nascimento: st
  status:boolean
class Emprestimo(BaseModel):
    id: int
    data_emprestimo: str
    data_devolucao: str
    status:bool
    chave = Chave
    servidor_pegou = chave.Servidor
    servido_retornou = chave.Servidor
```
