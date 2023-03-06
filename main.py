
import requests
import bs4
import http.client
http.client._MAXHEADERS = 1000

r = requests.get("https://www.otomoto.pl/osobowe/abarth")
soup = bs4.BeautifulSoup(r.text, 'html.parser')
#advertisement = soup.find_all(class_='e1p19lg76 e1p19lg720 ooa-10p8u4x er34gjf0')
advertisement = soup.find_all("h2", {"class": "e1p19lg76 e1p19lg720 ooa-10p8u4x er34gjf0"})

def gathering_adreses(x):
    """
    1. extracting adresses
    2. returning them in correct form
    """
    adresses = []
    for i in x:
        start_adres = str(i).find("https")  # Find adress start of ad
        end_adres = str(i).find("html")  # find adress end of ad
        start_adres -= 0
        end_adres += 4
        adres = ""
        for html_len in range(start_adres, end_adres):
            adres += str(i)[html_len]  # sklej cały adres ogłoeszenia
        adresses.append(adres)  # dodaj adres do listy ogłoszeń
    return adresses

# def gathering_params(x):
#     """"
#     1.gathering parameters of car
#     """
#     params = []
#     for i in x:
#         start_adres = str(i).find("title=")  # Find start of parameters of car
#         end_adres = str(i).find(">")  # find end of parameters of car
#         start_adres += 7
#         end_adres -= 1
#         adres = ""
#         for par_len in range(start_adres, end_adres):
#             adres += str(i)[par_len]  # glue together chars in parameter
#         params.append(adres)  
#     return params


