# AnavNet

Client library to the [AnavNet](http://anavnet.hidrografico.pt/AvisosLocais/AvisosLocais.aspx) website, which provides the current warnings from the Portuguese maritime ports.
* Includes all the available port names and identifiers.
* Counts the total messages per port.
* Extracts all the information from the messages.
* Includes a console script to consume the library.

### Requirements

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
* [Requests](http://docs.python-requests.org/en/master/)

### Installation

```sh
$ pip install anavnet
```

### Usage

#### Library

```python
>>> from anavnet import AnavNet
>>> anavnet = AnavNet()
>>> anavnet.set_port(16)
>>> anavnet.get_total_messages()
>>> 12
>>> anavnet.get_message(1)
{'num_aviso': '288/18', 'dt_promulgacao': '23-Ago-2018', 'dt_inicio': '24-Ago-2018', 'dt_fim': '05-Set-2018', 'ent_promulgacao': 'Capitania do Porto de Lisboa - CAPIMARLISBOA', 'local': 'Rio Tejo - Cais Militar do Portinho da Costa.', 'assunto': 'Área interdita à navegação', 'descricao': 'No período de 24AGO a 05SET, está interdita a navegação a menos de 50 metros do Cais Militar do Portinho da Costa.', 'dt_cancelamento': 'Data de cancelamento: 05-Set-2018'}
```

#### Console script:

```sh
$ anavclient --help

usage: anavclient [-h]
                  (--list | --total TOTAL | --text TEXT TEXT | --json JSON JSON)

optional arguments:
  -h, --help        show this help message and exit
  --list            Lists available ports
  --total TOTAL     Gets the total of messages. Argument: PORT_ID
  --text TEXT TEXT  Get message as formatted text. Arguments: PORT_ID, MESSAGE_INDEX
  --json JSON JSON  Get message as JSON. Arguments: PORT_ID, MESSAGE_INDEX
```
 
### Tests

```sh
$ python -m unittest discover -s tests
```

License
----

BSD-3-Clause

