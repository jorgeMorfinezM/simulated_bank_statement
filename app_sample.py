# -*- coding: utf-8 -*-

"""
Requires Python 3.8 or later
"""

__author__ = "Jorge Morfinez Mojica (jorge.morfinez.m@gmail.com)"
__copyright__ = "Copyright 2021. All Rights Reserved."
__license__ = ""
__history__ = """ This script creates an xls file (Excel) from the construction of an HTML in XML format with random 
                  data to specific columns. """
__version__ = "1.21.G15.1 ($Rev: 100 $)"


import os
import base64
import pandas
import argparse
import xlsxwriter
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
import xlrd
from xlrd import open_workbook, open_workbook_xls
from io import StringIO, BytesIO
from lxml import etree
from xml.sax.saxutils import unescape
import xml.etree.cElementTree as ET
from datetime import timedelta, datetime
from DataFillClass import DataFillClass

STYLE_CONTENT = "<!--\n" \
                    "     table\n" \
                    "{mso - displayed - decimal - separator: \"\.\";\n" \
                    "mso - displayed - thousand - separator: \"\,\";}\n" \
                    "@page\n" \
                    "{margin: 1.0 in .75 in 1.0 in .75 in;\n" \
                    "mso - header - margin: .5 in;\n" \
                    "mso - footer - margin: .5 in;}\n" \
                    "tr\n" \
                    "{mso - height - source: auto;}\n" \
                    "col\n" \
                    "{mso - width - source: auto;}\n" \
                    "br\n" \
                    "{mso - data - placement: same - cell;}\n" \
                    ".style0\n" \
                    "{mso - number - format: General;\n" \
                    "text - align: general;\n" \
                    "vertical - align: bottom;\n" \
                    "white - space: nowrap;\n" \
                    "mso - rotate: 0;\n" \
                    "mso - background - source: auto;\n" \
                    "mso - pattern: auto;\n" \
                    "color: windowtext;\n" \
                    "font - size: 10.0\n" \
                    "pt;\n" \
                    "font - weight: 400;\n" \
                    "font - style: normal;\n" \
                    "text - decoration: none;\n" \
                    "font - family: Arial;\n" \
                    "mso - generic - font - family: auto;\n" \
                    "mso - font - charset: 0;\n" \
                    "border: none;\n" \
                    "mso - protection: locked\n" \
                    "visible;\n" \
                    "mso - style - name: Normal;\n" \
                    "mso - style - id: 0;}\n" \
                    "td\n" \
                    "{mso - style - parent: style0;\n" \
                    "padding - top: 1\n" \
                    "px;\n" \
                    "padding - right: 1\n" \
                    "px;\n" \
                    "padding - left: 1\n" \
                    "px;\n" \
                    "mso - ignore: padding;\n" \
                    "color: windowtext;\n" \
                    "font - size: 10.0\n" \
                    "pt;\n" \
                    "font - weight: 400;\n" \
                    "font - style: normal;\n" \
                    "text - decoration: none;\n" \
                    "font - family: Arial;\n" \
                    "mso - generic - font - family: auto;\n" \
                    "mso - font - charset: 0;\n" \
                    "mso - number - format: General;\n" \
                    "text - align: general;\n" \
                    "vertical - align: bottom;\n" \
                    "border: none;\n" \
                    "mso - background - source: auto;\n" \
                    "mso - pattern: auto;\n" \
                    "mso - protection: locked\n" \
                    "visible;\n" \
                    "white - space: nowrap;\n" \
                    "mso - rotate: 0;}\n" \
                    ".font5\n" \
                    "{font - size: 16.0pt;\n" \
                    "font - weight: 700;\n" \
                    "font - family: Arial\n" \
                    "Unicode\n" \
                    "MS\, Andale\n" \
                    "WT\, Tahoma\, Arial\, MS\n" \
                    "UI\n" \
                    "Gothic\, Gulim\, SimSun\, PMingLiU\, Raghu8\, sans - serif;\n" \
                    "}\n" \
                    ".font6\n" \
                    "{font - size: 10.0pt;\n" \
                    "font - family: Arial\n" \
                    "Unicode\n" \
                    "MS\, Andale\n" \
                    "WT\, Tahoma\, Arial\, MS\n" \
                    "UI\n" \
                    "Gothic\, Gulim\, SimSun\, PMingLiU\, Raghu8\, sans - serif;\n" \
                    "}\n" \
                    ".font8\n" \
                    "{font - size: 8.0pt;\n" \
                    "font - family: Arial\n" \
                    "Unicode\n" \
                    "MS\, Andale\n" \
                    "WT\, Tahoma\, Arial\, MS\n" \
                    "UI\n" \
                    "Gothic\, Gulim\, SimSun\, PMingLiU\, Raghu8\, sans - serif;\n" \
                    "}\n" \
                    ".font7\n" \
                    "{font - size: 8.0pt;\n" \
                    "font - weight: 700;\n" \
                    "font - family: Arial\n" \
                    "Unicode\n" \
                    "MS\, Andale\n" \
                    "WT\, Tahoma\, Arial\, MS\n" \
                    "UI\n" \
                    "Gothic\, Gulim\, SimSun\, PMingLiU\, Raghu8\, sans - serif;\n" \
                    "}\n" \
                    ".font9\n" \
                    "{color:  # 999999;\n" \
                    "     font - size: 8.0\n" \
                    "pt;\n" \
                    "font - family: Arial\n" \
                    "Unicode\n" \
                    "MS\, Andale\n" \
                    "WT\, Tahoma\, Arial\, MS\n" \
                    "UI\n" \
                    "Gothic\, Gulim\, SimSun\, PMingLiU\, Raghu8\, sans - serif;\n" \
                    "}\n" \
                    ".font10\n" \
                    "{color:  # FF0000;\n" \
                    "     font - size: 10.0\n" \
                    "pt;\n" \
                    "font - family: Arial\n" \
                    "Unicode\n" \
                    "MS\, Andale\n" \
                    "WT\, Tahoma\, Arial\, MS\n" \
                    "UI\n" \
                    "Gothic\, Gulim\, SimSun\, PMingLiU\, Raghu8\, sans - serif;\n" \
                    "}\n" \
                    ".font11\n" \
                    "{font - size: 12.0pt;\n" \
                    "font - weight: 700;\n" \
                    "font - family: Arial\n" \
                    "Unicode\n" \
                    "MS\, Andale\n" \
                    "WT\, Tahoma\, Arial\, MS\n" \
                    "UI\n" \
                    "Gothic\, Gulim\, SimSun\, PMingLiU\, Raghu8\, sans - serif;\n" \
                    "}\n" \
                    ".xl31\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\@\";\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl10\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\#\,\#\#0\";\n" \
                    "text - align: right;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl12\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\#\,\#\#0\.00\";\n" \
                    "text - align: right;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl13\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\#\,\#\#0\.000\";\n" \
                    "text - align: right;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl17\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\#\,\#\#0\.0000000\";\n" \
                    "text - align: right;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl18\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\#\,\#\#0\.00000000\";\n" \
                    "text - align: right;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl25\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\@\";\n" \
                    "}\n" \
                    ".xl28\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\@\";\n" \
                    "vertical - align: top;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl28b\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"General\";\n" \
                    "vertical - align: top;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl24\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\@\";\n" \
                    "vertical - align: top;\n" \
                    "}\n" \
                    ".xl00\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\#\,\#\#0\";\n" \
                    "text - align: right;\n" \
                    "vertical - align: top;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl02\n" \
                    "{mso - style - parent: style0\n;" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\#\,\#\#0\.00\";\n" \
                    "text - align: right;\n" \
                    "vertical - align: top;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl03\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\#\,\#\#0\.000\";\n" \
                    "text - align: right;\n" \
                    "vertical - align: top;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl07\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\#\,\#\#0\.0000000\";\n" \
                    "text - align: right;\n" \
                    "vertical - align: top;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl08\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\#\,\#\#0\.00000000\";\n" \
                    "text - align: right;\n" \
                    "vertical - align: top;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl29\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\@\";\n" \
                    "text - align: right;\n" \
                    "vertical - align: top;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl27\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\@\";\n" \
                    "text - align: left;\n" \
                    "vertical - align: top;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "background:  # E3E3FC;\n" \
                    "mso - pattern:auto\n" \
                    "none;\n" \
                    "}\n" \
                    ".xl32\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\@\";\n" \
                    "text - align: right;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl24c\n" \
                    "{\n" \
                    "    mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"Short Date\";\n" \
                    "text - align: right;\n" \
                    "vertical - align: top;\n" \
                    "border - left: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - top: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - right: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "border - bottom: 0.8\n" \
                    "pt\n" \
                    "solid  # CCCCCC;\n" \
                    "}\n" \
                    ".xl26\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "mso - number - format: \"\@\";\n" \
                    "text - align: right;\n" \
                    "}\n" \
                    ".xl28a\n" \
                    "{mso - style - parent: style0;\n" \
                    "white - space: normal;\n" \
                    "vertical - align: top;}\n" \
                    "-->"


def create_xml_head():
    html = ET.Element("html")

    html.set("xmlns:ss", "urn:schemas-microsoft-com:office:spreadsheet")
    html.set("xmlns:x", "urn:schemas-microsoft-com:office:excel")
    html.set("xmlns:o", "urn:schemas-microsoft-com:office:office")
    html.set("xmlns:v", "urn:schemas-microsoft-com:vml")

    head_node = ET.SubElement(html, "head")

    meta_node1 = ET.SubElement(head_node, "meta")
    meta_node1.set("content", "text/html; charset=utf-8")
    meta_node1.set("http-equiv", "Content-Type")

    meta_node2 = ET.SubElement(head_node, "meta")
    meta_node2.set("content", "Excel.Sheet")
    meta_node2.set("name", "ProgId")

    meta_node3 = ET.SubElement(head_node, "meta")
    meta_node3.set("content", "Microsoft Excel 9")
    meta_node3.set("name", "Generator")

    style_node = ET.SubElement(head_node, "style")
    # style_node.text = unescape(STYLE_CONTENT.replace("&lt;", "<").replace("&gt;", ">"))
    style_node.text = unescape(STYLE_CONTENT)

    return html


def create_xml_head_nodes(html_node):

    body_node = ET.SubElement(html_node, "body")

    body_node.set("style", "height:100%")

    table = ET.SubElement(body_node, "table")

    table.set("xmlns", "")

    tr_table = ET.SubElement(table, "tr")

    td_table = ET.SubElement(tr_table, "td")

    td_table.set("colspan", "7")
    td_table.set("rowspan", "2")
    td_table.set("class", "xl24")

    span_td = ET.SubElement(td_table, "span")

    span_td.text = "BANCO XXXX"

    span_td.set("class", "font5")

    return body_node


def create_data_headers_nodes(body_element):

    list_headers = ['Pais', 'Fecha', 'Referencia', 'Moneda', 'Monto',
                    'Hora', 'Transaccion']

    # body = create_xml_head_nodes()

    table_content = ET.SubElement(body_element, "table")

    tr_table_content = ET.SubElement(table_content, "tr")
    tr_table_content.set("xmlns", "")

    # HEADERS del XLS
    for i in range(0, len(list_headers)):
        td_table_content = ET.SubElement(tr_table_content, "td")

        td_table_content.set("class", "xl27")

        span_td_content = ET.SubElement(td_table_content, "span")

        span_td_content.text = list_headers[i]

        span_td_content.set("class", "font7")

    return table_content


def generate_data_nodes(data_qty_xml, table_content_elem):
    # DATA on XLS:

    # HEADERS del XLS
    for i in range(0, data_qty_xml):

        list_data = create_data_list()

        tr_table_data = ET.SubElement(table_content_elem, "tr")

        tr_table_data.set("xmlns", "")

        # if i == 0:
        #
        #     td_mx_node = ET.SubElement(tr_table_data, "td")
        #     td_mx_node.set("class", "xl28")
        #     td_mx_node.set("rowspan", "9")
        #
        #     span_td_mx = ET.SubElement(td_mx_node, "span")
        #     span_td_mx.set("class", "font8")
        #     span_td_mx.text = "MX"

        for j in range(0, len(list_data)):

            td_table_data = ET.SubElement(tr_table_data, "td")

            # if i == 0 and j == 0:
            #     td_table_data.set("rowspan", "9")

            if j == 0:
                td_table_data.set("class", "xl24c")
            elif j == 3:
                td_table_data.set("class", "xl02")
            else:
                td_table_data.set("class", "xl28")

            span_td_content = ET.SubElement(td_table_data, "span")

            span_td_content.text = list_data[j]

            span_td_content.set("class", "font8")


def create_data_list():
    data_list = []

    data_fill = DataFillClass()

    today = datetime.now()

    # Columna Account Location:
    fixed_list_data = ['MX']

    account_location_row = data_fill.fill_string_fixed_data(fixed_list_data, '')

    data_list.append(account_location_row)

    # Columna Value date:
    value_date_column = data_fill.fill_date_data('', datetime(2021, 6, 1), today)

    data_list.append(value_date_column)

    # Columna Transaction narrative:
    transaction_narrative_row = data_fill.fill_string_digits_data(11, '', '')

    data_list.append(transaction_narrative_row)

    # Columna Account currency:
    fixed_list_data = ['MXN']

    account_currency_row = data_fill.fill_string_fixed_data(fixed_list_data, '')

    data_list.append(account_currency_row)

    # Columna Transaction amount:
    transaction_amount_row = data_fill.fill_amount_integer_data('', "{:,.2f}")

    data_list.append(transaction_amount_row)

    # Columna Transaction time:
    transaction_time_row = data_fill.fill_time_formated_data('', datetime(2021, 6, 1), today)

    data_list.append(transaction_time_row)

    # Columna Customer reference:
    fixed_list_data = ['ABONO XXXX']

    customer_reference_row = data_fill.fill_string_fixed_data(fixed_list_data, '')

    data_list.append(customer_reference_row)

    return data_list


def overwrite_data(xls_file_name, data_qty_ow):

    os.rename(xls_file_name, r'html_xls_file.xml')

    mytree = ET.parse('html_xls_file.xml')
    myroot = mytree.getroot()

    result_xml = etree.tostring(mytree.getroot(), pretty_print=True, method="xml")

    print(f'\netree.tostring overwrite: {result_xml}\n')

    root = ET.fromstring(result_xml)

    # Top-level elements
    # print(f'\nTop-level elements: {root.findall(".")}')  # SI VA

    # myroot.find('.//table/..[@xmlns=""]', namespaces={"xmlns": ""})
    table_data_node = myroot.find('.//body/table[1]/')

    tr_nodes_all = root.findall(".//table[1]/tr/td")  # SI VA

    print(f'td All data nodes: {tr_nodes_all}\n')
    print(f'table All data nodes: {table_data_node}\n')

    # td_nodes_all = root.findall(".//table[1]/tr/td/table/")
    # td_nodes_all = root.findall('.//table[1]/tr/..[@xmlns=""]')

    # for td_nodes in root.iter('tr'):
    #     for child in td_nodes.getchildren():
    #         for node_span in child.iterfind('span'):
    #
    #             # print(node_span.tag, node_span.text, node_span.attrib)
    #             print(node_span.findtext('span'))

    num_tr_data = 0

    for td_nodes in root.iter('tr'):
        for child in td_nodes.iterfind('td'):

            if 'class' in child.keys():
                if 'xl27' not in child.attrib.get('class'):

                    if 'colspan' not in child.keys():
                        print(f"Child: {child.keys()}")
                        print(f"Attrib to child: {child.attrib}")
                        print(f"Tag to child: {child.tag}")

                        print(f"\ntext in span TD child: {child.findtext('span')}\n")

                        num_tr_data += 1

    generate_data_nodes(data_qty_ow, table_data_node)


def parse_xml(xml_file, df_cols):
    """Parse the input XML file and store the result in a pandas
    DataFrame with the given columns.

    The first element of df_cols is supposed to be the identifier
    variable, which is an attribute of each node element in the
    XML data; other features will be parsed from the text content
    of each sub-element.
    """

    xtree = ET.parse(xml_file)
    xroot = xtree.getroot()
    rows = []
    # rows = create_data_list()

    for i in range(0, 5):

        data_rows = create_data_list()

        # for node in xroot:
            # res = []
            #
            # res.append(node.attrib.get(df_cols[0]))

            # for el in df_cols[1:]:
            #     if node is not None and node.find(el) is not None:
            #         res.append(node.find(el).text)
            #     else:
            #         res.append(None)

        rows.append({df_cols[i]: data_rows[i]
                     for i, _ in enumerate(df_cols)})

    # out_df = pandas.DataFrame(rows, columns=df_cols)
    out_df = pandas.DataFrame(rows)

    return out_df


def generate_file_xml_format(data_qty_rows):
    """
    Create/Format XML-HTML-XLS file with random data and quantity rows.

    :param data_qty_rows:
    :return: xml_str
    """
    # Create/Format the HTML-XML-XLS Header
    html_root_node = create_xml_head()

    # Set Namespace on header
    html_root_node.set("xmlns", "http://www.w3.org/TR/REC-html40")

    # Create/Format Body node
    body = create_xml_head_nodes(html_root_node)

    # Format/Create nodes to HTML-XML-XLS file
    table_node_head = create_data_headers_nodes(body)

    # Call random data functions to write on nodes
    generate_data_nodes(data_qty_rows, table_node_head)

    # Create XML format file
    # xml_str = ET.tostring(body, 'utf-8')
    xml_str = ET.tostring(html_root_node, 'utf-8')  # SI VA

    return xml_str


def create_xls_file_formatting(xls_string, xml_file_name, xls_file_name):
    print(f'XML Str: {xls_string}')

    # To format XML:
    xml_parser = etree.XMLParser(recover=True)  # recover from bad characters.

    # parser = etree.HTMLParser(recover=True)

    tree = etree.parse(BytesIO(xls_string), xml_parser)

    # Creating tostring xml
    result = etree.tostring(tree.getroot(), pretty_print=True, method="html")

    print(f'result etree.tostring original: {result}')

    # xml_2_save = xml_str
    xml_2_save = result

    # Writing xml file
    with open(xml_file_name, "wb") as file_last:
        file_last.write(xml_2_save)

    file_last.close()

    # Rename XML file to XLS file
    os.rename(xml_file_name, xls_file_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--data_quantity_rows', type=int, required=True,
                        help="Number of rows on the file of simulated data")

    args = parser.parse_args()

    data_quantity = int(args.data_quantity_rows)

    # Generate XML nodes with data
    xml_str = generate_file_xml_format(data_quantity)

    xml_filename = "html_xls_file.xml"

    xls_filename = "simulated_bank_statement.xls"

    # Create XLS file from XML with random data
    create_xls_file_formatting(xml_str, xml_filename, xls_filename)

    # Another method to overwriting/adding more data - DO NOT FINISHED!
    # data_qty_rewrite = 5
    #
    # overwrite_data(xls_filename, data_qty_rewrite)  # OTRO METODO DE SOBREESCRIBIR
