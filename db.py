import requests
import xml.etree.ElementTree as ET
import time
headers = {"Authorization": "Bearer 2a71d5a2335896206f908ed2b9035853"}


thisdate =  time.strftime("%Y-%m-%d", time.time()-3600*12)
print thisdate 
t300 = requests.get("https://api.resrobot.se/v2/trip?key=78d03ab5-d9bc-4734-9e09-70ee80d286f9&destId=740098548&originId=800060110&format=json&date="+thisdate+"&operators=380&time=12:00")
t301 = requests.get("https://api.resrobot.se/v2/trip?key=78d03ab5-d9bc-4734-9e09-70ee80d286f9&destId=800060110&originId=740098548&format=json&date="+thisdate+"&operators=380&time=12:00")

data.Trip[0].LegList.Leg[0].Stops.Stop;


def get(train, stop, date, time):
    deps = requests.get("https://api.deutschebahn.com/timetables/v1/plan/"+stop+"/"+date+"/"+time, headers=headers)
    timetable = ET.fromstring(deps.content)
    for dep in timetable:
        if dep.find('tl').attrib["n"] == train:
            id = dep.attrib["id"]
            print(ET.tostring(dep, encoding="utf-8"))
            chgs = requests.get("https://api.deutschebahn.com/timetables/v1/fchg/"+stop+"", headers=headers)
            changes = ET.fromstring(chgs.content)
            for change in changes:
                if change.attrib["id"] == id:
                    print("RT --> ")
                    print(ET.tostring(change, encoding="utf-8"))

get("301", "8011102","210715","08")
print(" ---> ")
get("301", "8002549","210715","05")
print(" ---> ")

print(" ---> ")
get("300", "8011102","210714","19")
print(" ---> ")
get("300", "8002549","210714","23")
