
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


  expected_result = '''
  ApiData("https://data.ssb.no/api/v0/no/table/11418/", 
    MaaleMetode=c("01"), Yrke=c("1111", "1112"), AvtaltVanlig=c("5"), ContentsCode=c("Manedslonn"), Tid=c("2021"), 
    defaultJSONquery=TRUE)
  '''
  
  call_result = make_px_call(url, query) 

  assert call_result.strip() == expected_result.strip()


