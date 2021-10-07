# cs61a-sp21
personal solutions on labs, projects and homework of CS61A Spring 2021.

# detailed solutions
https://www.cnblogs.com/ikventure/p/14984919.html



### project 4: scheme interpreter

https://www.cnblogs.com/ikventure/p/15059547.html

#### overview

- Read 读取  返回Pair实例

  - scheme_tokens.py  词法分析 lexer

    tokenize_lines 函数将scheme表达式分解为token标记，返回一个tokens的Buffer对象

    `(+ 1 2)`将返回`['(', '+', '1', '2', ')']`

  - scheme_reader.py  句法分析 parser 

    将scheme标记解析为python表示

    - scheme_read 返回Buffer中的下一个完整表达式
    - read_tail 返回Buffer中的的剩余部分

- Eval 计算

  - scheme.py → scheme_eval and scheme_apply 
    - scheme_eval 在给定环境中计算scheme表达式的值
    - scheme_apply 将函数Procedure应用到参数上
  - scheme.py → `do_?_form`  运算特殊表达式，如do_define_form

- Print 打印

  - 打印`__str__`表示

- Loop 循环

  - scheme.py → read_eval_print_loop
