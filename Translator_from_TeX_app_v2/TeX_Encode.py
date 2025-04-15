from pathlib import Path

def TeX_Encode(path_initial,footnotetextflag):
    path = path_initial+r'\English_2.tex'
    path_SWT = path_initial+r'\English_SWT.log'
    path_sentence=path_initial+r'\English_sentence.log'
    path_main = path_initial+r'\English_main.log'

    file_path_obj = Path(path)
    if not file_path_obj.exists():
        return -1
    s=""
    with open(path,'r',encoding="utf-8") as f:
        s = f.read()
    num=len(s)

    m_ini_doc=s.find('begin{document}')+15

    s_swt=""
    s_swt=s[:m_ini_doc]

    #$$の書き方が嫌いなので、equation環境に置き換える
    i=0
    k=1
    m_pst=m_ini_doc
    while i<num:
        m=s[m_pst:].find('$$')+m_pst
        if m==m_pst-1:
            break
        if k==1:
            s=s[:m]+'\\begin{equation*}'+s[m+2:]
            m_pst=m+16
        else:
            s=s[:m]+'\\end{equation*}'+s[m+2:]
            m_pst=m+14
        k=-k
        i=i+1

    COUNT=1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{tabular*}')+m_pst
        if m_ini==m_pst-1:
            break
        m_fin=s[m_ini:].find('\\end{tabular*}')+m_ini
        m_ini_pst=m_ini
        j=0
        while j <100:
            m_overlapp=s[m_ini_pst+16:m_fin].find('\\begin{tabular*}')+m_ini_pst+16
            if m_overlapp==m_ini_pst+15:
                break
            m_ini_pst=m_overlapp
            m_fin=s[m_fin+14:].find('\\end{tabular*}')+m_fin+14
            j=j+1
        WORD=s[m_ini:m_fin+14]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+14:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{tabular}')+m_pst
        if m_ini==m_pst-1:
            break
        m_fin=s[m_ini:].find('\\end{tabular}')+m_ini
        m_ini_pst=m_ini
        j=0
        while j <100:
            m_overlapp=s[m_ini_pst+15:m_fin].find('\\begin{tabular}')+m_ini_pst+15
            if m_overlapp==m_ini_pst+14:
                break
            m_ini_pst=m_overlapp
            m_fin=s[m_fin+13:].find('\\end{tabular}')+m_fin+13
            j=j+1
        WORD=s[m_ini:m_fin+13]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+13:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    #文中の式を抽出・s_swtに移す。代わりにSWXXXXに置き換える
    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('$')+m_pst
        m_fin=s[m_ini+1:].find('$')+m_ini+1
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+1]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+1:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{equation*}')+m_pst
        m_fin=s[m_ini:].find('\\end{equation*}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+15]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+15:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{equation}')+m_pst
        m_fin=s[m_ini:].find('\\end{equation}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+14]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+14:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{aligned}')+m_pst
        m_fin=s[m_ini:].find('\\end{aligned}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+13]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+13:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{aligned*}')+m_pst
        m_fin=s[m_ini:].find('\\end{aligned*}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+14]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+14:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{align}')+m_pst
        m_fin=s[m_ini:].find('\\end{align}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+11]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+11:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{align*}')+m_pst
        m_fin=s[m_ini:].find('\\end{align*}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+12]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+12:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{gather*}')+m_pst
        m_fin=s[m_ini:].find('\\end{gather*}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+13]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+13:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{gather}')+m_pst
        m_fin=s[m_ini:].find('\\end{gather}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+12]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+12:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\[')+m_pst
        m_fin=s[m_ini:].find('\\]')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+2]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+2:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{figure*}')+m_pst
        m_fin=s[m_ini:].find('\\end{figure*}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+13]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+13:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{figure}')+m_pst
        m_fin=s[m_ini:].find('\\end{figure}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+12]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+12:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{center}')+m_pst
        m_fin=s[m_ini:].find('\\end{center}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+12]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+12:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{center*}')+m_pst
        m_fin=s[m_ini:].find('\\end{center*}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+13]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+13:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\includegraphics')+m_pst
        m_fin=s[m_ini:].find('}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+1]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+1:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\section')+m_pst
        m_fin=s[m_ini:].find('}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+1]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+1:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\subsection')+m_pst
        m_fin=s[m_ini:].find('}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+1]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+1:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\href')+m_pst
        m_fin=s[m_ini:].find('}')+m_ini
        if m_ini==m_pst-1:
            break
        if s[m_fin+1]=='{':
            m_fin=s[m_fin+1:].find('}')+m_fin+1
        WORD=s[m_ini:m_fin+1]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+1:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\footnotetext')+m_pst
        m_fin=s[m_ini:].find('}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+1]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+1:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\maketitle')+m_pst
        m_fin=m_ini+10
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{abstract}')+m_pst
        m_fin=m_ini+16
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\end{abstract}')+m_pst
        m_fin=m_ini+14
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{enumerate}')+m_pst
        m_fin=s[m_ini:].find('\\end{enumerate}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+15]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+15:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{itemize}')+m_pst
        m_fin=s[m_ini:].find('\\end{itemize}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+13]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+13:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{array}')+m_pst
        m_fin=s[m_ini:].find('\\end{array}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+11]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+11:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{verbatim}')+m_pst
        m_fin=s[m_ini:].find('\\end{verbatim}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+16]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+16:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=m_ini_doc
    i=0
    while i<num:
        m_ini=s[m_pst:].find('\\begin{verbatim*}')+m_pst
        m_fin=s[m_ini:].find('\\end{verbatim*}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s[m_ini:m_fin+17]
        FLAG="SW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s=s[:m_ini]+FLAG+s[m_fin+17:]
        s_swt=s_swt+FLAG+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    #s_swtに残っている文章を抜き出して、s_sentenceに書く。かわりにUWXXXXに置き換える。
    s_sentence=""
    COUNT=1
    num2=len(s_swt)
    m_pst=0
    i=0
    while i<num2:
        m_ini=s_swt[m_pst:].find('\\item')+m_pst
        m_fin=s_swt[m_ini+5:].find('\n')+m_ini+5
        if m_ini==m_pst-1:
            break
        WORD=s_swt[m_ini+6:m_fin]
        FLAG="UW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s_swt=s_swt[:m_ini+6]+FLAG+s_swt[m_fin:]
        s_sentence=s_sentence+FLAG+" "+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=0
    i=0
    while i<num2:
        m_ini=s_swt[m_pst:].find('\\section')+m_pst
        m_ini2=s_swt[m_ini:].find('{')+m_ini
        m_fin=s_swt[m_ini2:].find('}')+m_ini2
        if m_ini==m_pst-1:
            break
        WORD=s_swt[m_ini2+1:m_fin]
        FLAG="UW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s_swt=s_swt[:m_ini2+1]+FLAG+s_swt[m_fin:]
        s_sentence=s_sentence+FLAG+" "+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=0
    i=0
    while i<num2:
        m_ini=s_swt[m_pst:].find('\\subsection')+m_pst
        m_ini2=s_swt[m_ini:].find('{')+m_ini
        m_fin=s_swt[m_ini2:].find('}')+m_ini2
        if m_ini==m_pst-1:
            break
        WORD=s_swt[m_ini2+1:m_fin]
        FLAG="UW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s_swt=s_swt[:m_ini2+1]+FLAG+s_swt[m_fin:]
        s_sentence=s_sentence+FLAG+" "+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    m_pst=0
    i=0
    while i<num2:
        m_ini=s_swt[m_pst:].find('\\title{')+m_pst
        m_fin=s_swt[m_ini:].find('}')+m_ini
        if m_ini==m_pst-1:
            break
        WORD=s_swt[m_ini+7:m_fin]
        FLAG="UW"+str(COUNT).zfill(4)
        COUNT=COUNT+1
        s_swt=s_swt[:m_ini+7]+FLAG+s_swt[m_fin:]
        s_sentence=s_sentence+FLAG+" "+WORD+"\n"
        m_pst=m_fin+len(FLAG)-len(WORD)
        i=i+1

    if footnotetextflag==True:
        m_pst=m_ini_doc
        i=0
        while i<num2:
            m_ini=s_swt[m_pst:].find('\\footnotetext')+m_pst
            m_ini2=s_swt[m_ini:].find('{')+m_ini
            m_fin=s_swt[m_ini2:].find('}')+m_ini2
            if m_ini==m_pst-1:
                break
            WORD=s_swt[m_ini2+1:m_fin]
            FLAG="UW"+str(COUNT).zfill(4)
            COUNT=COUNT+1
            s_swt=s_swt[:m_ini2+1]+FLAG+s_swt[m_fin:]
            s_sentence=s_sentence+FLAG+" "+WORD+"\n"
            m_pst=m_fin+len(FLAG)-len(WORD)
            i=i+1

    m_fin_doc=s.find('\\end{document}')
    s_swt=s_swt+s[m_fin_doc:]
    s=s[m_ini_doc:m_fin_doc]

    with open(path_SWT, mode='w', encoding='utf-8', newline='\n') as f:
        f.write(s_swt)
    with open(path_main, mode='w', encoding='utf-8', newline='\n') as f:
        f.write(s)
    with open(path_sentence, mode='w', encoding='utf-8', newline='\n') as f:
        f.write(s_sentence)
