# tick
Parse Eventlogging schema talk pages

Install dependencies
```
pip install -r requirements.txt
```

Uses MW Api + mwparserfromhell to parse EL schema talk pages, from the schema list in `schemas.txt`,
find params matching SchemaDoc (https://meta.wikimedia.org/wiki/Template:SchemaDoc) template, 
and store all the data in a csv file.
