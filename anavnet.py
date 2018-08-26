#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import sys
import re
import requests
from bs4 import BeautifulSoup


class AnavNet:
    __url = "http://anavnet.hidrografico.pt/AvisosLocais/AvisosLocais.aspx?Porto="
    __keys = {
        'num_aviso': 'LabelNoAviso',
        'dt_promulgacao': 'DATAPROMULGACAOLabel',
        'dt_inicio': 'DATAINICIOLabel',
        'dt_fim': 'DATAFIMLabel',

        'ent_promulgacao': 'ENTPROMULGACAOLabel',
        'local': 'DESCPORTOLOCALLabel',
        'assunto': 'ASSUNTOLabel',
        'descricao': 'DESCRICAOLabel',

        'dt_cancelamento': 'LabelDataCancelar'
    }
    __ports = {
        37: "Angra do Heroismo",
        10: "Aveiro",
        1: "Caminha",
        14: "Cascais",
        8: "Douro",
        27: "Faro",
        11: "Figueira da Foz",
        32: "Funchal",
        40: "Horta",
        23: "Lagos",
        7: "Leixões",
        16: "Lisboa",
        12: "Nazaré",
        29: "Olhão",
        44: "Peniche",
        34: "Ponta Delgada",
        25: "Portimão",
        33: "Porto Santo",
        5: "Povoa de Varzim",
        36: "Praia da Vitória",
        43: "Santa Cruz das Flores",
        20: "Setúbal",
        22: "Sines",
        45: "Tavira",
        3: "Viana do Castelo",
        30: "Vila Real de Santo António",
        6: "Vila do Conde",
        35: "Vila do Porto",
    }
    __current_index = None
    __current_port = None
    __current_total = None
    __soup = None
    __values = {}

    def set_port(self, port):
        if port not in self.__ports:
            raise KeyError('Invalid port')
        self.__current_port = port
        r = requests.get(self.__url + str(self.__current_port))
        self.__soup = BeautifulSoup(r.text, features="html.parser")
        self.__count_total()

    def get_port_name(self):
        if self.__current_port is None:
            raise RuntimeError("Run set_port() first")
        return self.__ports[self.__current_port]

    def get_ports(self):
        return self.__ports

    def get_message(self, index, formatted=False):
        if self.__current_port is None:
            raise RuntimeError("Run set_port() first")

        self.__current_index = "{:0>2d}".format(index)  # Add a zero to the left

        if index > self.__current_total:
            raise IndexError("Index {} is bigger than {}".format(index, self.__current_total))
        else:
            self.__parse_message()
            if formatted is True:
                return self.__get_formatted_message()
            else:
                return self.__values

    def get_total_messages(self):
        if self.__current_port is None:
            raise RuntimeError("Run set_port() first")
        return self.__current_total

    def __count_total(self):
        """
        Calcula o numero total de mensagens na pagina
        """
        self.__current_total = len(self.__soup.findAll("span", {"id": re.compile('.*LabelIDAviso$')}))

    def __parse_message(self):
        """
        Percorre todos os items dos valores e "parsa-os"
        """
        self.__values = {}
        for k in self.__keys:
            self.__values[k] = self.__get_item_value(self.__keys[k])

    def __get_formatted_message(self):
        """
        Devolve uma mensagem formatada
        """
        message = "Aviso Local: {} de {} - Período de: {} a {}\n".format(
            self.__values['num_aviso'],
            self.__values['dt_promulgacao'],
            self.__values['dt_inicio'],
            self.__values['dt_fim']
        )

        message += "Promulgado por: {}\n".format(self.__values['ent_promulgacao'])
        message += "Local: {}\n".format(self.__values['local'])
        message += "Assunto: {}\n\n".format(self.__values['assunto'])
        message += self.__values['descricao']
        # message += self.__values['dt_cancelamento']

        return message

    def __get_item_value(self, name):
        """
        Devolve o conteudo de um item na pagina.
        O site parece ser feito com componentes do Visual Studio, é tudo "qqcoisaLabel", portanto é facil apanhar os
        valores. São todos "span" com id com algo do genero:
        ctl00_ContentPlaceHolder1_DataListAvisosLocais_ctl01_DESCPORTOLOCALLabel
                                                 index <- ^^ ^^ -> nome
        :param name: Nome do elemento a devolver
        :return: Conteúdo
        """
        f = self.__soup.find(
            "span",
            {"id": "ctl00_ContentPlaceHolder1_DataListAvisosLocais_ctl" + self.__current_index + "_" + name}
        )

        if f is None:
            return f

        # Se o string for None é porque existe mais do que uma string
        if f.string is None:
            out = ""
            # Concatena todas as strings com uma newline no fim
            for s in f.stripped_strings:
                out += s + "\n"
            return out.rstrip()
        else:
            return f.string


if __name__ == '__main__':
    # index = 1
    # if len(sys.argv) == 2:
    #    index = int(sys.argv[1])

    parser = AnavNet()

    for port in parser.get_ports():
        parser.set_port(port)

        print("{} - {}".format(port, parser.get_port_name()))
        print("Numero de mensagens: {}\n".format(parser.get_total_messages()))

        for index in range(1, parser.get_total_messages() + 1):
            print(parser.get_message(index))
            print("---")
