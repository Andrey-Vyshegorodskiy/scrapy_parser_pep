import datetime as dt

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    statuses = {}
    total = 0

    def open_spider(self, spider):  # метод нужен при тестировании
        pass

    def process_item(self, item, spider):
        if item.get('status'):
            self.total += 1
            self.statuses[item['status']] = (
                self.statuses.get(item['status'], 0) + 1)
        return item

    def close_spider(self, spider):
        result_dir = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)
        file_path = result_dir / (
            f'status_summary_'
            f'{dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
        )
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status in self.statuses:
                f.write(f'{status},{self.statuses[status]}\n')
            f.write(f'Total,{self.total}\n')
