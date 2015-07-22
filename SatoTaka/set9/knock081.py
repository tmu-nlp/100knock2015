#!/usr/bin/python
# _*_coding:utf-8 _*_ 

import sys

def main():
    country_name = ["United States", "United Arab Emirates", "Antigua and Barbuda", "United Kingdom", "Islamic Republic of Iran", "Isle of Man", "El Salvador", "Netherlands Antilles", "Cape Verde", "Cote d'Ivoire", "Costa Rica", "Saudi Arabia", "Sao Tome and Principe", "San Marino", "Sierra Leone", "Syrian Arab Republic", "Equatorial Guinea", "Saint Kitts and Nevis", "Saint Vincent and the Grenadines", "Saint Lucia", "Solomon Islands", "Republic of Korea", "United Republic of Tanzania", "Czech Republic", "Central African Republic", "Democratic People's Republic of Korea", "Dominican Republic", "Trinidad and Tobago", "New Zealand", "Holy See", "Vatican City State", "Papua New Guinea", "Burkina Faso", "Brunei Darussalam", "Viet Nam", "Bosnia and Herzegovina", "Marshall Islands", "the former Yugoslav Republic of Macedonia", "Federated States of Micronesia", "South Africa", "Republic of Moldova", "Lao People's Democratic Republic", "Libyan Arab Jamahiriya", "Russian Federation"]

    input_file = open(sys.argv[1], "r")

    for line in input_file:
        line = line.strip()
        for country in country_name:
            if country in line:
               line = line.replace(country, "_".join(country.split(" ")))
        print line

    input_file.close()

if __name__=="__main__":
   main()
