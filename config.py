
categories={
"1" :"Filme SD",
" 2":"Filme DVD",
"3" :"Filme DVD-RO",
" 4":"Filme HD",
"5" :"FLAC",
"6 " :"Filme 4K",
"7":" XXX",
"8":"Programe",
"9":"Jocuri PC",
"10" :"Jocuri Console",
"11" :"Audio",
"12" :"Videoclip",
"13" :"Sport",
"14" :"TV",
"15" :"Desene",
"16" :"Docs",
"17" :"Linux",
"18" :"Diverse",
"19" :"Filme HD-RO",
"20" :"Filme Blu-Ray",
"21" :" Seriale HD",
"22" :"Mobile",
"23" :"Seriale SD",
"24" :"Anime",
"25" :"Filme 3D",
"26" :"Filme 4K Blu-Ray",
"27" :"Seriale 4K"
}
erori={
    400:'Invalid search/filter',
    401 :'Username and passkey cannot be empty',
    403 :' Too many failed authentications',
    403 :' Invalid passkey/username',
    404 :' No results',
    429 :' Rate limit reached',
    503 :' Service unavaible'
}
filme=['mp4','avi','mkv']



params = {
        'action':'latest-torrents',
        'category':'',
        'sort':'1',
        'limit':'10'
    }