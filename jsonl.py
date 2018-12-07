#!/usr/bin/python
import json


def write_jsonl(obj, outfile):
    """
    Writes new line delimited json object
    :param obj: object to jsonify
    :param outfile: file to write to
    :return: None
    """
    json_string = json.dumps(obj)
    outfile.write(json_string+'\n')


def parse_jsonl(infile):
    """
    Parses a new line delimited file containing json objects
    :param infile: file handler
    :return: json line generator
    """
    for line in infile:
        json_line = json.loads(line)
        yield json_line
