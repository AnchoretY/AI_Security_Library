# https://xz.aliyun.com/t/2136#toc-14
SQL_pattern = """/select(\s)+|insert(\s)+|update(\s)+|(\s)+and(\s)+|(\s)+or(\s)+|delete(\s)+|\'|\/\*|\*|\.\.\/
        |\.\/|union(\s)+|into(\s)+|load_file(\s)+|outfile(\s)+"""
Webshell_pattern = """(preg_replace.*\/e|`.*?\$.*?`|\bcreate_function\b|\bpassthru\b|\bshell_exec\b|\bexec\b|
        \bbase64_decode\b|\bedoced_46esab\b|\beval\b|\bsystem\b|\bproc_open\b|\bpopen\b|\bcurl_exec\b|\bcurl_multi_exec\b|
        \bparse_ini_file\b|\bshow_source\b|cmd\.exe|KAdot@ngs\.ru|小组专用大马|提权|木马|PHP\s?反弹|shell\s?加强版|
        WScript\.shell|PHP\s?Shell|Eval\sPHP\sCode|Udp1-fsockopen|xxddos|Send\sFlow|fsockopen\('(udp|tcp)|SYN\sFlood)|
        z0|z1|z2|z9|caidao"""
XSS_pattern = """xss|javascript|vbscript|expression|applet|meta|xml|blink|link|style|script|embed|object|
        iframe|frame|frameset|ilayer|layer|bgsound|title|base|onabort|onactivate|onafterprint|onafterupdate|
        onbeforeactivate|onbeforecopy|onbeforecut|onbeforedeactivate|onbeforeeditfocus|onbeforepaste|onbeforeprint|
        onbeforeunload|onbeforeupdate|onblur|onbounce|oncellchange|onchange|onclick|oncontextmenu|oncontrolselect|
        oncopy|oncut|ondataavailable|ondatasetchanged|ondatasetcomplete|ondblclick|ondeactivate|ondrag|ondragend|
        ondragenter|ondragleave|ondragover|ondragstart|ondrop|onerror|onerrorupdate|onfilterchange|onfinish|onfocus|
        onfocusin|onfocusout|onhelp|onkeydown|onkeypress|onkeyup|onlayoutcomplete|onload|onlosecapture|onmousedown|
        onmouseenter|onmouseleave|onmousemove|onmouseout|onmouseover|onmouseup|onmousewheel|onmove|onmoveend|onmovestart|
        onpaste|onpropertychange|onreadystatechange|onreset|onresize|onresizeend|onresizestart|onrowenter|onrowexit|
        onrowsdelete|onrowsinserted|onscroll|onselect|onselectionchange|onselectstart|onstart|onstop|onsubmit|
        onunload(\s)+"""




# 
