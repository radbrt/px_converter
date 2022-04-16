import json
import streamlit as st
import os
"""
# PxWebApiData call creator

Statistics Norway (and likely Denmark and Sweden as well) make the json request for an API call available when you have created a table on the web portal - which is cool.

For people who like using R and the PxWebApiData library, it would be better to get the actual API call - basically a differently formatted version of the JSON.

This app converts the URL and JSON provided by Statistics Norway into an `ApiData` function call.
"""


url = st.text_input("The api endpoint URL")
txt = st.text_area("The API request JSON")

if url and txt:
    d = json.loads(txt)

    l = d["query"]
    ttot = []

    for k in l:
        qstrings = [f'"{v}"' for v in k["selection"]["values"]]
        sel = k["selection"]

        joinstring = ",\n"

        if sel.get('filter'):
            totlist = f"{k['code']}=list('{sel.get('filter')}', c({joinstring.join(qstrings)}))"
        else:
            totlist = f"{k['code']}=c({', '.join(qstrings)})"
        
        ttot.append(totlist)

    totlist_tot = ", ".join(ttot)

    full = f"""ApiData(\"{url}\", 
    {totlist_tot}, 
    defaultJSONquery=TRUE)"""

    st.code(full)
