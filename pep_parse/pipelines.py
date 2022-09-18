import collections
import csv
import datetime as dt

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def __init__(self):
        self.result_dir = BASE_DIR / 'results'
        self.result_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = collections.defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_path = self.result_dir / (
            f'status_summary_'
            f'{dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
        )
        with open(file_path, 'w', encoding='utf-8') as f:
            csv_writer = csv.writer(
                f,
                delimiter=';',
                quoting=csv.QUOTE_NONE,
                lineterminator='\n'
            )
            csv_writer.writerows([
                ['Статус,Количество'],
                *self.statuses.items(),
                ['Total', sum(self.statuses.values())]
            ])
