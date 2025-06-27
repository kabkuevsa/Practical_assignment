from tinydb import TinyDB, Query

class FormTemplateDB:
    def __init__(self, db_path='templates.json'):
        self.db = TinyDB(db_path)
    
    def add_template(self, template):
        if 'name' not in template:
            raise ValueError("Template must have a 'name' field")
        self.db.insert(template)
    
    def find_template(self, fields):
        Form = Query()
        for template in self.db.all():
            template_fields = {k: v for k, v in template.items() if k != 'name'}
            if all(field in fields and fields[field] == field_type 
                   for field, field_type in template_fields.items()):
                return template['name']
        return None