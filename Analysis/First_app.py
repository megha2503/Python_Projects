import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Couse Reviews", classes="text-h3 text-right q-pa-md")
    p1 = jp.QDiv(a=wp, text="Graphs represents the course review analysis")
    
    return wp

jp.justpy(app)