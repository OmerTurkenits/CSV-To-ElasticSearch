# CSV To ElasticSearch Python Converter 📃
<b>CSV To Elasticsearch Convertion Using Python.<b/>
<br />
<b>The Code Is Located In The "File.py" File And Uses The "flight_data.csv" CSV File<b/>
<br />
<br />
## The Index Template 📋
```json
        PUT _template/flights
        {
          "index_patterns": ["flights-*"],
          "mappings": {
            "properties": {
              "carrier": {"type":"keyword"},
              "dayOfWeek": {"type":"integer"},

              "dest": {"type":"keyword"},
              "destAirportID": {"type":"keyword"},
              "destCityName": {"type":"keyword"},
              "destCountry": {"type":"keyword"},
              "destLocation": {"type":"geo_point"},
              "destRegion": {"type":"keyword"},
              "destWeather": {"type":"keyword"},

              "distanceKilometers": {"type":"double"},
              "distanceMiles": {"type":"double"},

              "flightDelay": {"type":"boolean"},
              "flightDelayMin": {"type":"integer"},
              "flightDelayType": {"type":"keyword"},

              "flightNum": {"type":"keyword"},
              "flightTimeHour": {"type":"double"},
              "flightTimeMin": {"type":"double"},
              "hour_of_day": {"type":"integer"},

              "origin": {"type":"keyword"},
              "originAirportID": {"type":"keyword"},
              "originCityName": {"type":"keyword"},
              "originCountry": {"type":"keyword"},
              "originLocation": {"type":"geo_point"},
              "originRegion": {"type":"keyword"},
              "originWeather": {"type":"keyword"},

              "timestamp": {"type":"date", "format": ["MMM dd, yyyy @ HH:mm:ss.SSS"]},
              "cancelled": {"type":"boolean"},
              "avgTicketPrice": {"type":"float"}
            }
          }
        }
        
```
        
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
