import re
from pathlib import Path

def TeX_replace(path_initial,path_ans2):
    path_ans1 = path_initial+r'\Japanese_first.tex'

    file_path_obj = Path(path_ans1)
    if not file_path_obj.exists():
        return -1
    with open(path_ans1,'r',encoding="utf-8") as f:
        s2 = f.read()

    #\\includegraphics関連
    r2=re.findall("\\\\includegraphics", s2)
    m2=[m2.span() for m2 in re.finditer("\\\\includegraphics", s2)]
    num=len(r2)

    x_ini=0
    for i in range(num):
        m2_ini=s2[x_ini:].find('\\includegraphics')+x_ini
        m2_fin=m2_ini+9
        x_ini=s2[m2_ini:m2_fin+40].find('[')+m2_ini
        x_fin=s2[m2_ini:m2_fin+40].find(']')+m2_ini
        s2=s2[:x_ini+1]+"width=0.8\\linewidth"+s2[x_fin:]

    x_fin=0
    for i in range(num):
        m2_ini=s2[x_fin:].find('\\includegraphics')+x_fin
        m2_fin=m2_ini+9
        x_fin=s2[m2_ini:m2_fin+90].find('}')+m2_ini
        s2=s2[:x_fin]+".jpg"+'}'+'\n'+'\\end{center}'+s2[x_fin+1:]

    x_fin=0
    for i in range(num):
        m2_fin=s2[x_fin:].find('\\includegraphics')+x_fin
        s2=s2[:m2_fin]+'\\begin{center}'+'\n'+s2[m2_fin:]
        x_fin=m2_fin+17

    s2=s2.replace('\\begin{center}\n\\begin{center}','\\begin{center}')
    s2=s2.replace('\\end{center}\n\\end{center}','\\end{center}')

    x_fin=0
    for i in range(num):
        m2_fin=s2[x_fin:].find('\\includegraphics')+x_fin
        m2_ini=s2[:m2_fin].rfind('\\begin{center}')
        s2=s2[:m2_ini]+'\\begin{figure}[H]'+'\n'+s2[m2_ini:]
        x_fin=m2_fin+30

    x_fin=0
    for i in range(num):
        m2_ini=s2[x_fin:].find('\\includegraphics')+x_fin
        m2_fin=s2[m2_ini:].find('\\end{center}')+m2_ini+13
        s2=s2[:m2_fin]+'\\end{figure}'+'\n'+s2[m2_fin:]
        x_fin=m2_fin
    
    #プリアンプルを日本語用に変換
    num=1
    m2_ini=s2.find('\\documentclass')
    m2_fin=s2[m2_ini+10:].find('\n')+m2_ini+10
    s2=s2[:m2_ini]+"\\documentclass[fleqn,dvipdfmx]{jsarticle}"+s2[m2_fin:]

    num=1
    m2_ini=s2.find('\\usepackage{graphicx}')
    m2_fin=s2[m2_ini+10:].find('\n')+m2_ini+10
    s2=s2[:m2_ini]+"\\usepackage{graphicx}\n\\usepackage{here}"+s2[m2_fin:]

    with open(path_ans2, mode='w', encoding='utf-8', newline='\n') as f:
        f.write(s2)
