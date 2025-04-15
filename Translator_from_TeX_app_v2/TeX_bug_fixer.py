from pathlib import Path

def TeX_bug_fixer(path_initial,filename_in):
    path = path_initial+'\\'+filename_in
    path_ans = path_initial+'\\'+"English_2.tex"

    file_path_obj = Path(path)
    if not file_path_obj.exists():
        return -1
    s=""
    with open(path,'r',encoding="utf-8") as f:
        s = f.read()
    num=len(s)
    m_ini_doc=s.find('begin{document}')+15

    #align 環境に\tagがあって動かないので、分割してそれぞれの式として独立させる。

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{align*}')+m_pst
        if m_ini==m_pst-1:
            break
        m_fin=s[m_ini:].find('\\end{align*}')+m_ini
        j=0
        while j<1000:
            separate_num=s[m_ini:m_fin].find('\\\\')+m_ini
            if separate_num!=m_ini-1:
                tag_num_ini=s[m_ini:separate_num].find('\\tag')+m_ini
                if tag_num_ini==m_ini-1:
                    tag_word=""
                    tag_num_ini=separate_num
                else:
                    tag_word=s[tag_num_ini:separate_num]
                WORD='\n\\end{align*}'+tag_word+'\n\\end{equation*}\n\\begin{equation*}\n\\begin{align*}'
                s=s[:tag_num_ini]+WORD+s[separate_num+2:]
                m_ini=separate_num+2+len(WORD)-separate_num+tag_num_ini
                m_fin=m_fin+2+len(WORD)-separate_num+tag_num_ini
            else:
                m_pst=m_fin
                break
            j=j+1
        i=i+1

    s=s.replace('align*','aligned')

    with open(path_ans, mode='w', encoding='utf-8', newline='\n') as f:
        f.write(s)
