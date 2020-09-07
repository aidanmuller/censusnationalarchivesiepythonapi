# http://www.census.nationalarchives.ie/search/results.jsp?searchMoreVisible=false&census_year=1911&surname=Muller&firstname=&county19011911=&county1821=&county1831=&county1841=&county1851=&barony=&parish=&ward=&townland=&houseNumber=&familyId=&ded=&age=&sex=&search=Search&ageInMonths=&relationToHead=&religion=&education=&occupation=&marriageStatus=&yearsMarried=&birthplace=&nativeCountry=&language=&deafdumb=&causeOfDeath=&yearOfDeath=&familiesNumber=&malesNumber=&femalesNumber=&maleServNumber=&femaleServNumber=&estChurchNumber=&romanCatNumber=&presbNumber=&protNumber=&marriageYears=&childrenBorn=&childrenLiving=
#nd = d[d.find('Displaying resul')-1:len(d)]
#npages = int(nd[nd.find('Displaying results 1 - 10 of ')+29:nd.find('</span>')])

from bs4 import BeautifulSoup
import urllib2 as u
import re

def getcensus1911(forename='', surname='', county='', town='', result=0):
    # Get URL of census query
    url = 'http://www.census.nationalarchives.ie/search/results.jsp?searchMoreVisible=false&census_year=1911&surname={}&firstname={}&county19011911={}&county1821=&county1831=&county1841=&county1851=&barony=&parish=&ward=&townland={}&houseNumber=&familyId=&ded=&age=&sex=&search=Search&ageInMonths=&relationToHead=&religion=&education=&occupation=&marriageStatus=&yearsMarried=&birthplace=&nativeCountry=&language=&deafdumb=&causeOfDeath=&yearOfDeath=&familiesNumber=&malesNumber=&femalesNumber=&maleServNumber=&femaleServNumber=&estChurchNumber=&romanCatNumber=&presbNumber=&protNumber=&marriageYears=&childrenBorn=&childrenLiving=&pager.offset={}'.format(surname, forename, county, town, result)
    d = u.urlopen(url).read()
    # Find where last name is stored in HTML
    # All Census information is in a tr class called odd
    # Find odd in result of query and locate the link which has the person's last name in it
    lname = d[d.find('"odd"')+6:len(d)]
    tdpoint = lname.find('</td>')
    lname = lname[4:lname.find('</td>')]
    # Parse <a href> and find what the contents of the <a href> is (the lastname)
    lname = BeautifulSoup(lname, features="lxml").a.string
    # Find odd
    fname = d[d.find('"odd"')+6:len(d)]
    # The first name is stored right after the last so we can just search the tags after the end of the <a href>
    fname = fname[tdpoint+5:len(d)]
    fname = fname[4:fname.find('</td')]
    # Parse for first name
    fname = BeautifulSoup(fname, features="lxml").a.string
    return str(lname), str(fname)

