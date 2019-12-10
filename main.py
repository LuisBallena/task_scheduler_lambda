import json
import os

from lxml import etree as et


def main_handler(event, context):
    print('## ENVIRONMENT VARIABLES')
    print(os.environ)
    print('## EVENT')
    print(event)
    root = et.Element('html', version="5.0")
    et.SubElement(root, 'head')
    et.SubElement(root, 'title', bgcolor="red", fontsize='22')
    et.SubElement(root, 'body', fontsize="15")
    return {
        'statusCode': 200,
        'body': json.dumps(et.tostring(root, pretty_print=True).decode("utf-8"))
    }
