# Random permutation validator  
  
###  `user` _(Bash?)_ linux executable is in `dist` folder  
run executable in linux = `exec appriori [...(opt param)]`  
Necessary params:  
- `-i or --input` - `filename.type`  
- `-g or --given` - `field names`  
- `-e or --expected` - `field names`  
- `-p or --permutations` - `int permutations`  
  
Optional params:  
- `-d or --debug` - `enables debug features`
  
example: exec appriori -i fanituotteet.csv -g "Caps,Mugs" -e "TShirts" -p 100  
  
### `user` Expected file input  
Id;Caps;Mugs;TShirts;  
1;1;1;1;  
2;0;0;0;  
3;1;1;1;  
where `id` is expected (and removed from calc)  
and matrix dimensions are dynamic (unbound) 

### `dev` Py3 environment  
- install python3 virtualenv  
- start virtualenv=source bin/activate  
- stop virtualenv=deactivate  

### `dev` Script usage in linux wiht python3 installed  
python3 appriori.py [...(opt param)]  
syntax of left/right group = 'classA,classB'  
read output on `target.csv`  
  
