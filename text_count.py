def text_statistics():
    print("=====文本数字统计工具=====")
    context=input("请输入或者粘贴需要统计的文本内容：")
    context_strip=context.strip()

    if len(context_strip)==0:
        print("错误不得输入内容为空")
        return

    total_char=len(context)
    no_space_char=len(context.replace(" ",""))
    word_list=context.split()
    english_char=len(word_list)
    china_count=0
    for char in context:
        if '\u4e00' <= char <= '\u9fff':
            china_count+=1
    print("=======统计结果=======")
    print(f"1.总字符数量，包含标点符号和空格哦：{total_char}")
    print(f"2.去除空格和标点符号的数量为：{no_space_char}")
    print(f"英文单词数目为：{english_char}")
    print(f"中文汉字数目为：{china_count}")
if __name__=="__main__":
    text_statistics()