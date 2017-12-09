#!/usr/bin/python

import tika
from mmda.models import File
from tika import parser

projectpath = request.form['filename']

parsed = parser.from_file(projectpath, xmlContent=True)
f = open('metadata.txt','w')
f.write(parsed["metadata"])
f.close()