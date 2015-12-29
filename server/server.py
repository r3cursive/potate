#!/usr/bin/env python

from flask import Flask, request
from datetime import datetime
app = Flask(__name__)

@app.route('/sitrep', methods=['POST'])
def getClientInfo():
    uuid = request.form['uuid']
    hostname = request.form['hostname']
    internalIP = request.form['InternalIP']
    externalIP = request.headers.getlist("X-Forwarded-For")[0]
    lastCheckin = str(datetime.now())
    return


def serveClient():
    """
    Returns client for download
    :return: provides client
    """
    return


