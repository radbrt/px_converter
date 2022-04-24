from  src.px_converter_function import make_px_call


def test_empty_dimension():
  url = 'https://data.ssb.no/api/v0/no/table/11450/'
  query = {
    "query": [
      {
        "code": "Konsumgrp",
        "selection": {
          "filter": "vs:CoiCop",
          "values": []
        }
      },
      {
        "code": "ContentsCode",
        "selection": {
          "filter": "item",
          "values": [
            "KpiAar"
          ]
        }
      },
      {
        "code": "Tid",
        "selection": {
          "filter": "item",
          "values": [
            "2016"
          ]
        }
      }
    ],
    "response": {
      "format": "json-stat2"
    }
  }

  expected_result_str = '''
ApiData("https://data.ssb.no/api/v0/no/table/11450/", 
    Konsumgrp=FALSE, 
    ContentsCode=list('item', c("KpiAar")), 
    Tid=list('item', c("2016")), 
    defaultJSONquery=TRUE)
  '''
  
  call_result = [line.strip() for line in make_px_call(url, query).split('\n')]
  expected_result = [line.strip() for line in expected_result_str.split('\n')]

  assert call_result == expected_result
