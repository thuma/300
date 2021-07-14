import requests
import xml.etree.ElementTree as ET
headers = {"Authorization": "Bearer 2a71d5a2335896206f908ed2b9035853"}



def get(train, stop, date, time):
    deps = requests.get("https://api.deutschebahn.com/timetables/v1/plan/"+stop+"/"+date+"/"+time, headers=headers)
    timetable = ET.fromstring(deps.content)
    for dep in timetable:
        if dep.find('tl').attrib["n"] == train:
            id = dep.attrib["id"]
            print(ET.tostring(dep, encoding="utf-8"))
            print(dep.find('dp').attrib["pt"])
            print(dep.find('dp').attrib["pp"])
            print(dep.find('dp').attrib["ppth"])
            chgs = requests.get("https://api.deutschebahn.com/timetables/v1/fchg/"+stop+"", headers=headers)
            changes = ET.fromstring(chgs.content)
            for change in changes:
                if change.attrib["id"] == id:
                    print(ET.tostring(change, encoding="utf-8"))

get("300", "8011102","210724","19")
