from pathlib import Path

def TeX_Decode(path_initial):
    path_SWT = path_initial+r'\English_SWT.log'
    path_sentence = path_initial+r'\Japanese_sentence.log'
    path_main = path_initial+r'\Japanese_main.log'
    path_ans = path_initial+r'\Japanese_first.tex'

    file_path_obj = Path(path_main)
    if not file_path_obj.exists():
        return -1
    file_path_obj = Path(path_SWT)
    if not file_path_obj.exists():
        return -1
    file_path_obj = Path(path_sentence)
    if not file_path_obj.exists():
        return -1
    s=""
    with open(path_main,'r',encoding="utf-8") as f:
        s = f.read()
    num=len(s)
    s_swt=""
    with open(path_SWT,'r',encoding="utf-8") as f:
        s_swt = f.read()
    num_swt=len(s_swt)
    s_sentence=""
    with open(path_sentence,'r',encoding="utf-8") as f:
        s_sentence = f.read()
    num_sentence=len(s_sentence)

    #UWXXXXをs_sentenceからs_swtに置換
    m_pst=0
    i=0
    while i<num_sentence:
        FLAG="UW"+str(i+1).zfill(4)
        FLAG_next="UW"+str(i+2).zfill(4)
        m_ini=s_sentence[m_pst:].find(FLAG)+m_pst
        if m_ini==m_pst-1:
            break
        m_fin=s_sentence[m_ini+1:].find(FLAG_next)+m_ini+1
        if m_fin==m_ini:
            m_fin=num_sentence#最後まで探索した時
        WORD=s_sentence[m_ini+7:m_fin-1]
        s_swt=s_swt.replace(FLAG, WORD)
        m_pst=m_fin
        i=i+1

    #main
    m_ini_doc=s_swt.find('begin{document}')+15
    s=s_swt[:m_ini_doc]+s

    for j in range(2):
        m_pst=0
        i=0
        while i<num_swt:
            FLAG="SW"+str(i+1).zfill(4)
            FLAG_next="SW"+str(i+2).zfill(4)
            m_ini=s_swt[m_pst:].find(FLAG)+m_pst
            if m_ini==m_pst-1:
                break
            m_fin=s_swt[m_ini+1:].find(FLAG_next)+m_ini+1
            if m_fin==m_ini:
                m_fin=s_swt[m_ini+1:].find("end{document}")+m_ini+1#最後まで探索した時
            WORD=s_swt[m_ini+6:m_fin-1]
            s=s.replace(FLAG, WORD)
            m_pst=m_fin
            i=i+1

    s=s+s_swt[m_fin-1:]

    with open(path_ans, mode='w', encoding='utf-8', newline='\n') as f:
        f.write(s)
