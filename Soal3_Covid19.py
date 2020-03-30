#%%
from bs4 import BeautifulSoup
import requests
import folium as fo
import pandas as pd

url = "https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Indonesia"
x = requests.get(url)
datacorona = pd.read_html(x.text)
prov = requests.get(
    "https://raw.githubusercontent.com/LintangWisesa/Indonesia-Covid19-Maps/master/data/gps_indonesia.json"
)
pv = prov.json()
peta = fo.Map(location=[-1.6948082, 106.238069], zoom_start=4.58)

for i in range(len(pv)):
    icona = fo.features.CustomIcon(pv[i]["logo"], icon_size=(30,30))

    fo.Marker(
        popup="<h4><b>"
        + pv[i]["Provinsi"]
        + "</b></h4><table><tbody><tr><th style='color:red'>Confirmed&nbsp;&nbsp;</th><th style='color:green'>Recovered&nbsp;&nbsp;</th><th style='color:black'>Deaths&nbsp;&nbsp;</th></tr><tr><td><center><b style='color:red'>"
        + datacorona[3]["Confirmed"]["1330"][i]
        + "</b></center></td><td><center><b style='color:green'>"
        + datacorona[3]["Recovered"]["64"][i]
        + "</b></center></td><td><center><b>"
        + datacorona[3]["Deaths"]["114"][i]
        + "</b></center></td></tr></tbody></table>",
        location=[pv[i]["latitude"], pv[i]["longitude"]],
        tooltip=pv[i]["Provinsi"],
        icon=icona,
        legend_name="Indonesia Covid-19"
    ).add_to(peta)

peta.save("petacovid.html")


#%%
