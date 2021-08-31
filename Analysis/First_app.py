import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Students interest in the field of DataScience", classes="text-h3 text-right q-pa-md")
    p1 = jp.QDiv(a=wp, text="Graphs represents the statistics on Python and ML knowledge", classes="text-center")
    
    return wp

jp.justpy(app)