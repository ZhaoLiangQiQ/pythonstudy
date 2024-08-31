{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#  Python大数据课程之Python基础"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 一、第一部分"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1 Python数据类型"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1.1 字符串"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "在Python中用引号引起来的字符集称之为字符串，比如：'hello'、\"my Python\"、\"2+3\"等都是字符串\n",
    "Python中字符串中使用的引号可以是单引号、双引号跟三引号"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world!\n"
     ]
    }
   ],
   "source": [
    "print ('hello world!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "It is a \"dog\"!\n"
     ]
    }
   ],
   "source": [
    "c = 'It is a \"dog\"!'\n",
    "print (c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "It's a dog!\n"
     ]
    }
   ],
   "source": [
    "c1= \"It's a dog!\"\n",
    "print (c1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "world\n",
      "!\n"
     ]
    }
   ],
   "source": [
    "c2 = \"\"\"hello\n",
    "world\n",
    "!\"\"\"\n",
    "print (c2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 转义字符'\\'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "转义字符\\可以转义很多字符，比如\\n表示换行，\\t表示制表符，字符\\本身也要转义，所以\\\\表示的字符就是\\"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "It's a dog!\n",
      "hello world!\n",
      "hello Python!\n",
      "\\\t\\\n"
     ]
    }
   ],
   "source": [
    "print ('It\\'s a dog!')\n",
    "print (\"hello world!\\nhello Python!\")\n",
    "print ('\\\\\\t\\\\')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "原样输出引号内字符串可以使用在引号前加r"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\\\\\\t\\\\\n"
     ]
    }
   ],
   "source": [
    "print (r'\\\\\\t\\\\')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 子字符串及运算"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "s = 'Python'\n",
    "print( 'Py' in s)\n",
    "print( 'py' in s)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "取子字符串有两种方法，使用[]索引或者切片运算法[:]，这两个方法使用面非常广"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "t\n"
     ]
    }
   ],
   "source": [
    "print (s[2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yth\n"
     ]
    }
   ],
   "source": [
    "print (s[1:4])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 字符串连接与格式化输出"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The first word is \"hello\", and the second word is \"world\"\n",
      "hello world!\n"
     ]
    }
   ],
   "source": [
    "word1 = '\"hello\"'\n",
    "word2 = '\"world\"'\n",
    "sentence = word1.strip('\"') + ' ' + word2.strip('\"') + '!'\n",
    "\n",
    "print( 'The first word is %s, and the second word is %s' %(word1, word2))\n",
    "print (sentence)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1.2 整数与浮点数"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 整数\n",
    "\n",
    "Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "i = 7\n",
    "print (i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "7 + 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "7 - 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "21"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "7 * 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "343"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "7 ** 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.3333333333333335"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "7 / 3#Python3之后，整数除法和浮点数除法已经没有差异"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "7 % 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "7//3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 浮点数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.3333333333333335"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "7.0 / 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "314.0"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3.14 * 10 ** 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "其它表示方法"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "0b1111"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "255"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "0xff"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.2e-05"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "1.2e-5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "更多运算"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.0\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "print (math.log(math.e)) # 更多运算可查阅文档"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1.3 布尔值"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "True and False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "True or False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "True + False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "18 >= 6 * 3 or 'py' in 'Python'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "18 >= 6 * 3 and 'py' in 'Python'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "18 >= 6 * 3 and 'Py' in 'Python'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1.4 日期时间"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "time.struct_time(tm_year=2016, tm_mon=7, tm_mday=20, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=202, tm_isdst=-1)\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "\n",
    "now = time.strptime('2016-07-20', '%Y-%m-%d')\n",
    "print (now)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2016-07-20'"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "time.strftime('%Y-%m-%d', now)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import datetime\n",
    "\n",
    "someDay = datetime.date(1999,2,10)\n",
    "anotherDay = datetime.date(1999,2,15)\n",
    "deltaDay = anotherDay - someDay\n",
    "deltaDay.days"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "还有其他一些datetime格式\n",
    "![](images/09b1dbf9ccdb4b69b614a0875b4e5f4c_006tKfTcgy1fkr9s9113dj30g80i7weq.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 查看变量类型"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "NoneType"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(1.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bool"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s=\"NoneType\"\n",
    "type(s)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 类型转换"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'10086'"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str(10086)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "?float()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10086.0"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "float(10086)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10086"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int('10086')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10086+0j)"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "complex(10086)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2 Python数据结构"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "列表（list）、元组（tuple）、集合（set）、字典（dict）"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2.1 列表(list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "用来存储一连串元素的容器，列表用[]来表示，其中元素的类型可不相同。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "mylist= [0, 1, 2, 3, 4, 5]\n",
    "print (mylist)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "列表索引和切片"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4]= 4\n",
      "[-4]= 2\n",
      "[0:4]= [0, 1, 2, 3]\n",
      "[:4]= [0, 1, 2, 3]\n",
      "[4:]= [4, 5]\n",
      "[0:4:2]= [0, 2]\n",
      "[-5:-1:]= [1, 2, 3, 4]\n",
      "[-2::-1]= [4, 3, 2, 1, 0]\n"
     ]
    }
   ],
   "source": [
    "# 索引从0开始，含左不含右\n",
    "print ('[4]=', mylist[4])\n",
    "print ('[-4]=', mylist[-4])\n",
    "print ('[0:4]=', mylist[0:4])\n",
    "print ('[:4]=', mylist[:4])#dddd\n",
    "print( '[4:]=', mylist[4:])\n",
    "print ('[0:4:2]=', mylist[0:4:2]) # 0到4，步长为2\n",
    "print ('[-5:-1:]=', mylist[-5:-1:]) # 倒数第5个元素开始到倒数第一个元素，倒序\n",
    "print ('[-2::-1]=', mylist[-2::-1])  # 倒数第二个元素开始到序列开始的元素，倒序"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "修改列表"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "小月\n",
      "小楠\n",
      "19978\n"
     ]
    }
   ],
   "source": [
    "mylist[3] = \"小月\"  \n",
    "print (mylist[3])\n",
    "\n",
    "mylist[5]=\"小楠\"\n",
    "print (mylist[5])\n",
    "\n",
    "mylist[5]=19978\n",
    "print (mylist[5])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, '小月', 4, 19978]\n"
     ]
    }
   ],
   "source": [
    "print (mylist)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "插入元素"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, '小月', 4, 19978, 'han', 'long', 'wan']\n"
     ]
    }
   ],
   "source": [
    "mylist.append('han') # 添加到尾部\n",
    "mylist.extend(['long', 'wan']) # 添加到尾部\n",
    "print (mylist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, [90, 80, 75, 66], 1, 2, '小月', 4, 19978, 'han', 'long', 'wan']"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scores = [90, 80, 75, 66]\n",
    "mylist.insert(1, scores) # 添加到指定位置\n",
    "mylist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "a=[]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "删除元素"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[90, 80, 75, 66]\n",
      "[0, 1, 2, '小月', 4, 19978, 'han', 'long', 'wan']\n"
     ]
    }
   ],
   "source": [
    "print (mylist.pop(1)) # 该函数返回被弹出的元素，不传入参数则删除最后一个元素\n",
    "print (mylist)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "判断元素是否在列表中等"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "print( 'wan' in mylist)\n",
    "print ('han' not in mylist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mylist.count('wan')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mylist.index('wan')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "range函数生成整数列表"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "range(0, 10)\n",
      "range(-5, 5)\n",
      "range(-10, 10, 2)\n",
      "range(16, 10, -1)\n"
     ]
    }
   ],
   "source": [
    "print (range(10))\n",
    "print (range(-5, 5))\n",
    "print (range(-10, 10, 2))\n",
    "print (range(16, 10, -1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2.2 元组(tuple)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "元组类似列表，元组里面的元素也是进行索引计算。列表里面的元素的值可以修改，而元组里面的元素的值不能修改，只能读取。元组的符号是()。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('ming', 'jun', 'qiang', 'wu', [90, 80, 75, 66])"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "studentsTuple = (\"ming\", \"jun\", \"qiang\", \"wu\", scores)\n",
    "studentsTuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TypeError\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    studentsTuple[1] = 'fu'\n",
    "except TypeError:\n",
    "    print ('TypeError')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('ming', 'jun', 'qiang', 'wu', [90, 100, 75, 66])"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scores[1]= 100\n",
    "studentsTuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'ming' in studentsTuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('ming', 'jun', 'qiang', 'wu')"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "studentsTuple[0:4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "studentsTuple.count('ming')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "studentsTuple.index('jun')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(studentsTuple)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2.3 集合(set)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Python中集合主要有两个功能，一个功能是进行集合操作，另一个功能是消除重复元素。 集合的格式是：set()，其中()内可以是列表、字典或字符串，因为字符串是以列表的形式存储的"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0, 1, 2, 'han', 4, 'long', 'wan', 19978, '小月'}\n"
     ]
    }
   ],
   "source": [
    "studentsSet = set(mylist)\n",
    "print (studentsSet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0, 1, 2, 'han', 4, 'long', 'xu', 'wan', 19978, '小月'}\n"
     ]
    }
   ],
   "source": [
    "studentsSet.add('xu')\n",
    "print (studentsSet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0, 1, 2, 'han', 4, 'long', 'wan', 19978, '小月'}\n"
     ]
    }
   ],
   "source": [
    "studentsSet.remove('xu')\n",
    "print (studentsSet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a= {'n', 'g', 'm', 'c', 's', 'b', 'a'}\n"
     ]
    }
   ],
   "source": [
    "a = set(\"abcnmaaaaggsng\")\n",
    "print ('a=', a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b= {'f', 'm', 'd', 'c'}\n"
     ]
    }
   ],
   "source": [
    "b = set(\"cdfm\")\n",
    "print ('b=', b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x= {'c', 'm'}\n"
     ]
    }
   ],
   "source": [
    "#交集\n",
    "x = a & b \n",
    "print( 'x=', x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "y= {'g', 'n', 'f', 'c', 'm', 's', 'b', 'a', 'd'}\n",
      "z= {'g', 'n', 's', 'b', 'a'}\n",
      "{'g', 'n', 's', 'b', 'a'}\n"
     ]
    }
   ],
   "source": [
    "#并集\n",
    "y = a | b\n",
    "print ('y=', y)\n",
    "#差集\n",
    "z = a - b\n",
    "print( 'z=', z)\n",
    "#去除重复元素\n",
    "new = set(a)\n",
    "print( z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2.4字典(dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Python中的字典dict也叫做关联数组，用大括号{}括起来，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度，其中key不能重复。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "guilin\n"
     ]
    }
   ],
   "source": [
    "k = {\"name\":\"weiwei\", \"home\":\"guilin\"}\n",
    "print (k[\"home\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['name', 'home'])\n",
      "dict_values(['weiwei', 'guilin'])\n"
     ]
    }
   ],
   "source": [
    "print( k.keys())\n",
    "print( k.values())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "添加、修改字典里面的项目"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'guangzhou', 'home': 'guilin', 'like': 'music'}\n"
     ]
    }
   ],
   "source": [
    "k[\"like\"] = \"music\"\n",
    "k['name'] = 'guangzhou'\n",
    "print (k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "k.get('edu', -1) # 通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "删除key-value元素"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'guangzhou', 'home': 'guilin'}\n"
     ]
    }
   ],
   "source": [
    "k.pop('like')\n",
    "print (k)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2.5 列表、元组、集合、字典的互相转换"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(mylist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0, 1, 2, '小月', 4, 19978, 'han', 'long', 'wan')"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tuple(mylist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['name', 'home']"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<zip object at 0x00000135BEAF2A88>\n",
      "{'A': 1, 'B': 2, 'C': 3}\n"
     ]
    }
   ],
   "source": [
    "zl = zip(('A', 'B', 'C'), [1, 2, 3, 4]) # zip可以将列表、元组、集合、字典‘缝合’起来\n",
    "print (zl)\n",
    "print (dict(zl))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3 Python控制流"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "在Python中通常的情况下程序的执行是从上往下执行的，而某些时候我们为了改变程序的执行顺序，使用控制流语句控制程序执行方式。Python中有三种控制流类型：顺序结构、分支结构、循环结构。"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "另外，Python可以使用分号\";\"分隔语句，但一般是使用换行来分隔；语句块不用大括号\"{}\"，而使用缩进（可以使用四个空格）来表示"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.1 顺序结构"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "36\n"
     ]
    }
   ],
   "source": [
    "s = '7'\n",
    "num = int(s) # 一般不使用这种分隔方式\n",
    "num -= 1 # num = num - 1 \n",
    "num *= 6 # num = num * 6\n",
    "print (num)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.2 分支结构：Python中if语句是用来判断选择执行哪个语句块的"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "if <True or Flase表达式>:\n",
    "    执行语句块\n",
    "elif <True or Flase表达式>：\n",
    "    执行语句块\n",
    "else：        # 都不满足\n",
    "    执行语句块\n",
    "    \n",
    "# elif子句可以有多条，elif和else部分可省略"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "..........\n"
     ]
    }
   ],
   "source": [
    "salary = 1000\n",
    "if salary > 10000:\n",
    "    print (\"Wow!!!!!!!\")\n",
    "elif salary > 5000:\n",
    "    print (\"That's OK.\")\n",
    "elif salary > 3000:\n",
    "    print (\"5555555555\")\n",
    "else:\n",
    "    print (\"..........\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.3 循环结构"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "while 循环"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "while <True or Flase表达式>:\n",
    "    循环执行语句块\n",
    "else：          # 不满足条件\n",
    "    执行语句块\n",
    "\n",
    "#else部分可以省略"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "Hello\n",
      "Hello\n",
      "Hello\n",
      "Hello\n",
      "Done\n"
     ]
    }
   ],
   "source": [
    "a = 1\n",
    "while a < 10:\n",
    "    if a <= 5:\n",
    "        print (a)\n",
    "    else:\n",
    "        print (\"Hello\")\n",
    "    a = a + 1\n",
    "else:\n",
    "    print (\"Done\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- for 循环"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "for (条件变量) in (集合)：\n",
    "    执行语句块\n",
    "    \n",
    "# “集合”并不单指set，而是“形似”集合的列表、元组、字典、数组都可以进行循环\n",
    "# 条件变量可以有多个"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yao 226\n",
      "Sharq 216\n",
      "AI 183\n"
     ]
    }
   ],
   "source": [
    "heights = {'Yao':226, 'Sharq':216, 'AI':183}\n",
    "for i in heights:\n",
    "    print (i, heights[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yao 226\n",
      "Sharq 216\n",
      "AI 183\n"
     ]
    }
   ],
   "source": [
    "for key, value in heights.items():\n",
    "    print(key, value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5050\n"
     ]
    }
   ],
   "source": [
    "total = 0\n",
    "for i in range(1, 101):\n",
    "    total += i#total=total+i\n",
    "print (total)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.4 break、continue和pass"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "break:跳出循环\n",
    "continue:跳出当前循环,继续下一次循环\n",
    "pass:占位符，什么也不做"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 5):\n",
    "    if i == 3:\n",
    "        break\n",
    "    print (i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 5):\n",
    "    if i == 3:\n",
    "        continue\n",
    "    print (i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 5):\n",
    "    if i == 3:\n",
    "        pass\n",
    "    print (i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.5 列表生成式"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "三种形式\n",
    "- [<表达式> for (条件变量) in (集合)]\n",
    "- [<表达式> for (条件变量) in (集合) if <'True or False'表达式>]\n",
    "- [<表达式> if <'True or False'表达式> else <表达式>  for (条件变量) in (集合) ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Apple', 'Watermelon', 'Banana']"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruits = ['\"Apple', 'Watermelon', '\"Banana\"']\n",
    "[x.strip('\"') for x in fruits] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Apple', 'Watermelon', 'Banana']"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 另一种写法\n",
    "test_list=[]\n",
    "for x in fruits:\n",
    "    x=x.strip('\"')\n",
    "    test_list.append(x)\n",
    "test_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 9, 25, 49, 81, 121, 169, 225, 289, 361]"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[x ** 2 for x in range(21) if x%2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 9, 25, 49, 81, 121, 169, 225, 289, 361]"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 另一种写法\n",
    "test_list=[]\n",
    "for x in range(21):\n",
    "    if x%2:\n",
    "        x=x**2\n",
    "        test_list.append(x)\n",
    "test_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[m + n for m in 'ABC' for n in 'XYZ']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 另一种写法\n",
    "test_list=[]\n",
    "for m in 'ABC':\n",
    "    for n in 'XYZ':\n",
    "        x=m+n\n",
    "        test_list.append(x)\n",
    "test_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['x=A', 'y=B', 'z=C']"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d = {'x': 'A', 'y': 'B', 'z': 'C' }\n",
    "[k + '=' + v for k, v in d.items()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['x=A', 'y=B', 'z=C']"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 另一种写法\n",
    "test_list=[]\n",
    "for k, v in d.items():\n",
    "    x=k + '=' + v\n",
    "    test_list.append(x)\n",
    "test_list"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4 Python函数"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "函数是用来封装特定功能的实体，可对不同类型和结构的数据进行操作，达到预定目标"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.1 调用函数"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Python内置了很多有用的函数，我们可以直接调用，进行数据分析时多数情况下是通过调用定义好的函数来操作数据的"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "str1 = \"as\"\n",
    "int1 = -9\n",
    "print (len(str1))\n",
    "print (abs(int1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Apple', 'Banana', 'Melon', 'Grape']\n"
     ]
    }
   ],
   "source": [
    "fruits = ['Apple', 'Banana', 'Melon']\n",
    "fruits.append('Grape')\n",
    "print (fruits)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.2 定义函数"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "当系统自带函数不足以完成指定的功能时，需要用户自定义函数来完成。"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "def 函数名()：\n",
    "    函数内容\n",
    "    函数内容\n",
    "    <return 返回值>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def my_abs(x):\n",
    "    if x >= 0:\n",
    "        return x\n",
    "    else:\n",
    "        return -x\n",
    "    \n",
    "my_abs(-9)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "可以没有return"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n",
      "['Apple', 'Banana', 'Grape']\n"
     ]
    }
   ],
   "source": [
    "def filter_fruit(someList, d):\n",
    "    for i in someList:\n",
    "        if i == d:\n",
    "            someList.remove(i)\n",
    "        else:\n",
    "            pass\n",
    "\n",
    "print (filter_fruit(fruits, 'Melon'))\n",
    "print (fruits)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "多个返回值的情况"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4 5 20\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "tuple"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def test(i, j):\n",
    "    k = i * j\n",
    "    return i, j, k\n",
    "\n",
    "a , b , c = test(4, 5)\n",
    "print (a, b , c)\n",
    "type(test(4, 5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.3 高阶函数"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 把另一个函数作为参数传入一个函数，这样的函数称为高阶函数"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "函数本身也可以赋值给变量，函数与其它对象具有同等地位"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myFunction = abs\n",
    "myFunction(-9)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 参数传入函数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def add(x, y, f):\n",
    "    return f(x) + f(y)\n",
    "\n",
    "add(7, -5, myFunction)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 常用高阶函数"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "map/reduce: map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回；reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<map at 0x135bea80438>"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myList = [-1, 2, -3, 4, -5, 6, 7]\n",
    "map(abs, myList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3560020598205630145296938"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from functools import reduce\n",
    "def powerAdd(a, b):\n",
    "    return pow(a, 2) + pow(b, 2)\n",
    "\n",
    "reduce(powerAdd, myList) # 是否是计算平方和？"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "filter： filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<filter at 0x135bea93b00>"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def is_odd(x):\n",
    "    return x % 3  # 0被判断为False，其它被判断为True\n",
    "\n",
    "filter(is_odd, myList)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "sorted: 实现对序列排序，默认情况下对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "默认排序：数字大小或字母序（针对字符串）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[-5, -3, -1, 2, 4, 6, 7]"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted(myList)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 返回函数: 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function __main__.powAdd.<locals>.power>"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def powAdd(x, y):\n",
    "    def power(n):\n",
    "        return pow(x, n) + pow(y, n)\n",
    "    return power\n",
    "\n",
    "myF = powAdd(3, 4)\n",
    "myF"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myF(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 匿名函数：高阶函数传入函数时，不需要显式地定义函数，直接传入匿名函数更方便"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f = lambda x: x * x\n",
    "f(4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "等同于："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "def f(x):\n",
    "    return x * x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<map at 0x135beaaa0b8>"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "map(lambda x: x * x, myList)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "匿名函数可以传入多个参数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "140"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reduce(lambda x, y: x + y, map(lambda x: x * x, myList))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "返回函数可以是匿名函数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def powAdd1(x, y):\n",
    "    return lambda n: pow(x, n) + pow(y, n)\n",
    "\n",
    "lamb = powAdd1(3, 4)\n",
    "lamb(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 其它"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 标识符第一个字符只能是字母或下划线，第一个字符不能出现数字或其他字符；标识符除第一个字符外，其他部分可以是字母或者下划线或者数字，标识符大小写敏感，比如name跟Name是不同的标识符。\n",
    "- Python规范：\n",
    "* 类标识符每个字符第一个字母大写；\n",
    "* 对象\\变量标识符的第一个字母小写，其余首字母大写，或使用下划线'_' 连接；\n",
    "* 函数命名同普通对象。"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 关键字"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "关键字是指系统中自带的具备特定含义的标识符"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']\n"
     ]
    }
   ],
   "source": [
    "# 查看一下关键字有哪些，避免关键字做自定义标识符\n",
    "import keyword\n",
    "print (keyword.kwlist)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 注释"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Python中的注释一般用#进行注释"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 帮助"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "可以用？或者help()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
