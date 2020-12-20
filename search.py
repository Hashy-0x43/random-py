import webbrowser as w

engines = [
    "Google",
    "DuckDuckGo",
    "DuckDuckGo Lite",
    "Brainly",
    "Startpage",
    "Pinterest",
    "USATodayEducate",
    "TheWashingtonPost",
    "YouTube",
    "RateMyProfessor",
    "Yacy",
    "Invidious",
    "CNN"
]

start_num = 0
engine_quantity = len(engines)

print("")

while start_num != engine_quantity:
    print(engines[start_num])
    start_num += 1

print("")

engine = str(input("Search Engine : "))
query = str(input("Query : "))

if engine == engines[0]:
    w.open(f"https://www.google.com/search?q={query}")

if engine == engines[1]:
    w.open(f"https://duckduckgo.com/?q={query}")

if engine == engines[2]:
    w.open(f"https://lite.duckduckgo.com/lite/?q={query}")

if engine == engines[3]:
    w.open(f"https://brainly.com/app/ask?q={query}")

if engine == engines[4]:
    w.open(f"https://www.startpage.com/do/search?q={query}")

if engine == engines[5]:
    w.open(f"https://www.pinterest.com/search/pins/?q={query}")

if engine == engines[6]:
    w.open(f"http://www.usatodayeducate.com/?s={query}")

if engine == engines[7]:
    attributes = [
        "&sort=",
        "&datefilter="
    ]

    sort = str(input("[ Relevance | Date ]\nSort By: "))
    datefilter = str(input("[ past 24 hours | 7 days | 60 days | 12 months | all since 2005 ]\nDate Filter: "))

    w.open(f"https://www.washingtonpost.com/newssearch/?btn-search=&query={query}{attributes[0]}{sort}{attributes[1]}{datefilter}")

if engine == engines[8]:
    w.open(f"https://www.youtube.com/results?search_query={query}")

if engine == engines[9]:
    teacherName = str(input("Teacher's Name: "))
    w.open(f"https://www.ratemyprofessors.com/search.jsp?query={query}")

if engine == engines[10]:
    w.open(f"http://localhost:8090/yacysearch.html?query={query}")

if engine == engines[11]:
    w.open(f"https://invidious.fdn.fr/search?q={query}")

if engine == engines[12]:
    attributes = [
        "&size=",
        "&category=",
        "&sort=",
        "&type="
    ]
    size = str(input("Articles Per Page [1-50]: "))
    catagory = str(input("[ all cnn | us | world | politics | business | opinion | health | entertainment | style | travel ]\nCatagory: "))
    sort = str(input("[ relevance | newest ]\nSort By: "))
    type = str(input("[ everything | article | video | gallery ]\nType: "))

    if catagory == "all cnn":
        w.open(f"https://www.cnn.com/search?q={query}{attributes[0]}{size}{attributes[2]}{sort}{attributes[3]}{type}")

    elif type == "everything":
        w.open(f"https://www.cnn.com/search?q={query}{attributes[0]}{size}{attributes[1]}{catagory}{attributes[2]}{sort}")

    elif catagory == "all cnn" and type == "everything":
        w.open(
            f"https://www.cnn.com/search?q={query}{attributes[0]}{size}{attributes[2]}{sort}")

    elif catagory != "all cnn" and type != "everything":
        w.open(f"https://www.cnn.com/search?q={query}{attributes[0]}{size}{attributes[1]}{catagory}{attributes[2]}{sort}{attributes[3]}{type}")