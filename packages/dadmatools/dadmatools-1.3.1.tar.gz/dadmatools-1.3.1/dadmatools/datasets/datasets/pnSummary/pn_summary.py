import csv
import io
import json
import os
from dadmatools.datasets.base import BaseDataset, DatasetInfo
from dadmatools.datasets.dataset_utils import download_dataset, is_exist_dataset, DEFAULT_CACHE_DIR, unzip_dataset

URL = 'https://drive.google.com/uc?id=16OgJ_OrfzUF_i3ftLjFn9kpcyoi7UJeO'
DATASET_NAME = "PnSummary"

def PnSummary(dest_dir=DEFAULT_CACHE_DIR):
    base_addr = os.path.dirname(__file__)
    info_addr = os.path.join(base_addr, 'info.py')
    DATASET_INFO = json.load(open(info_addr))
    dest_dir = os.path.join(dest_dir, DATASET_NAME)

    def get_pn_summary_item(dir_addr, fname):
        f_addr = os.path.join(dir_addr, fname)
        keys = ['id', 'title', 'article', 'summary', 'category', 'categories', 'network']
        with io.open(f_addr, encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:

                item = row[0].split('\t')
                try:
                    yield {k:item[i] for i,k in enumerate(keys)}
                except :
                    continue

    if not is_exist_dataset(DATASET_INFO, dest_dir):
        downloaded_file = download_dataset(URL, dest_dir)
        dest_dir = unzip_dataset(downloaded_file, dest_dir, zip_format='zip')
    info = DatasetInfo(info_addr=info_addr)
    train_iterator = get_pn_summary_item(dest_dir, 'pn_summary/train.csv')
    test_iterator = get_pn_summary_item(dest_dir, 'pn_summary/test.csv')
    dev_iterator = get_pn_summary_item(dest_dir, 'pn_summary/dev.csv')
    sizes = DATASET_INFO['size']
    train_dataset = BaseDataset(train_iterator, info, num_lines=sizes['train'])
    test_dataset = BaseDataset(test_iterator, info, num_lines=sizes['test'])
    dev_dataset = BaseDataset(dev_iterator, info, num_lines=sizes['dev'])
    return {'train':train_dataset, 'test':test_dataset, 'dev':dev_dataset}

