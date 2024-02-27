import re
import sys


def converter(htmlBody):
    # Headers
    htmlBody = re.sub(r'^#(\s.*)$', r'<h1>\1</h1>', htmlBody, flags=re.MULTILINE)
    htmlBody = re.sub(r'^##(\s.*)$', r'<h2>\1</h2>', htmlBody, flags=re.MULTILINE)
    htmlBody = re.sub(r'^###(\s.*)$', r'<h3>\1</h3>', htmlBody, flags=re.MULTILINE)

    htmlBody = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', htmlBody)

    htmlBody = re.sub(r'\*([^\*]*)\*', r'<i>\1</i>', htmlBody)

    htmlBody = re.sub(r'^\s*>\s*(.+)$', r'<blockquote>\1</blockquote>', htmlBody, flags=re.MULTILINE)

    htmlBody = re.sub(r'^\s*\d+\.\s+(.+)$', r'<li>\1</li>', htmlBody, flags=re.MULTILINE)
    htmlBody = re.sub(r'((<li>.*</li>\n)+)', r'<ol>\n\1</ol>\n', htmlBody, flags=re.MULTILINE)

    htmlBody = re.sub(r'^\s*-\s+(.+)$', r'<lo>\1</lo>', htmlBody, flags=re.MULTILINE)
    htmlBody = re.sub(r'((<lo>.*</lo>\n)+)', r'<ul>\n\1</ul>\n', htmlBody, flags=re.MULTILINE)
    htmlBody = re.sub(r'<lo>', r'<li>', htmlBody)
    htmlBody = re.sub(r'</lo>', r'</li>', htmlBody)

    htmlBody = re.sub(r'`(.*)`', r'<code>\1</code>', htmlBody)

    htmlBody = re.sub(r'^\s*---\s*$', r'<hr>', htmlBody, flags=re.MULTILINE)

    htmlBody = re.sub(r'!\[([^\]]*)\]\(([^\)]*)\)', r'<img src="\2" alt="\1"/>', htmlBody)

    htmlBody = re.sub(r'\[([^\]]*)\]\(([^\)]*)\)', r'<a href="\2">\1</a>', htmlBody)

    return htmlBody


def main(args):

    finalHTMLText = """<!DOCTYPE html>
<html lang="pt PT">
<head>
    <title>Pagina</title>
    <meta charset="utf-8">
</head>

<body>

"""

    with open(args[1]) as file:
        finalHTMLText += converter(file.read())

    finalHTMLText += "\n\n</body>"

    with open("outputFile.html", "w") as file:
        file.write(finalHTMLText)


if __name__ == "__main__":
    main(sys.argv)