CHILD = "Sara"
TEMPLATE = "mathe_template.html"
PROBLEMS = "problems_sara.json"

import json
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

# Lade die JSON-Datei
with open(PROBLEMS, "r") as f:
    problems_data = json.load(f)

# Lade die Jinja2 Vorlage
env = Environment(loader=FileSystemLoader("."))
template = env.get_template(TEMPLATE)

# Rendere die Vorlage mit den JSON-Daten
rendered_html = template.render(problems=problems_data)

# Erhalte das aktuelle Datum und die Uhrzeit
now = datetime.now()

# Erstelle einen Zeitstempel im Format "YYYY-MM-DD"
timestamp = now.strftime("%Y-%m-%d")

# Speichere das gerenderte HTML in einer neuen Datei mit Zeitstempel
output_filename = f"{timestamp}_{CHILD}_aufgaben.html"
with open(output_filename, "w") as f:
    f.write(rendered_html)
