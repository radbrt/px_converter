import json
import streamlit as st
import os
"""
# PxWebApiData call creator

Statistics Norway (and likely Denmark and Sweden as well) make the json request for an API call available when you have created a table on the web portal - which is cool.

For people who like using R and the PxWebApiData library, it would be better to get the actual API call - basically a differently formatted version of the JSON.

This app converts the URL and JSON provided by Statistics Norway into an `ApiData` function call.
"""


url_input = st.text_input("The api endpoint URL")
json_string_input = st.text_area("The API request JSON")

if url_input and json_string_input:
    full_json = json.loads(json_string_input)

    json_query = full_json["query"]
    all_dimensions = []

    for dimension in json_query:
        quoted_selection_values = [f'"{v}"' for v in dimension["selection"]["values"]]
        selection = dimension["selection"]

        joinstring = ",\n"

        if quoted_selection_values:
            dimension_argument = f"{dimension['code']}=c({', '.join(quoted_selection_values)})"
        else:
            dimension_argument = f"{dimension['code']}=FALSE"

        # if selection.get('filter'):
        #     dimension_argument = f"{dimension['code']}=list('{selection.get('filter')}', c({joinstring.join(quoted_selection_values)}))"
        # else:
        #     dimension_argument = f"{dimension['code']}=c({', '.join(quoted_selection_values)})"
        
        all_dimensions.append(dimension_argument)

    all_dimensions_string = ", ".join(all_dimensions)

    full = f"""ApiData(\"{url_input}\", 
    {all_dimensions_string}, 
    defaultJSONquery=TRUE)"""

    st.code(full)
