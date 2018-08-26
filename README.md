
# AnavNet

Client library to the [AnavNet](http://anavnet.hidrografico.pt/AvisosLocais/AvisosLocais.aspx) website, which provides messages about current portuguese ports warnings.
* Includes all the available port names and identifiers.
* Counts the total messages per port.
* Parses all the items of the messages.
* Includes a script to allow the usage from console.

### Requirements

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
* [Requests](http://docs.python-requests.org/en/master/)

### Installation

```sh
$ pip install anavnet
```

### Usage

```python
>>> from anavnet import AnavNet
>>> anavnet = AnavNet()
>>> anavnet.set_port(16)
>>> anavnet.get_total_messages()
>>> 12
>>> anavnet.get_message(1)
{'num_aviso': '288/18', 'dt_promulgacao': '23-Ago-2018', 'dt_inicio': '24-Ago-2018', 'dt_fim': '05-Set-2018', 'ent_promulgacao': 'Capitania do Porto de Lisboa - CAPIMARLISBOA', 'local': 'Rio Tejo - Cais Militar do Portinho da Costa.', 'assunto': 'Área interdita à navegação', 'descricao': 'No período de 24AGO a 05SET, está interdita a navegação a menos de 50 metros do Cais Militar do Portinho da Costa.', 'dt_cancelamento': 'Data de cancelamento: 05-Set-2018'}
```

Or the console script:

```sh
$ anavclient --help
```
 

### Tests

To run the available tests:

```sh
$ python -m unittest discover -s tests
```

License
----

BSD-3-Clause

