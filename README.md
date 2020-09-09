# Random permutation validator  
  
###  `user` _(Bash?)_ linux executable is in `dist` folder  
run executable in linux = `exec appriori file params params permutations`  
example: exec appriori fanituotteet.csv "Caps,TShirts" "Mugs" 100  
  
### `user` Expected file input  
id;asd;basd;ad;  
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
python3 {String:filename.type} {String:left group} {Strint:right group} {integer: permutations}  
syntax of left/right group = 'classA,classB'  
read output on `target.csv`  
  
