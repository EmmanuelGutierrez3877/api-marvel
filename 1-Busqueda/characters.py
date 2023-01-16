import requests
from flask import Response

apikey ="ts=1&apikey=71f0282cf32da26c7f3327b6d81c40d8&hash=6158fd49a08d763ed9268a77697e5918"

def searchCharacter(name = None, filtro = None):
    resultados = []

    if (name == None):
        page = "https://gateway.marvel.com:443/v1/public/characters?orderBy=name&limit=100&{}".format(apikey)
        r = (requests.get(page)).json()
        r = r['data']['results']
        for x in r:
            #print(x['name'])
            resultados.append({
                'id': x['id'],
                'name': x['name'],
                'image': get_urlImage(x),
                'apperances': get_apperances(x)
            })

    elif (name != None):
        if (filtro == None or filtro == "1"):
            page = "https://gateway.marvel.com:443/v1/public/characters?nameStartsWith={}&limit=100&{}".format(name,apikey)
            r = (requests.get(page)).json()
            r = r['data']['results']
            for x in r:
                #print(x['name'])
                resultados.append({
                    'id': x['id'],
                    'name': x['name'],
                    'image': get_urlImage(x),
                    'apperances': get_apperances(x)
                })

        if (filtro == None or filtro == "2"):
            page2 = "https://gateway.marvel.com:443/v1/public/comics?titleStartsWith={}&limit=100&{}".format(name,apikey)
            r = (requests.get(page2)).json()
            r = r['data']['results']
            for x in r:
                resultados.append({
                    'id': x['id'],
                    'title': x['title'],
                    'image': get_urlImage(x),
                    'onSaleDate': get_onsaleDate(x)
                })
        
        if (filtro != None and filtro != "1" and filtro != "2"):
            return Response( "filtro invalido", status=400,)

    resultados.sort(key=get_name)
    #for x in resultados:
        #print(x)
    #print(len(resultados))
    return resultados

def get_name(reg):
    if ('name' in reg):
        return reg['name']
    elif('title' in reg):
        return reg['title']
    return None

def get_onsaleDate(reg):
    res = None
    for x in reg['dates']:
        if x['type'] == 'onsaleDate':
            res = x['date']
    return res

def get_urlImage(reg):
    
    if ('images' in reg):
        if (len(reg['images']) > 0):
            return reg['images'][0]['path']+"."+reg['images'][0]['extension']
        return ""

    elif ('thumbnail' in reg):
        return reg['thumbnail']['path']+"."+reg['thumbnail']['extension']

    return None

def get_apperances(reg):
    count = 0
    if ('comics' in reg):
        count += reg['comics']['available']
    if ('series' in reg):
        count += reg['series']['available']
    if ('stories' in reg):
        count += reg['stories']['available']
    if ('events' in reg):
        count += reg['events']['available']
    return count