import eel

eel.init('web')#Directory name
#It is best to always keep the UI code(html, javascript, css) in a separate directory in the same file

@eel.expose
def hello():
    print("Hello World")

eel.start('index.html')