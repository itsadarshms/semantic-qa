from flask import Flask, request
from flask_cors import CORS
import tensorflow_hub as hub
import numpy as np

from elastic import connect_elastic, semantic_search, keyword_search


# Define the app
app = Flask(__name__)
# Load configs
app.config.from_object('config')
# Set CORS policies
CORS(app)

# Load the universal-sentence-encoder
model = hub.load(app.config['MODEL_URL'])
# Connect to es node
connect_elastic(app.config['ELASTIC_IP'], app.config['ELASTIC_PORT'])


@app.route("/query", methods=["GET"])
def qa():
    # API to return top_n matched records for a given query
    if request.args.get("query"):
        # Generate embeddings for the input query
        query_vec = np.asarray(model([request.args.get("query")])[0]).tolist()
        # Retrieve the semantically similar records for the query
        records = semantic_search(query_vec, app.config['SEARCH_THRESH'])

        # Retrieve records using keyword search (TF-IDF score)
        # records = keyword_search(request.args.get("query"), app.config['SEARCH_THRESH'])
    else:
        return {"error": "Couldn't process your request"}, 422
    return {"data": records}


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
