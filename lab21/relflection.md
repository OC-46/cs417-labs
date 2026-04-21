Which section gave you a bug mypy caught that you wouldn’t have caught by reading the code? Be specific — what was the error message, what was the underlying mistake, and why is that kind of mistake easy to make in Python?

When making the badge in section 5, reading the code you wouldve thought nothing was wrong but by assinging id and name to their data types mypy could now catch the meistakes. This is easy to make because nothing is tchincally wrong with the code, the problem would onyl arise later if you entered the wrong data types into each section. 

Runtime cost. Type hints don’t run at runtime — Python ignores them. Mypy is a separate tool you choose to run. What’s the cost and benefit of that design choice? What would change if Python enforced types at runtime the way Java does?

Because there is no runtime costs you can continue to add the type hits in as you code without slowing down the program. If python had the same restrictions as java, you would get a response automatically but theres more of a runtime in the program and less probably less flexability. 

TypedDict vs plain dict. A dict can play two roles: a record with a fixed set of named fields (like Lab 18’s roster row), or a mapping from variable keys to values (like Lab 20’s completed dict that maps submission IDs to results). For each of these two cases, would you reach for TypedDict or dict[K, V], and why?

in Lab18 you would defintely use type dict so it owuld help yuo catch typos and make sure everything exist that should be there. but in lab 20 I would say you use dict with mapping because you are mapping submissions to the results.