# Semantic QA

A simple QA search engine built using elasticsearch and universal sentence encoder

<br>

### Pre-requisites

* Elasticsearch [7.0+]


<br>

### Installing dependencies

```
pip install -r requirements.txt
```

<br>

### Indexing the dataset

```
python dump_qa.py
```

<br>

### Running the server

```
python app.py
```

<br>

### Querying the index

```
http://localhost:5000/query?query=""
```