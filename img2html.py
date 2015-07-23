import os

html="""<div class="col s4">
    <img class="thumb materialboxed" src="%s"/>
</div>
""".strip()

for dirname, dirnames, filenames in os.walk('images'):
    for fn in filenames:
        print html % ("/"+os.path.join(dirname, fn))
