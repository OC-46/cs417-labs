Reflection

1:

Hard to change aspects:
- Everything was in the "main" finction 
- The map was hardcoded and didnt fit the json file structure. 
- The CSV parser only read the file and didnt parse anything

After:
- The "main" function now only does what its supposed to do, reads files, calls parsing and build_report helpers, and print the report
- the parsing function and parsing categories function both work with json now in the json shape
- the parse csv and parse json functions now take the input and return a list of row of dicts.

I was correct that the biggest pain points were the tangled I/O/logic and the hard-coded category mapping. there acually wasnt any crazy big changes that needed to be made.

2:

    I separated parsing by separation of I/O from logic into parse_csv and parse_json 
The design is separation of the file types but same problem.'parse_csv' now transforms CSV text into row dicts 'parse_json' loads JSON text into the same row shape. This means the rest of the time the code dosent care if the file was a csv or json, its now parsed and can be catagorised. 

I changed the categorize function to accept the dict shape and return the first matching category. The designidea is the dependency injection and pluggable parts. the parse_categories_json() reads the file and then the main() func passes that to the build_report. The test can only pass the custom category maps. 

I refactored the build report to compute the totals from just the inputs. the design idea is the separate I/O from logic. It no longer opens any files or prints anything the main() func is whats in charge of that. This allows the core logic to be tested without any of the filesystem being involved. 


3:

Part 2 was the hardest because the starter code was using the wrong category shape. The best solution was to change the categorize() func to work with the dict format and make sure it didnt matter what file strucuter the data cam from that it would be able to be processed.

4:
If we were to use data coming from an api you would want to add a function to get the transactions from the api and then have another function to parse the api responses that you would be reciving. The same as we did for the csv and json files. In the main function we would chose the data source, get the raw data and then resuse our build report function to compute the totals.
