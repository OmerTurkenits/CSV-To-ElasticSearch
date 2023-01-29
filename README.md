# CSV To ElasticSearch Python Converter 📃
<b>CSV To ElasticSearch Convertion Using Python.<b/>
<br />
<b>The Code Is Located In The "CSV-Elastic.py" File And Uses The "flight_data.csv" CSV File<b/>
<br />
<br />
## The Index Template 📋
```json
        PUT _template/flights-29-01-23
        {
          "index_patterns": ["flights-29-01-23*"],
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
{
  "_index": "flights_index-29-01-2023",
  "_type": "_doc",
  "_id": "wbbN_oUBVyJEN8App7il",
  "_version": 1,
  "_score": 1,
  "_source": {
    "AvgTicketPrice": 280.26,
    "Cancelled": false,
    "timestamp": "2022-01-12'T'23:05:37.000000",
    "OriginWeather": "Cloudy",
    "OriginRegion": "SE-BD",
    "OriginLocation": [
      "-58.5358",
      "-34.8222"
    ],
    "OriginCountry": "AR",
    "OriginCityName": "Buenos Aires",
    "OriginAirportID": "EZE",
    "Origin": "Ministro Pistarini International Airport",
    "hour_of_day": 21,
    "FlightTimeMin": 549.317,
    "FlightTimeHour": 9.155290925297226,
    "FlightNum": "WYZ2OB2",
    "FlightDelayType": "No Delay",
    "FlightDelayMin": 0,
    "FlightDelay": false,
    "DistanceMiles": 5119.951,
    "DistanceKilometers": 8239.762,
    "DestWeather": "Damaging Wind",
    "DestRegion": "US-VA",
    "DestLocation": [
      "-77.31970215",
      "37.50519943"
    ],
    "DestCountry": "US",
    "DestCityName": "Richmond",
    "DestAirportID": "RIC",
    "Dest": "Richmond International Airport",
    "dayOfWeek": 2,
    "Carrier": "Kibana Airlines"
  },
  "fields": {
    "Origin": [
      "Ministro Pistarini International Airport"
    ],
    "FlightNum": [
      "WYZ2OB2"
    ],
    "OriginLocation": [
      "-58.5358",
      "-34.8222"
    ],
    "DestLocation": [
      "-77.31970215",
      "37.50519943"
    ],
    "OriginCityName.keyword": [
      "Buenos Aires"
    ],
    "FlightDelay": [
      false
    ],
    "Carrier.keyword": [
      "Kibana Airlines"
    ],
    "DistanceMiles": [
      5119.951
    ],
    "FlightTimeMin": [
      549.317
    ],
    "timestamp.keyword": [
      "2022-01-12'T'23:05:37.000000"
    ],
    "OriginWeather": [
      "Cloudy"
    ],
    "dayOfWeek": [
      2
    ],
    "DestAirportID.keyword": [
      "RIC"
    ],
    "AvgTicketPrice": [
      280.26
    ],
    "DestLocation.keyword": [
      "-77.31970215",
      "37.50519943"
    ],
    "Carrier": [
      "Kibana Airlines"
    ],
    "FlightDelayMin": [
      0
    ],
    "Origin.keyword": [
      "Ministro Pistarini International Airport"
    ],
    "OriginRegion": [
      "SE-BD"
    ],
    "OriginRegion.keyword": [
      "SE-BD"
    ],
    "DestAirportID": [
      "RIC"
    ],
    "hour_of_day": [
      21
    ],
    "FlightDelayType": [
      "No Delay"
    ],
    "timestamp": [
      "2022-01-12'T'23:05:37.000000"
    ],
    "FlightDelayType.keyword": [
      "No Delay"
    ],
    "Dest": [
      "Richmond International Airport"
    ],
    "OriginLocation.keyword": [
      "-58.5358",
      "-34.8222"
    ],
    "FlightTimeHour": [
      9.155291
    ],
    "OriginWeather.keyword": [
      "Cloudy"
    ],
    "Dest.keyword": [
      "Richmond International Airport"
    ],
    "Cancelled": [
      false
    ],
    "FlightNum.keyword": [
      "WYZ2OB2"
    ],
    "DistanceKilometers": [
      8239.762
    ],
    "DestCountry.keyword": [
      "US"
    ],
    "OriginCountry.keyword": [
      "AR"
    ],
    "OriginCityName": [
      "Buenos Aires"
    ],
    "DestRegion.keyword": [
      "US-VA"
    ],
    "OriginAirportID.keyword": [
      "EZE"
    ],
    "DestWeather": [
      "Damaging Wind"
    ],
    "OriginCountry": [
      "AR"
    ],
    "DestWeather.keyword": [
      "Damaging Wind"
    ],
    "DestCountry": [
      "US"
    ],
    "DestCityName.keyword": [
      "Richmond"
    ],
    "DestRegion": [
      "US-VA"
    ],
    "OriginAirportID": [
      "EZE"
    ],
    "DestCityName": [
      "Richmond"
    ]
  }
}
        
```
