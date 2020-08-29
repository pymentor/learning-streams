import csv
from datetime import datetime, timedelta


with open("ZUO.csv") as csvfile_in, open("ZUO_out.csv", mode="w", newline="") as csvfile_out:
    rows = csv.reader(csvfile_in, delimiter=',', quotechar='|')

    column_names_row = []
    tmp = {}

    # convert rows object to dict
    for row in rows:
        if rows.line_num == 1:
            # save columns names
            column_names_row = row
            continue

        date_str = row[0]
        open_price = row[1]
        high_price = row[2]
        low_price = row[3]
        close_price = row[4]
        adj_close_price = row[5]
        volume = row[6]

        date_dt = datetime.strptime(date_str, "%Y-%m-%d")
        date_dt_3_days_ago = date_dt - timedelta(days=3)

        tmp[date_dt] = [
            date_dt_3_days_ago,
            open_price,
            high_price,
            low_price,
            float(close_price),
            adj_close_price,
            volume
        ]

    # write columns names to result csv file
    csv_writer = csv.writer(csvfile_out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    column_names_row.append("Ratio")
    csv_writer.writerow(column_names_row)

    # iterate over tmp dict and calculate ratio value for each day if possible
    for current_dt, data in tmp.items():
        ratio = "-/-"

        dt_3_days_ago = data[0]
        open_price = data[1]
        high_price = data[2]
        low_price = data[3]
        close_price = data[4]
        adj_close_price = data[5]
        volume = data[6]

        try:
            close_price_3_days_ago = tmp[dt_3_days_ago][4]
            ratio = round(close_price / close_price_3_days_ago, 5)
        except KeyError:
            # there is no some dates in the file and we can't get "3 days ago" date for some dates
            pass

        # write calculated ratio value to result csv file
        csv_writer.writerow(
            [
                current_dt.strftime("%Y-%m-%d"),
                open_price,
                high_price,
                low_price,
                close_price,
                adj_close_price,
                volume,
                ratio
            ]
        )
