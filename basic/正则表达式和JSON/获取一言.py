from urllib import request
import re
from threading import Timer
import time

# <div id="hitokoto" class="hitokoto-fullpage bounce animated">
#                     <div class="bracket left">『</div>
#                     <div class="word" id="hitokoto_text">万物初发清净明，可知此芽成何草。</div>
#                     <div class="bracket right">』</div>
#                 <div class="author" id="hitokoto_author">—— 「冰菓」</div>
#                 </div>

class OneTalk():
    url = 'https://hitokoto.cn/'
    pattern_get_word = '<div class="word" id="hitokoto_text">([\s\S]*?)</div>'
    pattern_get_author = '<div class="author" id="hitokoto_author">([\s\S]*?)</div>'

    def __fetch_content(self):
        r = request.urlopen(OneTalk.url)
        # bytes
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        # print(type(htmls))
        # print(htmls)
        return htmls

    def __get__one_talk(self, htmls):
        one_talked_word = re.findall(OneTalk.pattern_get_word, htmls)
        one_talked_author = re.findall(OneTalk.pattern_get_author, htmls)

        # words = {
        #     'word':one_talked_word,
        #     'author':one_talked_author
        # }
        words = str(one_talked_word) + str(one_talked_author)
        # print(words)
        return words

    def __refine(self, words):
        words = re.findall('', words)


    def __show(self,words):
        print(words)

    def go(self):
        htmls = self.__fetch_content()
        one_talked = self.__get__one_talk(htmls)
        words = self.__refine(one_talked)
        self.__show(one_talked)

one_talk = OneTalk()
one_talk.go()


# 每个 10 秒打印当前时间。
def timedTask():
    '''
    第一个参数: 延迟多长时间执行任务(单位: 秒)
    第二个参数: 要执行的任务, 即函数
    第三个参数: 调用函数的参数(tuple)
    '''
    Timer(10, one_talk.go, ()).start()

# 定时任务
# def task():
#     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    timedTask()
    # while True:
    #     # print(time.time())
    #     time.sleep(5)
