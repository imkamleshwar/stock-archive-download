indices = {
    'NIFTY500': ['3MINDIA', 'ABB', 'ACC', 'AIAENG', 'APLAPOLLO', 'AUBANK', 'AARTIIND', 'AAVAS', 'ABBOTINDIA',
                 'ADANIGAS', 'ADANIGREEN', 'ADANIPORTS', 'ADANIPOWER', 'ADANITRANS', 'ABCAPITAL', 'ABFRL',
                 'ADVENZYMES', 'AEGISCHEM', 'AFFLE', 'AJANTPHARM', 'AKZOINDIA', 'APLLTD', 'ALKEM', 'ALKYLAMINE',
                 'ALLCARGO', 'AMARAJABAT', 'AMBER', 'AMBUJACEM', 'APOLLOHOSP', 'APOLLOTYRE', 'ARVINDFASN', 'ASAHIINDIA',
                 'ASHOKLEY', 'ASHOKA', 'ASIANPAINT', 'ASTERDM', 'ASTRAZEN', 'ASTRAL', 'ATUL', 'AUROPHARMA',
                 'AVANTIFEED',
                 'DMART', 'AXISBANK', 'BASF', 'BEML', 'BSE', 'BAJAJ-AUTO', 'BAJAJCON', 'BAJAJELEC', 'BAJFINANCE',
                 'BAJAJFINSV',
                 'BAJAJHLDNG', 'BALKRISIND', 'BALMLAWRIE', 'BALRAMCHIN', 'BANDHANBNK', 'BANKBARODA', 'BANKINDIA',
                 'MAHABANK', 'BATAINDIA', 'BAYERCROP', 'BERGEPAINT', 'BDL', 'BEL', 'BHARATFORG', 'BHEL', 'BPCL',
                 'BHARATRAS', 'BHARTIARTL', 'INFRATEL', 'BIOCON', 'BIRLACORPN', 'BSOFT', 'BLISSGVS', 'BLUEDART',
                 'BLUESTARCO', 'BBTC', 'BOMDYEING', 'BOSCHLTD', 'BRIGADE', 'BRITANNIA', 'CARERATING', 'CCL',
                 'CESC',
                 'CRISIL', 'CSBBANK', 'CADILAHC', 'CANFINHOME', 'CANBK', 'CAPLIPOINT', 'CGCL', 'CARBORUNIV',
                 'CASTROLIND', 'CEATLTD', 'CENTRALBK', 'CDSL', 'CENTURYPLY', 'CENTURYTEX', 'CERA', 'CHAMBLFERT',
                 'CHENNPETRO', 'CHOLAHLDNG', 'CHOLAFIN', 'CIPLA', 'CUB', 'COALINDIA', 'COCHINSHIP', 'COLPAL',
                 'CONCOR',
                 'COROMANDEL', 'CREDITACC', 'CROMPTON', 'CUMMINSIND', 'CYIENT', 'DBCORP', 'DCBBANK', 'DCMSHRIRAM',
                 'DLF', 'DABUR', 'DALBHARAT', 'DEEPAKNTR', 'DELTACORP', 'DHANUKA', 'DBL', 'DISHTV', 'DCAL',
                 'DIVISLAB',
                 'DIXON', 'LALPATHLAB', 'DRREDDY', 'EIDPARRY', 'EIHOTEL', 'ESABINDIA', 'EDELWEISS', 'EICHERMOT',
                 'ELGIEQUIP', 'EMAMILTD', 'ENDURANCE', 'ENGINERSIN', 'EQUITAS', 'ERIS', 'ESCORTS', 'ESSELPACK',
                 'EXIDEIND', 'FDC', 'FEDERALBNK', 'FINEORG', 'FINCABLES', 'FINPIPE', 'FSL', 'FORTIS', 'FCONSUMER',
                 'FRETAIL', 'GAIL', 'GEPIL', 'GET&D', 'GHCL', 'GMMPFAUDLR', 'GMRINFRA', 'GALAXYSURF', 'GRSE',
                 'GARFIBRES', 'GICRE', 'GILLETTE', 'GLAXO', 'GLENMARK', 'GODFRYPHLP', 'GODREJAGRO', 'GODREJCP',
                 'GODREJIND', 'GODREJPROP', 'GRANULES', 'GRAPHITE', 'GRASIM', 'GESHIP', 'GREAVESCOT', 'GRINDWELL',
                 'GUJALKALI', 'FLUOROCHEM', 'GUJGASLTD', 'GMDCLTD', 'GNFC', 'GPPL', 'GSFC', 'GSPL', 'GULFOILLUB',
                 'HEG',
                 'HCLTECH', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HFCL', 'HATHWAY', 'HATSUN', 'HAVELLS',
                 'HEIDELBERG',
                 'HERITGFOOD', 'HEROMOTOCO', 'HEXAWARE', 'HSCL', 'HIMATSEIDE', 'HINDALCO', 'HAL', 'HINDCOPPER',
                 'HINDPETRO', 'HINDUNILVR', 'HINDZINC', 'HONAUT', 'HUDCO', 'HDFC', 'ICICIBANK', 'ICICIGI',
                 'ICICIPRULI',
                 'ISEC', 'ICRA', 'IDBI', 'IDFCFIRSTB', 'IDFC', 'IFBIND', 'IFCI', 'IIFL', 'IIFLWAM', 'IRB', 'IRCON',
                 'ITC', 'ITI', 'INDIACEM', 'ITDC', 'IBULHSGFIN', 'IBREALEST', 'IBVENTURES', 'INDIAMART', 'INDIANB',
                 'IEX', 'INDHOTEL', 'IOC', 'IOB', 'IRCTC', 'INDOSTAR', 'INDOCO', 'IGL', 'INDUSINDBK', 'INFIBEAM',
                 'NAUKRI', 'INFY', 'INGERRAND', 'INOXLEISUR', 'INTELLECT', 'INDIGO', 'IPCALAB', 'JBCHEPHARM',
                 'JKCEMENT', 'JKLAKSHMI', 'JKPAPER', 'JKTYRE', 'JMFINANCIL', 'JSWENERGY', 'JSWSTEEL', 'JAGRAN',
                 'JAICORPLTD', 'J&KBANK', 'JAMNAAUTO', 'JINDALSAW', 'JSLHISAR', 'JSL', 'JINDALSTEL', 'JCHAC',
                 'JUBLFOOD', 'JUBILANT', 'JUSTDIAL', 'JYOTHYLAB', 'KPRMILL', 'KEI', 'KNRCON', 'KPITTECH', 'KRBL',
                 'KSB',
                 'KAJARIACER', 'KALPATPOWR', 'KANSAINER', 'KTKBANK', 'KARURVYSYA', 'KSCL', 'KEC', 'KOLTEPATIL',
                 'KOTAKBANK', 'L&TFH', 'LTTS', 'LICHSGFIN', 'LAOPALA', 'LAXMIMACH', 'LTI', 'LT', 'LAURUSLABS',
                 'LEMONTREE', 'LINDEINDIA', 'LUPIN', 'LUXIND', 'MASFIN', 'MMTC', 'MOIL', 'MRF', 'MGL',
                 'MAHSCOOTER',
                 'MAHSEAMLES', 'M&MFIN', 'M&M', 'MAHINDCIE', 'MHRIL', 'MAHLOG', 'MANAPPURAM', 'MRPL', 'MARICO',
                 'MARUTI', 'MFSL', 'METROPOLIS', 'MINDTREE', 'MINDACORP', 'MINDAIND', 'MIDHANI', 'MOTHERSUMI',
                 'MOTILALOFS', 'MPHASIS', 'MCX', 'MUTHOOTFIN', 'NATCOPHARM', 'NBCC', 'NCC', 'NESCO', 'NHPC',
                 'NIITTECH',
                 'NLCINDIA', 'NMDC', 'NTPC', 'NH', 'NATIONALUM', 'NFL', 'NBVENTURES', 'NAVINFLUOR', 'NESTLEIND',
                 'NILKAMAL', 'NAM-INDIA', 'OBEROIRLTY', 'ONGC', 'OIL', 'OMAXE', 'OFSS', 'ORIENTCEM', 'ORIENTELEC',
                 'ORIENTREF', 'PIIND', 'PNBHOUSING', 'PNCINFRA', 'PTC', 'PVR', 'PAGEIND', 'PERSISTENT', 'PETRONET',
                 'PFIZER', 'PHILIPCARB', 'PHOENIXLTD', 'PIDILITIND', 'PEL', 'POLYMED', 'POLYCAB', 'PFC',
                 'POWERGRID',
                 'PRAJIND', 'PRESTIGE', 'PRSMJOHNSN', 'PGHL', 'PGHH', 'PNB', 'QUESS', 'RBLBANK', 'RECLTD', 'RITES',
                 'RADICO', 'RVNL', 'RAIN', 'RAJESHEXPO', 'RALLIS', 'RCF', 'RATNAMANI', 'RAYMOND', 'REDINGTON',
                 'RELAXO',
                 'RELIANCE', 'REPCOHOME', 'SBILIFE', 'SJVN', 'SKFINDIA', 'SRF', 'SADBHAV', 'SANOFI', 'SCHAEFFLER',
                 'SCHNEIDER', 'SIS', 'SEQUENT', 'SFL', 'SCI', 'SHOPERSTOP', 'SHREECEM', 'RENUKA', 'SHRIRAMCIT',
                 'SRTRANSFIN', 'SIEMENS', 'SOBHA', 'SOLARINDS', 'SONATSOFTW', 'SOUTHBANK', 'SPANDANA', 'SPICEJET',
                 'STARCEMENT', 'SBIN', 'SAIL', 'SWSOLAR', 'STRTECH', 'STAR', 'SUDARSCHEM', 'SUMICHEM', 'SPARC',
                 'SUNPHARMA', 'SUNTV', 'SUNDARMFIN', 'SUNDRMFAST', 'SUNTECK', 'SUPRAJIT', 'SUPREMEIND', 'SUZLON',
                 'SWANENERGY', 'SYMPHONY', 'SYNGENE', 'TCIEXP', 'TCNSBRANDS', 'TTKPRESTIG', 'TVTODAY',
                 'TV18BRDCST',
                 'TVSMOTOR', 'TAKE', 'TASTYBITE', 'TATACOMM', 'TCS', 'TATACONSUM', 'TATAELXSI', 'TATAINVEST',
                 'TATAMTRDVR', 'TATAMOTORS', 'TATAPOWER', 'TATASTLBSL', 'TATASTEEL', 'TEAMLEASE', 'TECHM', 'NIACL',
                 'RAMCOCEM', 'THERMAX', 'THYROCARE', 'TIMETECHNO', 'TIMKEN', 'TITAN', 'TORNTPHARM', 'TORNTPOWER',
                 'TRENT', 'TRIDENT', 'TIINDIA', 'UCOBANK', 'UFLEX', 'UPL', 'UJJIVAN', 'UJJIVANSFB', 'ULTRACEMCO',
                 'UNIONBANK', 'UBL', 'MCDOWELL-N', 'VGUARD', 'VMART', 'VIPIND', 'VRLLOG', 'VSTIND', 'VAIBHAVGBL',
                 'VAKRANGEE', 'VTL', 'VARROC', 'VBL', 'VEDL', 'VENKEYS', 'VESUVIUS', 'VINATIORGA', 'IDEA',
                 'VOLTAS',
                 'WABCOINDIA', 'WELCORP', 'WELSPUNIND', 'WESTLIFE', 'WHIRLPOOL', 'WIPRO', 'WOCKPHARMA', 'ZEEL',
                 'ZENSARTECH', 'ZYDUSWELL', 'ECLERX'],

    'NIFTY200': ['ACC', 'AUBANK', 'AARTIIND', 'ABBOTINDIA', 'ADANIGAS', 'ADANIPORTS', 'ADANIPOWER',
                 'ADANITRANS', 'ABCAPITAL', 'ABFRL', 'AJANTPHARM', 'ALKEM', 'AMARAJABAT', 'AMBUJACEM', 'APOLLOHOSP',
                 'APOLLOTYRE', 'ASHOKLEY', 'ASIANPAINT', 'AUROPHARMA', 'DMART', 'AXISBANK', 'BAJAJ-AUTO',
                 'BAJFINANCE',
                 'BAJAJFINSV', 'BAJAJHLDNG', 'BALKRISIND', 'BANDHANBNK', 'BANKBARODA', 'BANKINDIA', 'BATAINDIA',
                 'BERGEPAINT', 'BEL', 'BHARATFORG', 'BHEL', 'BPCL', 'BHARTIARTL', 'INFRATEL', 'BIOCON', 'BBTC',
                 'BOSCHLTD', 'BRITANNIA', 'CESC', 'CADILAHC', 'CANBK', 'CASTROLIND', 'CHOLAFIN', 'CIPLA', 'CUB',
                 'COALINDIA', 'COLPAL', 'CONCOR', 'COROMANDEL', 'CROMPTON', 'CUMMINSIND', 'DLF', 'DABUR',
                 'DALBHARAT',
                 'DIVISLAB', 'LALPATHLAB', 'DRREDDY', 'EDELWEISS', 'EICHERMOT', 'EMAMILTD', 'ENDURANCE', 'ESCORTS',
                 'EXIDEIND', 'FEDERALBNK', 'FORTIS', 'FRETAIL', 'GAIL', 'GMRINFRA', 'GICRE', 'GLENMARK',
                 'GODREJAGRO',
                 'GODREJCP', 'GODREJIND', 'GODREJPROP', 'GRASIM', 'GUJGASLTD', 'GSPL', 'HCLTECH', 'HDFCAMC',
                 'HDFCBANK',
                 'HDFCLIFE', 'HAVELLS', 'HEROMOTOCO', 'HEXAWARE', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR',
                 'HINDZINC',
                 'HUDCO', 'HDFC', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'IDBI', 'IDFCFIRSTB', 'ITC', 'IBULHSGFIN',
                 'IBVENTURES', 'INDHOTEL', 'IOC', 'IRCTC', 'IGL', 'INDUSINDBK', 'NAUKRI', 'INFY', 'INDIGO',
                 'IPCALAB',
                 'JSWENERGY', 'JSWSTEEL', 'JINDALSTEL', 'JUBLFOOD', 'JUBILANT', 'KOTAKBANK', 'L&TFH', 'LTTS',
                 'LICHSGFIN', 'LTI', 'LT', 'LUPIN', 'MRF', 'MGL', 'M&MFIN', 'M&M', 'MANAPPURAM', 'MRPL', 'MARICO',
                 'MARUTI', 'MFSL', 'MINDTREE', 'MOTHERSUMI', 'MPHASIS', 'MUTHOOTFIN', 'NATCOPHARM', 'NHPC',
                 'NIITTECH',
                 'NMDC', 'NTPC', 'NATIONALUM', 'NESTLEIND', 'NAM-INDIA', 'OBEROIRLTY', 'ONGC', 'OIL', 'OFSS',
                 'PIIND',
                 'PNBHOUSING', 'PAGEIND', 'PETRONET', 'PFIZER', 'PIDILITIND', 'PEL', 'POLYCAB', 'PFC', 'POWERGRID',
                 'PRESTIGE', 'PGHH', 'PNB', 'QUESS', 'RBLBANK', 'RECLTD', 'RAJESHEXPO', 'RELIANCE', 'SBILIFE',
                 'SRF',
                 'SHREECEM', 'SRTRANSFIN', 'SIEMENS', 'SBIN', 'SAIL', 'SUNPHARMA', 'SUNTV', 'SYNGENE', 'TVSMOTOR',
                 'TCS', 'TATACONSUM', 'TATAMOTORS', 'TATAPOWER', 'TATASTEEL', 'TECHM', 'RAMCOCEM', 'TITAN',
                 'TORNTPHARM', 'TORNTPOWER', 'TRENT', 'UPL', 'ULTRACEMCO', 'UNIONBANK', 'UBL', 'MCDOWELL-N',
                 'VGUARD',
                 'VBL', 'VEDL', 'IDEA', 'VOLTAS', 'WHIRLPOOL', 'WIPRO', 'ZEEL'],

    'NIFTY_SMALL_CAP_250': ['APLAPOLLO', 'ADVENZYMES', 'AEGISCHEM', 'AFFLE', 'ALKYLAMINE', 'ALLCARGO', 'AMBER',
                            'ARVINDFASN', 'ASAHIINDIA', 'ASHOKA', 'ASTERDM', 'ASTRAZEN', 'AVANTIFEED', 'BASF', 'BEML',
                            'BSE', 'BAJAJCON', 'BAJAJELEC', 'BALMLAWRIE', 'BALRAMCHIN', 'MAHABANK', 'BDL', 'BHARATRAS',
                            'BIRLACORPN', 'BSOFT', 'BLISSGVS', 'BLUESTARCO', 'BOMDYEING', 'BRIGADE', 'CARERATING',
                            'CCL', 'CSBBANK', 'CANFINHOME', 'CAPLIPOINT', 'CGCL', 'CARBORUNIV', 'CEATLTD', 'CDSL',
                            'CENTURYPLY', 'CENTURYTEX', 'CERA', 'CHAMBLFERT', 'CHENNPETRO', 'COCHINSHIP', 'CYIENT',
                            'DBCORP', 'DCBBANK', 'DCMSHRIRAM', 'DEEPAKNTR', 'DELTACORP', 'DHANUKA', 'DBL', 'DISHTV',
                            'DCAL', 'DIXON', 'EIDPARRY', 'ESABINDIA', 'ELGIEQUIP', 'ENGINERSIN', 'EQUITAS', 'ESSELPACK',
                            'FDC', 'FINEORG', 'FINCABLES', 'FINPIPE', 'FSL', 'FCONSUMER', 'GEPIL', 'GET&D', 'GHCL',
                            'GMMPFAUDLR', 'GALAXYSURF', 'GRSE', 'GARFIBRES', 'GODFRYPHLP', 'GRANULES', 'GRAPHITE',
                            'GESHIP', 'GREAVESCOT', 'GRINDWELL', 'GUJALKALI', 'FLUOROCHEM', 'GMDCLTD', 'GNFC', 'GPPL',
                            'GSFC', 'GULFOILLUB', 'HEG', 'HFCL', 'HATHWAY', 'HEIDELBERG', 'HERITGFOOD', 'HSCL',
                            'HIMATSEIDE', 'HINDCOPPER', 'ICRA', 'IDFC', 'IFBIND', 'IFCI', 'IIFL', 'IRB', 'IRCON', 'ITI',
                            'INDIACEM', 'ITDC', 'IBREALEST', 'INDIAMART', 'INDIANB', 'IEX', 'INDOSTAR', 'INDOCO',
                            'INFIBEAM', 'INGERRAND', 'INOXLEISUR', 'INTELLECT', 'JBCHEPHARM', 'JKLAKSHMI', 'JKPAPER',
                            'JKTYRE', 'JMFINANCIL', 'JAGRAN', 'JAICORPLTD', 'J&KBANK', 'JAMNAAUTO', 'JINDALSAW',
                            'JSLHISAR', 'JSL', 'JCHAC', 'JUSTDIAL', 'JYOTHYLAB', 'KPRMILL', 'KEI', 'KNRCON', 'KPITTECH',
                            'KRBL', 'KSB', 'KAJARIACER', 'KALPATPOWR', 'KTKBANK', 'KARURVYSYA', 'KSCL', 'KEC',
                            'KOLTEPATIL', 'LAOPALA', 'LAXMIMACH', 'LAURUSLABS', 'LEMONTREE', 'LINDEINDIA', 'LUXIND',
                            'MASFIN', 'MMTC', 'MOIL', 'MAHSCOOTER', 'MAHSEAMLES', 'MAHINDCIE', 'MHRIL', 'MAHLOG',
                            'METROPOLIS', 'MINDACORP', 'MIDHANI', 'MCX', 'NBCC', 'NCC', 'NESCO', 'NH', 'NFL',
                            'NBVENTURES', 'NAVINFLUOR', 'NILKAMAL', 'OMAXE', 'ORIENTCEM', 'ORIENTELEC', 'ORIENTREF',
                            'PNCINFRA', 'PTC', 'PVR', 'PERSISTENT', 'PHILIPCARB', 'POLYMED', 'PRAJIND', 'PRSMJOHNSN',
                            'PGHL', 'RITES', 'RADICO', 'RVNL', 'RAIN', 'RALLIS', 'RCF', 'RATNAMANI', 'RAYMOND',
                            'REDINGTON', 'REPCOHOME', 'SADBHAV', 'SCHNEIDER', 'SIS', 'SEQUENT', 'SFL', 'SCI',
                            'SHOPERSTOP', 'RENUKA', 'SOBHA', 'SONATSOFTW', 'SOUTHBANK', 'SPANDANA', 'SPICEJET',
                            'STARCEMENT', 'SWSOLAR', 'STRTECH', 'STAR', 'SUDARSCHEM', 'SPARC', 'SUNTECK', 'SUPRAJIT',
                            'SUZLON', 'SWANENERGY', 'TCIEXP', 'TCNSBRANDS', 'TVTODAY', 'TV18BRDCST', 'TAKE',
                            'TASTYBITE', 'TATAELXSI', 'TATAINVEST', 'TATASTLBSL', 'TEAMLEASE', 'THYROCARE',
                            'TIMETECHNO', 'TIMKEN', 'TRIDENT', 'TIINDIA', 'UFLEX', 'UJJIVAN', 'UJJIVANSFB', 'VMART',
                            'VIPIND', 'VRLLOG', 'VSTIND', 'VAIBHAVGBL', 'VAKRANGEE', 'VTL', 'VARROC', 'VENKEYS',
                            'VESUVIUS', 'WELCORP', 'WELSPUNIND', 'WESTLIFE', 'WOCKPHARMA', 'ZENSARTECH', 'ZYDUSWELL',
                            'ECLERX']
}

