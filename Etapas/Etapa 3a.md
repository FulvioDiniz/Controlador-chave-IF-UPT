# Criar Classe

Para criar as classes utilizamos a biblioteca pydantic.

```python
from pydantic import BaseModel
```

```python
class Chave(BaseModel):
  id: int
  nome: str
  situacao: str
  status:boolean
```

```python
class Servidor(BaseModel):
  id: int
  nome: str
  cpf: str
  contato:int
  nascimento: st
  status:boolean
```

```python
class Emprestimo(BaseModel):
  id: int
  data_emprestimo: str
  data_devolucao: str
  status:boolean
  nome_servidor: str
  nome_chave: str
```
