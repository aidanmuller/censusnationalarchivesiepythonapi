# http://www.census.nationalarchives.ie/search/results.jsp?searchMoreVisible=false&census_year=1911&surname=Muller&firstname=&county19011911=&county1821=&county1831=&county1841=&county1851=&barony=&parish=&ward=&townland=&houseNumber=&familyId=&ded=&age=&sex=&search=Search&ageInMonths=&relationToHead=&religion=&education=&occupation=&marriageStatus=&yearsMarried=&birthplace=&nativeCountry=&language=&deafdumb=&causeOfDeath=&yearOfDeath=&familiesNumber=&malesNumber=&femalesNumber=&maleServNumber=&femaleServNumber=&estChurchNumber=&romanCatNumber=&presbNumber=&protNumber=&marriageYears=&childrenBorn=&childrenLiving=

from bs4 import BeautifulSoup
import urllib2 as u
import re

def getcensusresults(forename='', surname='', county='', town=''):
    # GET URL TO QUERY
    url = 'http://www.census.nationalarchives.ie/search/results.jsp?searchMoreVisible=false&census_year=1911&surname={}&firstname={}&county19011911={}&county1821=&county1831=&county1841=&county1851=&barony=&parish=&ward=&townland={}&houseNumber=&familyId=&ded=&age=&sex=&search=Search&ageInMonths=&relationToHead=&religion=&education=&occupation=&marriageStatus=&yearsMarried=&birthplace=&nativeCountry=&language=&deafdumb=&causeOfDeath=&yearOfDeath=&familiesNumber=&malesNumber=&femalesNumber=&maleServNumber=&femaleServNumber=&estChurchNumber=&romanCatNumber=&presbNumber=&protNumber=&marriageYears=&childrenBorn=&childrenLiving='.format(surname, forename, county, town)
    d = u.urlopen(url).read()
    # FIND STRING IN HTML CONTAINING NUMBER OF RESULTS FROM SEARCH
    results = d[d.find('<span class="short">'):len(d)]
    results = results[0:results.find('</span>')+7]
    # NARROW THE STRING FROM 'DISPLAYING RESULTS X-Y of Z' to just 'Z'
    results = results[results.find('of ')+3:len(results)-7]
    return int(results)

def getcensus(forename='', surname='', county='', town='', result=0):
    # GET URL TO QUERY
    url = 'http://www.census.nationalarchives.ie/search/results.jsp?searchMoreVisible=false&census_year=1911&surname={}&firstname={}&county19011911={}&county1821=&county1831=&county1841=&county1851=&barony=&parish=&ward=&townland={}&houseNumber=&familyId=&ded=&age=&sex=&search=Search&ageInMonths=&relationToHead=&religion=&education=&occupation=&marriageStatus=&yearsMarried=&birthplace=&nativeCountry=&language=&deafdumb=&causeOfDeath=&yearOfDeath=&familiesNumber=&malesNumber=&femalesNumber=&maleServNumber=&femaleServNumber=&estChurchNumber=&romanCatNumber=&presbNumber=&protNumber=&marriageYears=&childrenBorn=&childrenLiving=&pager.offset={}'.format(surname, forename, county, town, result)
    d = u.urlopen(url).read()
    # FIND LAST NAME AND FIRST NAME IN SEARCH RESULT
    lname = d[d.find('"odd"')+6:len(d)]
    tdpoint = lname.find('</td>')
    lname = lname[4:lname.find('</td>')]
    link = BeautifulSoup(lname, features="lxml").find_all('a', href=True)[0]['href']
    link = 'http://census.nationalarchives.ie{}'.format(link)
    lname = BeautifulSoup(lname, features="lxml").a.string
    fname = d[d.find('"odd"')+6:len(d)]
    fname = fname[tdpoint+5:len(d)]
    fname = fname[4:fname.find('</td')]
    fname = BeautifulSoup(fname, features="lxml").a.string
    return str(lname), str(fname), link

