# -*- coding: utf-8 -*-

"""
Requires Python 3.8 or later
"""

__author__ = "Jorge Morfinez Mojica (jorge.morfinez.m@gmail.com)"
__copyright__ = "Copyright 2021"
__license__ = ""
__history__ = """ """
__version__ = "1.21.F21.1 ($Rev: 1 $)"


from xml.dom import minidom
import os

# This is an example we need convert to XML and then write to an HTML and the rewrite to an XLS:

"""
<body style="height:100%">
		<table xmlns="">
		<tr>
			<td class="xl24" colspan="7" rowspan="2"><span class="font5">BANCO 0146</span></td>
		</tr>
	</table>
	<table>
		<tr xmlns="">
			<td class="xl27">
				<span class="font7">Account Location</span>
			</td>
			<td class="xl27">
				<span class="font7">Value date</span>
			</td>
			<td class="xl27">
				<span class="font7">Transaction narrative</span>
			</td>
			<td class="xl27">
				<span class="font7">Account currency</span>
			</td>
			<td class="xl27">
				<span class="font7">Transaction amount</span>
			</td>
			<td class="xl27">
				<span class="font7">Transaction time</span>
			</td>
			<td class="xl27">
				<span class="font7">Customer reference</span>
			</td>
		</tr>
		<tr xmlns="">
			<td class="xl28" rowspan="9">
				<span class="font8">MX</span>
			</td>
			<td class="xl24c">
				<span class="font8">23/04/2021</span>
			</td>
			<td class="xl28">
				<span class="font8">02000101010</span>
			</td>
			<td class="xl28">
				<span class="font8">MXN</span>
			</td>
			<td class="xl02">
				<span class="font8">                 21,500.00</span>
			</td>
			<td class="xl28">
				<span class="font8">14.19</span>
			</td>
			<td class="xl28">
				<span class="font8">ABONO 0100</span>
			</td>
		</tr>
		<tr xmlns="">
			<td class="xl24c">
				<span class="font8">23/04/2021</span>
			</td>
			<td class="xl28">
				<span class="font8">04000108599</span>
			</td>
			<td class="xl28">
				<span class="font8">MXN</span>
			</td>
			<td class="xl02">
				<span class="font8">                 12,000.00</span>
			</td>
			<td class="xl28">
				<span class="font8">14.21</span>
			</td>
			<td class="xl28">
				<span class="font8">ABONO 0100</span>
			</td>
		</tr>
	</table>
</body>
"""

'''
root = minidom.Document()

xml = root.createElement('root')
root.appendChild(xml)

productChild = root.createElement('product')
productChild.setAttribute('name', 'Geeks for Geeks')

xml.appendChild(productChild)
'''

root = minidom.Document()

xml_body = root.createElement('body')
xml_body.setAttribute('style', 'height:100%')

root.appendChild(xml_body)

table_child1 = root.createElement('table')
table_child1.setAttribute('xmlns', '')

tr_table1 = table_child1.createElement('tr')

td_table1 = tr_table1.createElement('td')
td_table1.setAttribute('class', 'xl24')
td_table1.setAttribute('colspan', '7')
td_table1.setAttribute('rowspan', '2')

span_table1 = td_table1.createElement('span')
span_table1.setAttribute('class', 'font5')
span_table1.text = 'BANCO XXXX'

td_table1.appendChild(span_table1)

tr_table1.appendChild(td_table1)

table_child1.appendChild(tr_table1)

xml_body.appendChild(table_child1)

xml_str = root.toprettyxml(indent="\t")

print(f'XML Str: {xml_str}')

save_path_file = "file_bank.xml"

with open(save_path_file, "w") as f:
    f.write(xml_str)