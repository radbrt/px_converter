import json
import streamlit as st
import os

from src.px_converter_function import make_px_call

"""
# PxWebApiData call creator

Statistics Norway (and likely Denmark and Sweden as well) make the json request for an API call available when you have created a table on the web portal - which is cool.

For people who like using R and the PxWebApiData library, it would be better to get the actual API call - basically a differently formatted version of the JSON.

This app converts the URL and JSON provided by Statistics Norway into an `ApiData` function call.
"""

# def make_px_call(url, full_query):


#     json_query = full_query["query"]
#     all_dimensions = []

#     for dimension in json_query:
#         quoted_selection_values = [f'"{v}"' for v in dimension["selection"]["values"]]

#         if quoted_selection_values:
#             dimension_argument = f"{dimension['code']}=c({', '.join(quoted_selection_values)})"
#         else:
#             dimension_argument = f"{dimension['code']}=FALSE"

#         all_dimensions.append(dimension_argument)

#     all_dimensions_string = ", ".join(all_dimensions)

#     px_call = f"""ApiData(\"{url}\", 
#     {all_dimensions_string}, 
#     defaultJSONquery=TRUE)"""

#     return px_call


url_input = st.text_input("The api endpoint URL")
json_string_input = st.text_area("The API request JSON")

if url_input and json_string_input:
    full_json = json.loads(json_string_input)

    api_call = make_px_call(url_input, full_json)

    st.code(api_call)
