import tensorflow_hub as hub
import numpy as np
from tqdm import tqdm
import pandas as pd

from elastic import connect_elastic, insert_qa
import config


def process_qa():
    df = pd.read_csv("data/COVID-QA.csv")
    df.dropna(inplace=True, subset=["Answers", "Question"])

    print("\nIndexing QA's...")
    for _, row in tqdm(df.iterrows()):
        # Index each qa pair along with the question id and embedding
        insert_qa({
            'question': row['Question'],
            'answer': row['Answers'],
            'question_vec': np.asarray(model([row['Question']])[0]).tolist(),
            'q_id': row['Question ID']
        })


if __name__ == '__main__':
    # Load the universal-sentence-encoder model
    model = hub.load(config.MODEL_URL)
    print("Model loaded successfully...")
    # Connect to elasticsearch node
    connect_elastic(config.ELASTIC_IP, config.ELASTIC_PORT)
    # Index the dataset
    process_qa()
