#!/usr/bin/python3
"""
This file creates a route on the object app_views
that returns a JSON status.
"""


import json
from api.v1.views import app_views
from flask import Response


@app_views.route('/status', methods=['GET'])
def status():
    """A method that returns a JSON status"""
    response = json.dumps({"status": "OK"}, indent=2) + "\n"
    return Response(response, mimetype='application/json')
