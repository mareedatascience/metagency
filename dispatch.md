^/station -> list stations
^/station/([0-9]{4,6})/$ -> station information, list products table, nearby stations, climatology

^/station/[0-9]{4,6}/(.*) -> weather element for station. lists products table, station information, nearby stations

^/station/[0-9]{4,6}/(.*)/(.*) -> weather element at reporting frequency. data summary, data download link, charts appropriate for data type, station information, nearby stations

^/station/[0-9]{4,6}/(.*)/(.*)/([json|csv|excel|xls|xlsx|pdf]) -> downloads data in requested format

^/station/[0-9]{4,6}/(.*)/(.*)/codebook -> downloads codebook in pdf format

^/station/[0-9]{4,6}/(.*)/(.*)/holdings -> holdings information for station/wx/freq/

^/station/[0-9]{4,6}/(.*)/(.*)/(/d{4}) -> data for year
^/station/[0-9]{4,6}/(.*)/(.*)/(/d{4}-/d{2}) -> data for month
^/station/[0-9]{4,6}/(.*)/(.*)/(/d{4}-/d{2}-/d{2}) -> data for day
^/station/[0-9]{4,6}/(.*)/(.*)/(/d{4}-/d{2}-/d{2})/(/d{4}-/d{2}-/d{2}) -> data for date range

