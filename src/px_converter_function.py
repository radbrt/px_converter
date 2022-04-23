import json

def make_px_call(url, full_query):

    json_query = full_query["query"]
    all_dimensions = []

    for dimension in json_query:
        quoted_selection_values = [f'"{v}"' for v in dimension["selection"]["values"]]
        filter = dimension["selection"]["filter"]
        if quoted_selection_values:
            
            dimension_argument = f"{dimension['code']}=list('{filter}', c({', '.join(quoted_selection_values)}))"
        else:
            dimension_argument = f"{dimension['code']}=FALSE"

        all_dimensions.append(dimension_argument)

    all_dimensions_string = ", ".join(all_dimensions)

    px_call = f"""ApiData(\"{url}\", 
    {all_dimensions_string}, 
    defaultJSONquery=TRUE)"""

    return px_call
