import base64
import os
import requests as req
from  slugify import slugify

import config
import cred


class Filelist():
    def __init__(self):
        self.url = 'https://filelist.io/api.php'
        self.con = None
        self.credentials = cred.credentials
        self.params={
            'action':'latest-torrents',
            'category':'11',
            'sort':'1',
            'limit':'1'
            }
        self.rezults=None
        self.saveDir="temp"
        self._testDestinationFolder(self.params['category'])
    def connect(self):
        headers = {
                "Authorization": "Basic:{}".format(str(base64.b64encode(cred.credentials.encode("utf-8")), 'utf-8'))
            }
        self.con  =req.get(self.url, headers=headers, params=self.params)
        if self.con.status_code == 200:
            self.rezults=self.con.json()
        print(self.con)
    def getTorrentKeys(self):
        if self.rezults:
            return self.rezults[0].keys()
    def getListByKey(self,key):
        lista=[]
        if self.rezults:
            for item in self.rezults:
                if  key in item.keys():
                    lista.append(item[key])
        return lista
    def getListNameLink(self):
        dict={}
        if self.rezults:
            for item in self.rezults:
                dict.update({item['name']:item['download_link']})
        return dict
    def getCategory(self):
        return self.params['category']
    def getCategoryName(self):
        return slugify(config.categories[self.getCategory()])
    def setCategory(self,new_categ):
        new_categ=str(new_categ)
        if new_categ in config.categories and str(self.getCategory()) != new_categ:
            self.params['category']=new_categ
            self._testDestinationFolder(self.getCategory())
            self.connect()
            print("category changed")
        else:
            print("category stay as it is")
    def _testDestinationFolder(self,category):
        tmpdir = os.path.join(self.saveDir, slugify(config.categories[category]))
        if not os.path.isdir(os.path.join(os.getcwd(), tmpdir)):
            print("{} created".format(slugify(config.categories[category])))
            return os.makedirs(os.path.join(os.getcwd(), tmpdir), exist_ok=True)
        return False


    def _test_FileExists(self,fileName):
        nume=os.path.join(os.getcwd(),fileName)
        return os.path.isfile(nume)
    def _save_File(self,nume,content):
        with open(nume, 'wb') as f:
            f.write(content)
    def saveTorrentsList(self):
        lista = self.getListNameLink()
        for nume,contenut in lista.items():
            tmpdir = os.path.join(self.saveDir, slugify(config.categories[self.getCategory()]))
            new_name = "{}.torrent".format(os.path.join(tmpdir, nume))
            if not self._test_FileExists(new_name):
                r = req.get(contenut)

                self._save_File(new_name,r.content)
    def _dirByCateg(self):
        return os.path.join(self.saveDir, slugify(config.categories[self.params['category']]))
    def testUpdated(self):
        lista={}
        if self.rezults:
            for item in self.rezults:

                numeFile = '{}{}{}.torrent'.format(self._dirByCateg(), os.path.sep, item['name'])
                if not self._test_FileExists(numeFile):
                    lista.update({numeFile:item['download_link']})
        return lista
    def getSavedFiles(self):
        if self._dirByCateg():
            return os.listdir(self._dirByCateg())
        return None
    def getSavedCategories(self):
        subfolders = [f.name for f in os.scandir(self.saveDir) if f.is_dir()]
        return subfolders