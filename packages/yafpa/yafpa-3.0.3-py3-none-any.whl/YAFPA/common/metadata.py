import os
import re
from datetime import datetime
from pathlib import Path

import frontmatter

from YAFPA.common import global_value as settings

BASEDIR = Path(settings.BASEDIR)
web = settings.web


def remove_frontmatter(meta):
    meta.pop("title", None)
    meta.pop("update", None)
    meta.pop("link", None)
    meta.pop("date", None)
    return meta


def frontmatter_check(filename, folder):
    metadata = open(Path(f"{folder}/{filename}"), "r", encoding="utf-8")
    meta = frontmatter.load(metadata)
    metadata.close()
    final = open(Path(f"{folder}/{filename}"), "w", encoding="utf-8")
    now = datetime.now().strftime("%d-%m-%Y")
    if not "update" in meta.keys() or (
        "update" in meta.keys() and meta["update"] != False
    ):
        if not "date" in meta.keys():
            meta["date"] = now
    if not "title" in meta.keys():
        meta["title"] = filename.replace(".md", "")
    update = frontmatter.dumps(meta)
    final.write(update)
    final.close()
    return


def update_frontmatter(file, folder, share=0, link=1):
    metadata = open(file, "r", encoding="utf8")
    meta = frontmatter.load(metadata)
    metadata.close()
    folder_key = str(folder).replace(f"{BASEDIR}", "")
    folder_key = folder_key.replace(os.sep, "")
    folder_key = folder_key.replace("_", "")
    share = settings.share
    if "tag" in meta.keys():
        tag = meta["tag"]
    elif "tags" in meta.keys():
        tag = meta["tags"]
    else:
        tag = ""
    meta.metadata.pop("tag", None)
    meta.metadata.pop("tags", None)
    with open(file, "w", encoding="utf-8") as f:
        filename = os.path.basename(file)
        filename = filename.replace(".md", "")
        filename = filename.replace(" ", "-")
        clip = f"{web}{folder_key}/{filename}"
        meta["link"] = clip
        update = frontmatter.dumps(meta, sort_keys=False)
        meta = frontmatter.loads(update)
        if link != 1:
            meta.metadata.pop("link", None)
        elif (
            link == 1
            and share == 1
            and (share not in meta.keys() or meta[share] == "false")
        ):
            meta[share] = "true"
        if tag != "":
            meta["tag"] = tag
        update = frontmatter.dumps(meta, sort_keys=False)
        if re.search(r"\\U\w+", update):
            emojiz = re.search(r"\\U\w+", update)
            emojiz = emojiz.group().strip()
            raw = r"{}".format(emojiz)
            try:
                convert_emojiz = (
                    raw.encode("ascii")
                    .decode("unicode_escape")
                    .encode("utf-16", "surrogatepass")
                    .decode("utf-16")
                )
                update = re.sub(r'"\\U\w+"', convert_emojiz, update)
            except UnicodeEncodeError:
                pass
        f.write(update)
    return
