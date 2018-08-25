from csv import DictReader
import re


html = "<ul class=pub-list>\n"
with open("../resources/publications.csv") as fin:
    rows = sorted(DictReader(fin), key=lambda d: int(d['Year']) if d['Year'] else 0, reverse=True)
    for row in rows:
        html += "  <li>\n    <p>\n"
        html += "      <tt class=pub-title>{}</tt>.&nbsp".format(row['Title'])

        html += "<tt>{}<tt>".format(re.sub("(Pugh, Robert ?A?)",
                                   r"<b>\1</b>",
                                   row['Authors']))
        if row['Publication']:
            html += "<tt>{}</tt>.&nbsp".format(row['Publication'])

        if row['Year']:
            html += "<tt>{}</tt>.&nbsp".format(row['Year'])

        if row['Link']:
            html += "<a href=\"{}\">[Link]</a>".format(row['Link'])
        html += "    </p>\n  </li>\n"
html += "</ul>"

print(html)
