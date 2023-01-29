# Imports
import pandas as pd
import datetime
from elasticsearch import Elasticsearch

# Constants
CSV_FILE_PATH = "./flight_data.csv"
INDEX_NAME = "flights-29-01-23"


def price_handler(price: str) -> float:
    """
    Removes the dollar sign and commas from "price" type values,
        thus returning the price in float form.
    :param: price: The "price" value.
    :return: The price in float form.
    """
    price = price.replace("$", "")
    return comma_handler(price)


def comma_handler(num: str) -> float:
    """
    Removes the commas from number type values, and returns the string in number form.
    :param num: a string representation of a number.
    :return: the number as a float.
    """
    num = num.replace(",", "")
    return float(num)


def date_handler(date: str) -> str:
    """
    Converts the date to another format for the elasticsearch
    :param date: The date in the given format
    :return: The date in the new format
    """
    date = datetime.datetime.strptime(date, "%b %d, %Y @ %H:%M:%S.%f")
    return date.strftime("%Y-%m-%d'T'%H:%M:%S.%f")


def location_handler(location: str) -> list:
    """
    Converts the "Geo-Point" values to a list.
    :param: The geo point as a string form.
    :return: The geo point string as a list.
    """
    geo_list = location[location.index("[", 0, len(location)) + 1: location.index("]", 0, len(location))].split(",")
    new_geo_list = []

    for coordinate in geo_list:
        coordinate = coordinate.replace("\n", "")
        coordinate = coordinate.replace(" ", "")
        new_geo_list.append(coordinate)

    return new_geo_list


# A dict that contains an element and its corresponding handler function.
ELEMENT_HANDLER = {"AvgTicketPrice": price_handler,
                   "FlightTimeMin": comma_handler,
                   "DistanceMiles": comma_handler,
                   "DistanceKilometers": comma_handler,
                   "timestamp": date_handler,
                   "OriginLocation": location_handler,
                   "DestLocation": location_handler}


def main():
    # Connect to the elastic port.
    elastic_search = Elasticsearch(hosts=[{"host": "127.0.0.1", "port": 9200, "scheme": "http"}])

    # Create a panda reader element that reads the CSV file located at CSV_FILE_PATH.
    flight_data = pd.read_csv(CSV_FILE_PATH)

    for row, doc in flight_data.iterrows():

        # Convert the document to a dictionary.
        doc_dictionary = doc.to_dict()

        # Run through each element.
        for element in doc_dictionary:
            if element in ELEMENT_HANDLER.keys():
                doc_dictionary[element] = ELEMENT_HANDLER[element](doc_dictionary[element])

        # Push the document to the index.
        elastic_search.index(index=INDEX_NAME, body=doc_dictionary)


# The program's entry point
if __name__ == '__main__':
    main()
