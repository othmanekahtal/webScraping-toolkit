# save HTML locally :
# -----------------------------------------------------
# After we make a request and retrieve a web page's content,
# we can store that content locally with Python's open() function.
# To do so we need to use the argument wb, which stands for "write bytes".
# This let's us avoid any encoding issues when saving.
# -----------------------------------------------------
def save_html(html, filename, path='content/'):
    with open(path + filename+'.html', 'w') as f:
        f.write(html)


# open/read HTML from a local file
# To retrieve our saved file we'll make another function to wrap reading the HTML back into html.
# We need to use rb for "read bytes" in this case.
def open_html(path):
    with open(path, 'rb') as f:
        return f.read()
