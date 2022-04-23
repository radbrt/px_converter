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

  expected_result = '''
  ApiData("https://data.ssb.no/api/v0/no/table/11450/", 
    Konsumgrp=FALSE, ContentsCode=c("KpiAar"), Tid=c("2016"), 
    defaultJSONquery=TRUE)
  '''
  
  call_result = make_px_call(url, query) 

  assert call_result.strip() == expected_result.strip()
