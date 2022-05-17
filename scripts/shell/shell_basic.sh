#!/bin/bash
# https://www.cnblogs.com/alsodzy/p/8403870.html
# https://zhuanlan.zhihu.com/p/335813262
# 百度 shell basename
# c.biancheng.net/cpp/shell/
name=$1   # 接受第一个脚本参数
name=${name:0:6}01    #  截取代表字符串的name变量的[0：6）字符后面+“01”

# echo $name
#20210201  设输入$1="202102"
p_n=($(date -d "$name" +%Y%m) $(date -d "$name -1month" +%Y%m) $(date -d "$name -2month" +%Y%m))
#   $() 表示括号内的命令将会执行
# echo $p_n
inp=''
st_url=www.jk/
for m in ${p_n[@]}
do
  inp=${inp},${st_url}${m}*
#  echo $inp
  #,www.jk/202102*
  #,www.jk/202102*,www.jk/202101*
  #,www.jk/202102*,www.jk/202101*,www.jk/202012*
done

inp=${inp:1}
#echo $inp
# www.jk/202102*,www.jk/202101*,www.jk/202012*

lp=/hm/s1/wwfile
s_l_pf=$(basename ${lp})
#echo $s_l_pf
#wwfile