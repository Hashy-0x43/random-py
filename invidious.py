import webbrowser

search_engine = "https://invidious.fdn.fr/watch?v="

query = str(input("YouTube Video ID : "))

webbrowser.open(search_engine + query)
