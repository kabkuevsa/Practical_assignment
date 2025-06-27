import argparse
import sys
from validators import get_field_type
from db import FormTemplateDB

def main():
    parser = argparse.ArgumentParser(description="Поиск шаблона формы по полям")
    parser.add_argument("command", choices=["get_tpl"], help="Команда для поиска шаблона")
    args, unknown = parser.parse_known_args()

    fields = {}
    for arg in unknown:
        if arg.startswith("--"):
            key_value = arg[2:].split("=", maxsplit=1)
            if len(key_value) == 2:
                field_name, field_value = key_value
                fields[field_name] = get_field_type(field_value)

    db = FormTemplateDB()
    template_name = db.find_template(fields)

    if template_name:
        print(template_name)
    else:
        print({field: type_.capitalize() for field, type_ in fields.items()})

if __name__ == "__main__":
    main()