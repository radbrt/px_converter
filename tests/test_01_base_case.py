
from  src.px_converter_function import make_px_call


def test_simple():

  url = 'https://data.ssb.no/api/v0/no/table/11418/'
  query = {
    "query": [
      {
        "code": "MaaleMetode",
        "selection": {
          "filter": "item",
          "values": [
            "01"
          ]
        }
      },
      {
        "code": "Yrke",
        "selection": {
          "filter": "vs:NYK08Lonnansatt",
          "values": [
            "1111",
            "1112"
          ]
        }
      },
      {
        "code": "AvtaltVanlig",
        "selection": {
          "filter": "item",
          "values": [
            "5"
          ]
        }
      },
      {
        "code": "ContentsCode",
        "selection": {
          "filter": "item",
          "values": [
            "Manedslonn"
          ]
        }
      },
      {
        "code": "Tid",
        "selection": {
          "filter": "item",
          "values": [
            "2021"
          ]
        }
      }
    ],
    "response": {
      "format": "json-stat2"
    }
  }


  expected_result_str = '''
ApiData("https://data.ssb.no/api/v0/no/table/11418/", 
    MaaleMetode=list('item', c("01")), 
    Yrke=list('vs:NYK08Lonnansatt', c("1111", "1112")), 
    AvtaltVanlig=list('item', c("5")), 
    ContentsCode=list('item', c("Manedslonn")), 
    Tid=list('item', c("2021")), 
    defaultJSONquery=TRUE)
  '''
  
  call_result = [line.strip() for line in make_px_call(url, query).split('\n')]
  expected_result = [line.strip() for line in expected_result_str.split('\n')]

  assert call_result == expected_result

