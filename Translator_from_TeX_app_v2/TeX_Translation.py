from pathlib import Path
import deepl

def TeX_Translation(path_initial,API_KEY):
    path_eng_main = path_initial+r'\English_main.log'
    path_jp_main = path_initial+r'\Japanese_main.log'
    path_eng_sentence = path_initial+r'\English_sentence.log'
    path_jp_sentence = path_initial+r'\Japanese_sentence.log'

    file_path_obj = Path(path_eng_main)
    if not file_path_obj.exists():
        return -1
    file_path_obj = Path(path_eng_sentence)
    if not file_path_obj.exists():
        return -1
    #main
    with open(path_eng_main,'r',encoding="utf-8") as f:
        txt_main = f.read()
    
    #リクエストの最大数がシビアだから、分割して翻訳する。
    lenmax=60000
    lentext=len(txt_main)
    imax=int(lentext/lenmax)
    txt_main_list=[]
    m_ini=0
    i=0
    while i<imax:
        m_fin=txt_main[m_ini:(i+1)*lenmax].rfind('.')+m_ini
        txt_main_list.append(txt_main[m_ini:m_fin+1])
        m_ini=m_fin+1
        i=i+1
    txt_main_list.append(txt_main[m_ini:])

    source_lang = 'EN'
    target_lang = 'JA'

    print("progress (main)")
    # イニシャライズ
    translator = deepl.Translator(API_KEY)
    results=[]
    i=0
    while i<imax+1:
        results.append(translator.translate_text(txt_main_list[i], source_lang=source_lang, target_lang=target_lang))
        print(str(i)+"/"+str(imax))
        i=i+1

    result=""
    i=0
    while i<imax+1:
        result=result+results[i].text
        i=i+1
    with open(path_jp_main, mode='w', encoding='utf-8', newline='\n') as f:
        f.write(result)
    
    #sentence
    with open(path_eng_sentence,'r',encoding="utf-8") as f:
        txt_sentence = f.read()
    #これはリクエストの最大数は超えないとおもうから分割しない。
    #しかし文中にUWXXXXがあってうまく翻訳されないので、それぞれ抽出してばらばらに翻訳。

    num_sentence=len(txt_sentence)
    txt_sentence_list=[]
    m_pst=0
    i=0
    while i<num_sentence:
        FLAG="UW"+str(i+1).zfill(4)
        FLAG_next="UW"+str(i+2).zfill(4)
        m_ini=txt_sentence[m_pst:].find(FLAG)+m_pst
        if m_ini==m_pst-1:
            break
        m_fin=txt_sentence[m_ini+1:].find(FLAG_next)+m_ini+1
        if m_fin==m_ini:
            m_fin=num_sentence#最後まで探索した時
        WORD=txt_sentence[m_ini+7:m_fin-1]
        txt_sentence_list.append(WORD)
        m_pst=m_fin
        i=i+1

    source_lang = 'EN'
    target_lang = 'JA'

    print("progress (sentence)")
    # イニシャライズ
    translator = deepl.Translator(API_KEY)

    #DeepLの仕様上、最大で50分割しかできない
    matsize=i
    imax=int(i/50)
    results=[]
    i=0
    while i<imax:
        results=results+translator.translate_text(txt_sentence_list[i*imax:(i+1)*imax], source_lang=source_lang, target_lang=target_lang)
        print(str(i)+"/"+str(imax))
        i=i+1
    results=results+translator.translate_text(txt_sentence_list[i*imax:], source_lang=source_lang, target_lang=target_lang)

    result=""
    i=0
    while i<matsize:
        FLAG="UW"+str(i+1).zfill(4)
        result=result+FLAG+" "+results[i].text+"\n"
        i=i+1
    with open(path_jp_sentence, mode='w', encoding='utf-8', newline='\n') as f:
        f.write(result)
    
    return 200
