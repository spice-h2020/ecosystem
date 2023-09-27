import pysparql_anything as pysa
import os
import shutil

engine = pysa.SparqlAnything()
directory = './content/'
for root, dirs, files in os.walk(directory):
    for filename in files:
        location = os.path.join(root, filename)
        print(location)
        pre, ext = os.path.splitext(location)
        #pre = pre.replace("./content/", "./rdf/")
        output = pre + ".schema.json"
        pth = os.path.dirname(os.path.abspath(output))
        if not os.path.exists(pth):
            os.makedirs(pth)
        engine.run(q='./components-to-rdf.sparql', v={'componentFile': location}, o=output) #
