from annotations import *
from pprint import pprint


def recursion(children,links,article):
    redirect_flag=0
    for i in children:

        try:
            title = i.title
            article.append('*'+title)
            recursion(i.children, links,article)
        except:

            try:
                para_text = "".join(b.__str__() for b in i.para_bodies)
                para_t = para_text

                if len(para_text) >0:
                    article.append('-'+para_t)


                for para in i.para_bodies:
                    q = para
                    try:
                        n = q.anchor_text.strip()
                        m = q.page.strip()
                        if n[:8]!="Category":
                            if n[:5]!="Image":
                                links.append(n+u"\t"+m)

                    except:
                        pass
            except:
                pass


def section_constructor(corpus,key):
    try:
        ske=corpus.get(key).skeleton
        redirect_entity=[]
        links=[]
        article = []
        recursion(ske,links, article)
        print(key)
        d_dic ={}
        s_t = '*Introduction'
        para = []
        for i in range(len(article)):
            if i!=len(article)-1:
                if article[i][0] == '*':
                    if article[i+1][0] != '*':
                        s_t = article[i]


                else:
                    if article[i+1][0] != '*':
                        para.append(article[i])
                    else:
                        para.append(article[i])
                        d_dic[s_t] = para
                        s_t=''
                        para = []
            else:
                if article[i][0]!='*':
                    para.append(article[i])
                    d_dic[s_t] = para
        # pprint(article)
        print('-'*20)
        pprint(d_dic)
        print('.'*10)
        pprint(links)
        print('.'*10)
        redirect_text_set = {"-#redirect", "-#Redirect" }
        try:

            if d_dic['*Introduction'][0][:10] in redirect_text_set:
                if len(links)!=0:
                    redirected_entity= links[0].split('\t')[1]
                    redirect_entity.append(key)
                    redirect_entity.append(redirected_entity)
            else:
                pass
        except KeyError:
            print("EEEEEEEEEEEEEEEEEEEEEEE" +key)
        for i in redirect_entity:
            print(i)
            print("@"*10)
        print('\n'*3)

        if len(d_dic.keys())!=0:
            d_dic['PAGE_NAME'] = key
            return d_dic
    except AttributeError:
        print "Couldn't fine %s" % key

if __name__ == '__main__':
    global corpus
    e =0
    corpus = AnnotationsFile('combined.cbor')
    for k in corpus.keys()[:1000]:
        if k[:8]!=u"Category":
            if k[:5] != u"Image":
                if k[:8]!=u"Template":
                    if k[:9]!=u"Wikipedia":
                        if k[-3:]!=u"jpg":
                            if k[:4] !=u"Listr":
                                if k[:4] !=u"File":
                                    d = section_constructor(corpus,k)
    pprint(section_constructor(corpus, "List of minor The Hitchhiker's Guide to the Galaxy characters#Fenchurch"))
    print("number of keys (entities entries) is: " + str(len(corpus.keys())))
