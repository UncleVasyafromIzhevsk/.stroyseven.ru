import markdown


with open('ty.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text)


with open('checklist.html', 'w') as f:
    f.write(html)
