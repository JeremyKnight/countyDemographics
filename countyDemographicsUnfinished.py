import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))
    print(most_women(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first=counties[0]["County"]
    for c in counties:
        if c["County"]<first:
            first = c["County"]
    return first

def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    count = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"]>count:
            count = c["Age"]["Percent Under 18 Years"]

    string= counties[int(count)]["County"] + ", " + counties[int(count)]["State"]
    return string
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    count = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"]>count:
            count = c["Age"]["Percent Under 18 Years"]

    #string= counties[int(count)]["County"] + "," + counties[int(count)]["State"]
    return counties[int(count)]["Age"]["Percent Under 18 Years"]


def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    count = counties[0]["Age"]["Percent Under 18 Years"]

    for c in counties:
        if c["Age"]["Percent Under 18 Years"]>count:
            count = c["Age"]["Percent Under 18 Years"]

    string= counties[int(count)]["County"] + ", " + counties[int(count)]["State"] + ": " + str(counties[int(count)]["Age"]["Percent Under 18 Years"])
    return string


def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    #Find the state in the dictionary with the most counties
    #Return the state with the most counties
    dict = {}
    text=counties[0]["State"]
    x=0
    i=0
    for c in counties:
        if text == c["State"]:
            x+=1
        else:
            #dict[text]=x  <--this works
            #dict["State": text] ["num of counties": x}
            dict[i]={"State": text, "num of counties": x}
            text=c["State"]
            x=0
            i+=1
    y=0
    name =""
    count=0
    #for c in dict:
    while count<len(dict):
        if y<dict[count]["num of counties"]:
            y=dict[count]["num of counties"]
            name=dict[count]["State"]
        count+=1

    return name + ': ' + str(y)



#if text==state name than: x+=1 else



def most_women(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    """=county with biggest percentage of women"""
    count=counties[0]["Miscellaneous"]["Percent Female"]
    name=""
    for c in counties:
        if count<c["Miscellaneous"]["Percent Female"]:
            count=c["Miscellaneous"]["Percent Female"]
            name=c["County"]
    string=name+ ': ' + str(count)
    return string
if __name__ == '__main__':
    main()
