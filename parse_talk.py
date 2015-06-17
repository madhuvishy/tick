import mwparserfromhell
import mwclient
import csv

PARAMS = ['contact', 'project', 'status', 'purge']

site = mwclient.Site('meta.wikimedia.org')

def read_schemas_list(schemas_list_file):
    with open(schemas_list_file, 'r') as f:
        schemas_list = f.read().split('\n')
    return schemas_list

def parse_schemadoc_template(schema_name):
    try:
        talk_page_name = 'Schema_talk:' + schema_name
        talk_page = site.Pages[talk_page_name]
        text = talk_page.text()
        parsed_text = mwparserfromhell.parse(text)
        templates = parsed_text.filter_templates()
        if len(templates) > 0: #and templates[0].name == 'SchemaDoc':
            return templates[0]
        else:
            return None
    except Exception, e:
        print schema_name, e

def get_templates_data(schemas_list):
    all_template_data = []
    for schema in schemas_list:
        template = parse_schemadoc_template(schema)
        template_data = [unicode(schema, errors='ignore')]
        if template and template.params:
            for p in PARAMS:
                try:
                    val = unicode(str(template.get(p).value), errors='ignore')
                    template_data.append(val)
                except Exception, e:
                    pass    
        all_template_data.append(template_data)
    return all_template_data

def write_csv(templates_data):
    print len(templates_data)
    with open('template_data.csv', 'wb') as f:
        writer = csv.writer(f)
        for row in templates_data:
            writer.writerow(row)

schemas_list = read_schemas_list('schemas.txt')
templates_data = get_templates_data(schemas_list)
write_csv(templates_data)