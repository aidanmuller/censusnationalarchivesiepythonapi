# censusnationalarchivesiepythonapi
An API for the census.nationalarchives.ie written in and for Python. <br>
Made for the 1911 census.<br>
<br>
# documentation
```python
getcensusresults(firstname, lastname, county, town)
```
<br>
Returns number of results.<br>
If you do not know any parameters just replace it with ''.<br>
E.G getcensusresults('', 'Muller', '', '') returns the integer 15.<br>
<br>
`getcensus(firstname, lastname, county, town)`<br>
Returns firstname and lastname.<br>
If you do not know any parameters just replace it with ''.<br>
E.G getcensus('', 'Muller', '', '', 3) returns the 3rd person with the surname Muller, which happens to be ('Muller', 'Houe').<br>
