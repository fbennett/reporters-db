## Background of the Free Law Reporters Database

A long, long time ago near a courthouse not too far away, people started 
keeping books of every important opinion that was ever written. These books 
became known as *reporters* and were generally created by librarian-types of 
yore such as [Mr. William Cranch][crancherton] and [Alex Dallas][dalorama].

These men were busy for the next few centuries and created *thousands* of 
these books, culminating in what we know today as West's reporters or as 
regional reporters like the "Dakota Reports" or the thoroughly-named, 
"Synopses of the Decisions of the Supreme Court of Texas Arising from 
Restraints by Conscript and Other Military Authorities (Robards)."
 
In this repository we've taken a look at all these reporters and tried to 
sort out what we know about them and convert that to data. Naturally, 
converting several century's history into clean data results in a mess, but 
we've done our best and this mess is in use in a number of projects as listed
below.

We hope you'll find this useful to your endeavors and that you'll share your
work with the community.


## Known Implementations
 
 1. This work was originally deployed in the [CourtListener][cl] citation 
    finder beginning in about 2012. It has been used literally millions of 
    times to identify citations between cases.

 1. An extension for Firefox known as the [Free Law Ferret][ferret] uses this 
    code to find citations in your browser as you read things -- all over the 
    Web.
    
 1. A Node module called [Walverine][walv] uses an iteration of this code to
    find citations using the V8 JavaScript engine.


## Some Notes on the Data

Some things to bear in mind as you are examining the Free Law Reporters 
Database:

 1. Each Reporter key maps to a list of reporters that that key can represent. 
    In some cases (especially in early reporters), the key is ambiguous, 
    referring to more than one possible reporter.
 1. Formats follow the Blue Book standard, with variations listed for local 
    rules.
 1. The `variations` key consists of data from local rules, found through 
    organic usage in our corpus and from the [Cardiff Index to Legal 
    Abbreviations][cardiff]. We have used a dict for these values due to the 
    fact that there can be variations for each series.
 1. `mlz_jurisdiction` corresponds to the work that is being done for 
    Multi-Lingual Zotero.
 1. Regarding dates of the editions, there are a few things to know. In 
    reporters with multiple series, if multiple volumes have the same dates, 
    this indicates that the point where one series ends and the other begins is
    unknown. If an edition has 1750 as its start date, this indicates that the 
    actual start date is unknown. Likewise, if an edition has `null` as its 
    end date, that indicates the actual end date is either unknown, or it's
    known that the series has not completed. These areas need research before 
    we can release version 1.1 of this database.
    
Some notes on the `state_abbreviations` and `case_name_abbreviations` files:

 1. Abbreviations are based on data from the values in the nineteenth edition 
    of the Blue Book supplemented with abbreviations found in our corpus.
 1. `case_name_abbreviations.json` contains the abbreviations that are likely 
    to occur in the case name of an opinion.
 1. `state_abbreviations.json` contains the abbreviations that are likely to be
    used to refer to American states.
    
       
### Notes on Specific Data Point and References

 1. Mississippi supports neutral citations, but does so in their own format, as 
    specified in [this rule][missingthepoint]. Research is needed for the 
    format in `reporters.json` to see if it is used accidentally as a variant 
    of their rule or whether it is an error in this database.
 1. New Mexico dates confirmed via the [table here][nmdates].
 1. Both Puerto Rico and "Pennsylvania State Reports, Penrose and 
    Watts" use the citation "P.R." 


## Installation (Python)

You can install the Free Law Reporters Database with a few simple commands:

    sudo git clone https://github.com/freelawproject/reporters-db /usr/local/reporters_db
    sudo ln -s /usr/local/reporters_db /usr/lib/python2.7/dist-packages/reporters_db

Once installed you can use it in your code with something like:

    from reporters_db import REPORTERS

You can see all of the variables that can be imported by looking in 
`__init__.py`. Other variables currently include: `STATE_ABBREVIATIONS`, 
`CASE_NAME_ABBREVIATIONS`, `VARIATIONS_ONLY`, and `EDITIONS`. These latter two
are convenience variables that you can use to get different views of the 
`REPORTERS` data.

Of course, if you're not using Python, the data is in the `json` format, so 
you should be able to import it using your language of choice.


## Tests

[![Build Status](https://travis-ci.org/freelawproject/reporters-db.svg?branch=master)][travis]

We have a few tests that make sure things haven't completely broken. They are
automatically run by Travis CI each time a push is completed and should be run
by developers as well before pushing. They can be run with:

    python tests.py
    
It's pretty simple, right?


## Version History

### Past Versions

 - 1.0: Has all common Blue Book reporters, with their variations from the Cardiff database.
 - 1.0.1
    
    1. Bug fix after application to Lawbox bulk data
    2. Updates cite_type for better granularity and to eliminate a few errors.
    3. Adds WL, LEXIS and U.S. App. LEXIS as specialty_lexis and specialty_west cite_types.
    4. `fed` cite_type has been converted to `federal`

 - 1.0.2
    
    1. Adds tests to verify the data (see ./tests.py)
    2. Fixes a few data issues after applying tests

### Current Version

 - 1.0.9: Updates the mlz_jurisdiction field to be state-specific, per issue #1.

### Future Versions

 - 1.1: All dates are dialed in to the nearest year for every edition of every reporter (some still require
         research beyond what Blue Book provides).
 - 1.2: All dates are dialed into the correct day for every edition of every reporter.
 - 1.x: International Reporters added?
 - 2.0: Other features (suggestions welcome)?


## License

This repository is available under the permissive BSD license, making it easy 
and safe to incorporate in your own libraries.

Pull and feature requests welcome. Online editing in Github is possible (and easy!)



[crancherton]: https://en.wikipedia.org/wiki/William_Cranch
[dalorama]: https://en.wikipedia.org/wiki/Alexander_J._Dallas_%28statesman%29
[cl]: https://www.courtlistener.com
[ferret]: http://citationstylist.org/2013/08/20/free-law-ferret-document-to-cited-cases-in-a-click/
[walv]: https://github.com/adelevie/walverine
[cardiff]: http://www.legalabbrevs.cardiff.ac.uk/
[missingthepoint]: http://www.aallnet.org/main-menu/Advocacy/access/citation/neutralrules/rules-ms.html
[nmdates]: http://www.nmcompcomm.us/nmcases/pdf/NM%20Reports%20to%20Official%20-%20Vols.%201-75.pdf
[travis]: https://travis-ci.org/freelawproject/reporters-db
