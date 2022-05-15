import json
import requests


def get_dimension(var):
    
    if var.get('elimination'):
        return f"{var['code']}=FALSE"
    elif var.get('time'):
        return f"{var['code']}=TRUE"
    else:
        return f"{var['code']}=TRUE"
            


def get_table_dimensions(url):

    r = requests.get(url)
    if not r.ok:
        return False

    spec = r.json()["variables"]
    return spec

def make_table_args(spec):
    args = [get_dimension(val) for val in spec]
    return args



def make_px_call(url, full_query):

    json_query = full_query["query"]
    query_dimensions = []

    for dimension in json_query:
        quoted_selection_values = [f'"{v}"' for v in dimension["selection"]["values"]]
        filter = dimension["selection"]["filter"]
        if quoted_selection_values:
            
            dimension_argument = f"{dimension['code']}=list('{filter}', c({', '.join(quoted_selection_values)}))"
        else:
            dimension_argument = f"{dimension['code']}=FALSE"

        query_dimensions.append(dimension_argument)

    included_codes = [dim['code'] for dim in json_query]
    base_dims = get_table_dimensions(url)
    additional_dims = [dim for dim in base_dims if dim['code'] not in included_codes]
    additional_dim_args = make_table_args(additional_dims)
    all_dimensions = query_dimensions + additional_dim_args

    all_dimensions_string = ", \n".join(all_dimensions)

    px_call = f"""
    ApiData(\"{url}\", 
    {all_dimensions_string})
    """

    return px_call
