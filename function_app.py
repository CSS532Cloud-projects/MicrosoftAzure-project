import azure.functions as func
import logging
import csv
import codecs
import json

app = func.FunctionApp()

@app.function_name(name="BlobTriggerV2")
@app.blob_trigger(arg_name="myblob", path="myPath",
                               connection="myConnection") 
def BlobTriggerV2(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")

    blob_contents = myblob.read()
    logging.info(blob_contents.decode('utf-8'))