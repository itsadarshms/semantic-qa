# Semantic QA

A simple QA search engine built using elasticsearch and universal sentence encoder

<br>

#### Pre-requisites

* Elasticsearch [7.0+]


#### Installing dependencies

```
pip install -r requirements.txt
```

#### Indexing the dataset

```
python dump_qa.py
```

#### Running the server

```
python app.py
```

#### Querying the index

```
http://localhost:5000/query?query=""
```