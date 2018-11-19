#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import root
import requests
import json
import csv

SVT_CSV = "https://docs.google.com/spreadsheets/d/1TMdGNL11ROUcYgOQKmt1ikIIRdb3Y0Aqaqrlk1BE79w/export" \
                    "?format=csv"   # fgo.wiki图鉴csv
RUXI_JS = "http://kazemai.github.io/fgo-vz/common/js/master.js" # 茹西解包JSON
DOMAIN = "https://fgo.wiki/w"
CV = DOMAIN + "/声优一览"
ILLUSTRATOR = DOMAIN + "/画师一览"
CLASS_PASSIVE = DOMAIN + "/技能一览/职阶技能"

DOWNLOADS_DIR = root.get_root_dir() + "/downloads"
SERVANT_HTML_DIR = DOWNLOADS_DIR + "/servant_htmls"
RESOURCE_DIR = DOWNLOADS_DIR + "/resources"
JSON_DIR = RESOURCE_DIR + "/fgo_data"


def download(file_url: str, save_path: str, override=False):
    path, name = os.path.split(save_path)
    if os.path.exists(save_path):
        if override:
            os.remove(save_path)
            print("Existing file '{0}', will be deleted.".format(name))
        else:
            print("Existing file '{0}'".format(name))
            return

    if not os.path.isdir(path):
        os.makedirs(path)

    content = requests.get(file_url).content
    with open(save_path, 'wb') as f:
        if f.write(content):
            print("'{0}' downloaded".format(name))


def decode_fgo_data():
    with open(RESOURCE_DIR + "/fgo_data.json", "r", encoding='utf-8') as f:
        j = json.loads(f.read())
        for key, value in j.items():
            data = json.dumps(value)
            save_path = RESOURCE_DIR + "/fgo_data"
            if not os.path.isdir(save_path):
                os.makedirs(save_path)
            with open("{0}/{1}.json".format(save_path, key), "w") as n:
                if n.write(data):
                    print("'{0}' saved".format(key))


def d():
    svt_csv_path = RESOURCE_DIR + "/svt.csv"
    download(SVT_CSV, svt_csv_path)
    with open(svt_csv_path, encoding='UTF-8-sig') as f:
        svt_csv = list(csv.reader(f))[1:]
        for item in svt_csv:
            collection_no = item[0]
            link_name = item[5]
            file_path = SERVANT_HTML_DIR + "/{0}_{1}.html".format(collection_no.zfill(3), link_name)
            url = DOMAIN + "/" + link_name
            download(url, file_path)

