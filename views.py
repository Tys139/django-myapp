from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import pyarrow
import pandas as pd
import base64
import pyarrow as pa

def serialize_table(table):
    sink = pa.BufferOutputStream()
    print(table.schema)
    writer = pa.RecordBatchStreamWriter (sink, table.schema)
    writer.write_table(table)
    writer.close()
    buf = sink.getvalue()
    print(sink.getvalue())
    return sink.getvalue()



def index(request):
    n_legs = pa.array([2, 4, 5, 100])
    animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
    names = ["n_legs", "animals"]
    test= pa.Table.from_arrays([n_legs, animals], names=names)


    bytes = serialize_table(test)


    arrowdata = list(bytes )
    print(arrowdata)
    # with open('C:\\Users\\tatha\\PycharmProjects\\django-webpack\\myapp\\myapp\\app1\\chicago-crimes-2017.arrow', "rb") as arrowdata:
    #     arrowdata = arrowdata.read()
    # arrowdata =list(arrowdata)
    # print(arrowdata)


    injectme ={'bytes': arrowdata}
    return render(request,'test.html',context=injectme)