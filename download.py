import os
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from nsepy import get_history

from configs.config import indices
from utils.util import update_progress

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.float_format', lambda x: '%.4f' % x)

app = Flask(__name__)


@app.route('/download', methods=('GET', 'POST'))
def create():
    # print(request.method)
    # print("INSIDE CREATE ROUTE")
    if request.method == 'POST':
        indice = request.form['indices'].upper()
        start = request.form['start']
        end = request.form['end']
        display = request.form['display'].lower()
        download = request.form['download'].lower()

        # print(indice)
        # print(display)

        try:
            todays_date = datetime.now()

            if datetime.strptime(start, '%Y-%m-%d') > todays_date or \
                    datetime.strptime(end, '%Y-%m-%d') > todays_date:
                return render_template('download.html', data="**Please check Start Date: {} and End Date: {}. "
                                                             "Start Date and End Date can not be greater than Today's "
                                                             "Date: {}"
                                       .format(start, end, todays_date.strftime('%Y-%m-%d')))

            start_year = int(start.split('-')[0])
            start_month = int(start.split('-')[1].lstrip('0'))
            start_date = int(start.split('-')[2].lstrip('0'))

            # print(start_year, start_month, start_date)

            end_year = int(end.split('-')[0])
            end_month = int(end.split('-')[1].lstrip('0'))
            end_date = int(end.split('-')[2].lstrip('0'))

            # print(end_year, end_month, end_date)

            dataframe_list = []
            data_concat = None

            sorted_indices = sorted(indices.get(indice))
            sorted_indices_len = len(sorted_indices)
            progress_counter = 1

            for stock in sorted_indices:
                data = get_history(symbol=stock,
                                   start=datetime(start_year, start_month, start_date),
                                   end=datetime(end_year, end_month, end_date))
                dataframe_list.append(data)
                # print("Added '{}' to the list".format(stock))
                update_progress(progress_counter, sorted_indices_len)
                progress_counter = progress_counter + 1

            print()
            if dataframe_list:
                data_concat = pd.concat(dataframe_list)

            data_concat.index.name = data_concat.index.name.replace(' ', '_').lower()
            data_concat.columns = list(
                map(lambda x: x.lower().replace(' ', '_').replace('%', 'percent_'), data_concat.columns.values))

        except ValueError as VE:
            return render_template('download.html', data=VE)

        if data_concat is None or data_concat.empty:
            return render_template('download.html', data="**No Record found for indice {}".format(indice))

        elif data_concat is not None and not data_concat.empty:
            # print(data)
            data_concat.reset_index(level=0, inplace=True)
            data_concat.index = np.arange(1, len(data_concat) + 1)
            if display == 'yes' and download == 'yes':
                download_loc = str(os.path.join(Path.home(), 'Downloads/{}.csv'.format(indice)))
                data_concat.to_csv(download_loc, index=False)

                if data_concat.shape[0] > 1000:
                    data_concat = data_concat.head(1000)

                return render_template('download.html', download_loc=download_loc,
                                       data=data_concat.to_html(classes=["table", "table-striped", "table-hover"],
                                                                index=False, justify='center'))
            elif display == 'yes':
                return render_template('download.html',
                                       data=data_concat.to_html(classes=["table", "table-striped", "table-hover"],
                                                                index=False, justify='center'))
            elif download == 'yes':
                download_loc = str(os.path.join(Path.home(), 'Downloads/{}.csv'.format(indice)))
                data_concat.to_csv(download_loc, index=False)

                return render_template('download.html', download_loc=download_loc)
        else:
            pass
            # TODO

    return render_template('download.html', data="")


if __name__ == '__main__':
    app.run(debug=False)
