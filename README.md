# CSV To ElasticSearch Python Converter 📃
<b>CSV To ElasticSearch Convertion Using Python.<b/>
<br />
<b>The Code Is Located In The "CSV-Elastic.py" File And Uses The "flight_data.csv" CSV File<b/>
<br />
<br />
## The Index Template 📋
```json
        PUT _template/flights
        {
          "index_patterns": ["flights-*"],
          "mappings": {
            "properties": {
              "Carrier": {"type":"keyword"},
              "dayOfWeek": {"type":"integer"},

              "Dest": {"type":"keyword"},
              "DestAirportID": {"type":"keyword"},
              "DestCityName": {"type":"keyword"},
              "DestCountry": {"type":"keyword"},
              "DestLocation": {"type":"geo_point"},
              "DestRegion": {"type":"keyword"},
              "DestWeather": {"type":"keyword"},

              "DistanceKilometers": {"type":"double"},
              "DistanceMiles": {"type":"double"},

              "FlightDelay": {"type":"boolean"},
              "FlightDelayMin": {"type":"integer"},
              "FlightDelayType": {"type":"keyword"},

              "FlightNum": {"type":"keyword"},
              "FlightTimeHour": {"type":"double"},
              "FlightTimeMin": {"type":"double"},
              "Hour_of_day": {"type":"integer"},

              "Origin": {"type":"keyword"},
              "OriginAirportID": {"type":"keyword"},
              "OriginCityName": {"type":"keyword"},
              "OriginCountry": {"type":"keyword"},
              "OriginLocation": {"type":"geo_point"},
              "OriginRegion": {"type":"keyword"},
              "OriginWeather": {"type":"keyword"},

              "timestamp": {"type":"date", "format": ["MMM dd, yyyy @ HH:mm:ss.SSS"]},
              "Cancelled": {"type":"boolean"},
              "AvgTicketPrice": {"type":"float"}
            }
          }
        }
        
```
## The Discover 🔍 (Press Image To Enlarge)
<p align="center">
    <img width="1500" height = 500 src="https://user-images.githubusercontent.com/43177100/215349792-98e177c2-95f2-4fce-bd33-bbc8db957b4d.png" alt="Elastic">
</p>


        
## An Output Document Example 🖥
```json
        "_index" : "flight_data",
        "_type" : "_doc",
        "_id" : "7bqH84UB3vH4fRGhh7Pz",
        "_score" : 1.0,
        "_source" : {
          "AvgTicketPrice" : "$271.01",
          "Cancelled" : "true",
          "timestamp" : "Jan 12, 2022 @ 23:21:22.000",
          "OriginWeather" : "Rain",
          "OriginRegion" : "SE-BD",
          "OriginLocation" : "{\n  \"coordinates\": [\n    18.60169983,\n    -33.96480179\n  ],\n  \"type\": \"Point\"\n}",
          "OriginCountry" : "ZA",
          "OriginCityName" : "Cape Town",
          "OriginAirportID" : "CPT",
          "Origin" : "Cape Town International Airport",
          "hour_of_day" : "21",
          "FlightTimeMin" : "811.468",
          "FlightTimeHour" : "13.524470071170063",
          "FlightNum" : "3MXWA2E",
          "FlightDelayType" : "No Delay",
          "FlightDelayMin" : "0",
          "FlightDelay" : "false",
          "DistanceMiles" : "8,067.567",
          "DistanceKilometers" : "12,983.491",
          "DestWeather" : "Hail",
          "DestRegion" : "SE-BD",
          "DestLocation" : "{\n  \"coordinates\": [\n    121.8050003,\n    31.14340019\n  ],\n  \"type\": \"Point\"\n}",
          "DestCountry" : "CN",
          "DestCityName" : "Shanghai",
          "DestAirportID" : "PVG",
          "Dest" : "Shanghai Pudong International Airport",
          "dayOfWeek" : "2",
          "Carrier" : "Logstash Airways"
        }
        
```
