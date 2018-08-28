#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        37: u"Angra do Heroismo",
        10: u"Aveiro",
        1: u"Caminha",
        14: u"Cascais",
        8: u"Douro",
        27: u"Faro",
        11: u"Figueira da Foz",
        32: u"Funchal",
        40: u"Horta",
        23: u"Lagos",
        7: u"Leixões",
        16: u"Lisboa",
        12: u"Nazaré",
        29: u"Olhão",
        44: u"Peniche",
        34: u"Ponta Delgada",
        25: u"Portimão",
        33: u"Porto Santo",
        5: u"Povoa de Varzim",
        36: u"Praia da Vitória",
        43: u"Santa Cruz das Flores",
        20: u"Setúbal",
        22: u"Sines",
        45: u"Tavira",
        3: u"Viana do Castelo",
        30: u"Vila Real de Santo António",
        6: u"Vila do Conde",
        35: u"Vila do Porto",
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

    def get_message(self, index):
        if self.__current_port is None:
            raise RuntimeError("Run set_port() first")

        self.__current_index = "{:0>2d}".format(index)  # Add a zero to the left

        if index > self.__current_total or index < 1:
            raise IndexError("Invalid index")
        else:
            self.__parse_message()
            return self.__values

    def get_total_messages(self):
        if self.__current_port is None:
            raise RuntimeError("Run set_port() first")
        return self.__current_total

    def __count_total(self):
        self.__current_total = len(self.__soup.findAll("span", {"id": re.compile('.*LabelIDAviso$')}))

    def __parse_message(self):
        self.__values = {}
        for k in self.__keys:
            self.__values[k] = self.__get_item_value(self.__keys[k])

    def __get_item_value(self, name):
        f = self.__soup.find(
            "span",
            {"id": "ctl00_ContentPlaceHolder1_DataListAvisosLocais_ctl" + self.__current_index + "_" + name}
        )

        if f is None:
            return f

        if f.string is None:
            out = ""
            for s in f.stripped_strings:
                out += s + "\n"
            return out.rstrip()
        else:
            return f.string
