# py-jsonl
Simple helper package to read and write jsonl formatted files

## Reading
Read jsonl file line by line as a python dictionary
```python
from jsonl import read_jsonl

with open('file_to_read.jsonl') as fh:
    for jsonl in read_jsonl(fh):
        #do stuff
```

## Writing
Write jsonl file using python dictionaries
```python
from jsonl import write_jsonl

d = {"key": "value"}

with open('file_to_write.jsonl', 'w') as fh:
    write_jsonl(d, fh)

```