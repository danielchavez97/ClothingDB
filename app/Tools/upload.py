import urllib.request
import uuid
import boto3
import progressbar
from app.models import *
from app import db


def func():
    with open('data.json', 'r') as f:
        data = json.load(f)

    session = boto3.Session()
    s3 = session.resource('s3')
    bucket_name = 'cf-simple-s3-origin-db-556603787203'
    objs = []

    bar = progressbar.ProgressBar(maxval=len(data),
                                  widgets=[progressbar.Bar('*', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()

    for i in range(len(data)):
        entry = data[str(i)]
        name = entry['name']
        brand_name = entry['brand']
        filename = str(uuid.uuid4()) + '.jpg'
        objs.append(Item(name=name, brand_name=brand_name, thumbnails=[Thumbnail(filename=filename)]))
        try:
            url = entry['img_src']
            # upload image to s3
            with urllib.request.urlopen(url) as f:
                bucket = s3.Bucket(bucket_name)
                bucket.upload_fileobj(f, filename)
        except:
            with open('log.json', 'w') as f:
                json.dumps({'entry': entry})
            break

        bar.update(i + 1)

    with open('objs.txt', 'w') as f:
        for item in objs:
            f.write("%s\n" % item)

    print('adding to db')
    db.session.add_all(objs)
    db.session.commit()
    bar.finish()
