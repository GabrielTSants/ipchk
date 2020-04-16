#!/usr/bin/env python3

import requests
import ast
import argparse


# ipchck
# Author: Gabriel Tito Santos
# E-mail: rlgts@hotmail.com
# Date: 20200411

# vers = 0.1


class main:
    # Parser Config
    parser = argparse.ArgumentParser(usage="Usage: ipchk [IP|HOST] [Options]", prog="ipchk")
    parser.add_argument('address', action='store', type=str)
    parser.add_argument('-a', '--all', help='Print all info', action='store_true')
    parser.add_argument('-i', '--ip', help='IP from target', action='store_true')
    parser.add_argument('-c', '--country', help='Country Name', action='store_true')
    parser.add_argument('-r', '--region', help='Region Name', action='store_true')
    parser.add_argument('-z', '--zip', help='Zip Code', action='store_true')
    parser.add_argument('-t', '--timezone', help='Time Zone', action='store_true')
    parser.add_argument('-x', '--coord', help='Coordinates', action='store_true')
    # Export Variables
    args = parser.parse_args()  # args global variable

    # www Validation
    if args.address[:2] != "www":
        args.address = "www." + args.address
    print(args.address)

    url = "https://freegeoip.app/json/" + args.address

    headers = {
        'accept': "application/json",
        'content-type': "application/json"
    }

    response = requests.request("GET", url, headers=headers, )

    # Conversion of string in dictionary
    convert_string = ast.literal_eval(response.text)

    # Parameters CLI
    if args.all:
        print("IP: " + convert_string["ip"])
        print("Country: " + convert_string["country_name"] + " - " + convert_string["country_code"])
        print("Region Code: " + convert_string["region_code"])
        print("Zip Code: " + convert_string["zip_code"])
        print("Time Zone: " + convert_string["time_zone"])
        print("Latitude: " + str(convert_string["latitude"]) + " Longitude: " + str(convert_string["longitude"]))

    if args.ip:
        print("IP: " + convert_string["ip"])

    if args.country:
        print("Country: " + convert_string["country_name"] + " - " + convert_string["country_code"])

    if args.region:
        print("Region Code: " + convert_string["region_code"])

    if args.zip:
        print("Zip Code: " + convert_string["zip_code"])

    if args.coord:
        print("Latitude: " + str(convert_string["latitude"]) + " Longitude: " + str(convert_string["longitude"]))

    if args.timezone:
        print("Time Zone: " + convert_string["time_zone"])


if __name__ == '__main__':
    main()
