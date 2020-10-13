import MeCab
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def analyze(fname):
    mecab = MeCab.Tagger('-Ochasen')

    # 品詞を格納するリスト
    words = []

    with open(fname, 'r', encoding='utf-8') as f:
        # テキストファイルを一行毎のリストに変換
        line = f.readline()

        while line:
            node = mecab.parseToNode(line)

            while node:
                word_type = node.feature.split(',')[0]

                if word_type in ['名詞']:
                    words.append(node.surface)

                node = node.next

            line = f.readline()

    font_path = r'c:\WINDOWS\Fonts\BIZ-UDGothicB.ttc'

    txt = ' '.join(words)

    stop_words = ['https', u'ｈｔｔｐｓ', 'co', u'ちゃん', u'くん', u'さん']

    wordcloud = WordCloud(font_path=font_path,
                          stopwords=set(stop_words),
                          collocations=False,
                          width=2736, height=1824).generate(txt)

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    print('Enter the file path of the file you want to analyze')
    fname = input()

    analyze(fname)