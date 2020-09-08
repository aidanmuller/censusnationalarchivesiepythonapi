# censusnationalarchivesiepythonapi
An API for the census.nationalarchives.ie written in and for Python.
Made for the 1911 census.

# documentation
getcensusresults(firstname, lastname, county, town)
Returns number of results.
If you do not know any parameters just replace it with ''.
E.G getcensusresults('', 'Muller', '', '') returns the integer 15.

getcensus(firstname, lastname, county, town)
Returns firstname and lastname.
If you do not know any parameters just replace it with ''.
E.G getcensus('', 'Muller', '', '', 3) returns the 3rd person with the surname Muller, which happens to be ('Muller', 'Houe').
