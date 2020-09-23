# Random permutation validator  

## Introduction  
This project is a tool, created for validating appriori algorithm's inferred results. This program works by
randomising other-than index columns, and calculating confidence by:  
**given** = "when transaction has A.. ", **expected** = ".. transaction also has B,"  
**confidence = t / a**, where t is **given** & **expected** variables fulfilled and a is **given** variables fulfilled  
  
## Instructions 
  
###  `user` linux executable is in `dist` folder  
run executable in linux = `exec appriori [...(opt param)]`  
Necessary params:  
- `-i or --input` - `path-to-file/filename.type`  
- `-g or --given` - `field names`  
- `-e or --expected` - `field names`  
- `-p or --permutations` - `int permutations`  
  
Optional params:  
- `-d or --debug` - `enables debug features`  
end with `&` to not close terminal
  
example: **exec ./appriori -i fanituotteet.csv -g "Caps,Mugs" -e "TShirts" -p 100** 
  
read output on `target.csv`    
  
### `user` Expected file input  
Id,Caps,Mugs,TShirts,  
1,1,1,1  
2,0,0,0  
3,1,1,1  
where `id` is expected (and removed from calc)  
and matrix dimensions are dynamic (unbound) 

### `dev` Py3 environment  
- install python3 virtualenv  
- start virtualenv=source bin/activate  
- stop virtualenv=deactivate  

### `dev` Script usage in linux wiht python3 installed  
python3 appriori.py [...(opt param)]    
