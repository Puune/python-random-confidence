## Random permutation validator  
# `dev` Py3 environment  
- install python3 virtualenv  
- start virtualenv=source bin/activate  
- stop virtualenv=deactivate  
  
# Bash executable is in `output` folder  
run executable in linux = `exec appriori file param param param`  
example: exec appriori fanituotteet.csv "Caps" "Mugs" 100  
  
# `dev` Script usage in linux wiht python3 installed  
python3 {String:filename.type} {String:left group} {Strint:right group} {integer: permutations}  
syntax of left/right group = 'classA,classB'  
read output on `target.csv`  
  
# `user` Expected file input  
id;asd;basd;ad;  
1;1;1;1;  
2;0;0;0;  
3;1;1;1;  
where `id` is expected (and removed from calc)  
and matrix dimensions are dynamic (unbound) 