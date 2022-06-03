# Example file for parsing and processing JSON.
import urllib.request
import json
def printResults(data):
    # Use the json module to load the string data into a dictionary.
    theJSON = json.loads(data)

    # Now we can access the contents of the JSON like any other python object.
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    # Output the number of events, plus the magnitude and each event name.
    count = theJSON["metadata"]["count"]
    print(str(count) + "events recorded")
    print("\n")

    '''# For each event, print the place where it occurred.
    for i in theJSON["features"]:
      print(i["properties"]["place"])
    print("--------\n")
    # Print the events that only have a magnitude greater than 4.
    for i in theJSON["features"]:
      if i["properties"]["mag"] >= 4.0:
        print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    print("--------\n")'''
    # Print only the events where at least 1 person reported feeling something.
    print("Events that were felt:")
    for i in theJSON["features"]:
      feltReports = i["properties"]["felt"]
      if feltReports != None:
        if feltReports > 0:
         print("%2.1f" %i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times")



def main():
    # Define a variable to hold the source URL.
    # In this case we are using the free data feed from the USGS.
    # This feed lists all earthquakes for the last day larger Mag 2.5
    urlData =  "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received error")

if __name__=="__main__":
    main()        



