# HTML匹配检测
import re
from stack import Stack


def htmlChecker(htmlstr):
    # 匹配模式
    pattern = "<(.+?)>"
    # 将匹配模型编译为匹配规则
    html_pat = re.compile(pattern)
    # 将htmlst中复合匹配规则的提取出来形成一个列表
    tags = html_pat.findall(htmlstr)
    tag_stack = Stack()

    # if tags:
    #     for tag in tags:
    #         tag = tag.strip()
    #         if not tag.startswith("/"):
    #             tag_stack.push(tag)
    #         else:
    #             tag = tag.replace("/", "")
    #             if tag_stack.isEmpty():
    #                 print("html is not balanced, check: ", tag)
    #                 return False
    #             stack_top = tag_stack.pop()
    #             if stack_top != tag:
    #                 print("html is not balanced, check: ", one)
    #                 return False
    #     if not tag_stack.isEmpty():
    #         print("html is not closed, please check!")
    #         return False
    # print("html is balanced!")
    # return True

    balanced = True
    index = 0
    while index < len(tags) and balanced:
        tag = tags[index].strip()
        if not tag.startswith("/"):
            tag_stack.push(tag)
        else:
            tag = tag.replace("/", "")
            if tag_stack.isEmpty():
                print("html is not balanced, check: ", tag)
                balanced = False
            else:
                # 弹出栈的top元素与tag进行比较
                stack_top = tag_stack.pop()
                if stack_top != tag:
                    print("html is not balanced, check: ", tag)
                    balanced = False
        index += 1

    if balanced and tag_stack.isEmpty():
        print("html is balanced!")
        return True
    else:
        print("html is not closed, please check!")
        return False

# 测试
html_str = """
<html>
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
</html>
"""
htmlChecker(html_str)
html_str += "<a>"
htmlChecker(html_str)
html_str = "<a></b>"
htmlChecker(html_str)