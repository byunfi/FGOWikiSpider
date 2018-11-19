#!/usr/bin/python3
# -*- coding: utf-8 -*-

import fgo_file_manager as fm
import json

MST_SVT: list
MST_SVT_SKILL: list
COLLECTION_NO2ID = {}


def a():
    with open(fm.JSON_DIR + "/mstSvt.json", "r", encoding='utf-8') as mst_svt_f:
        mst_svt: [dict] = json.loads(mst_svt_f.read())
        global MST_SVT
        MST_SVT = list(filter(lambda x: x["cvId"] and x["collectionNo"], mst_svt))
        MST_SVT.sort(key=lambda x: x["collectionNo"])
        for item in MST_SVT:
            COLLECTION_NO2ID[item["collectionNo"]] = item["id"]

    with open(fm.JSON_DIR + "/mstSvtSkill.json", "r", encoding='utf-8') as mst_svt_skill_f:
        global MST_SVT_SKILL
        MST_SVT_SKILL = json.loads(mst_svt_skill_f.read())


a()
print(COLLECTION_NO2ID)
for i in range(1, 255):
    id = COLLECTION_NO2ID[i]
    print(id)
    for item in MST_SVT_SKILL:
        if item["svtId"] == id:
            print("--", item["num"], item["skillId"], item["strengthStatus"])
