def get_qinghua_by_page(page_no):
    offset = page_no * 10
    url = "<topic_url>&limit=10&offset={}".format(offset)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X  10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/69.0.3497.100 Safari/537.36",
    }
    r = requests.get(url, verify=False, headers=headers)
    content = r.content.decode("utf-8")
    data = json.loads(content)
    is_end = data["paging"]["is_end"]
    items = data["data"]
    client = pymongo.MongoClient()
    db = client["qinghua"]
    if len(items) > 0:
        db.answers.insert_many(items)
    return is_end


def get_qinghua():
    page_no = 0
    client = pymongo.MongoClient()
    db = client["qinghua"]
    while True:
        print(page_no)
        is_end = get_qinghua_by_page(page_no)
        page_no += 1
        if is_end:
            break 