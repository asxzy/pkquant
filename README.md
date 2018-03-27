# pkquant

see: https://github.com/ricequant/rqalpha


$ apt-get install -y python3 python3-dev python3-setuptools python3-pip 
$ aptitude install -y libagg-dev libpng libfreetype6 libqhull-dev
$ apt-get install libfreetype6-dev pkg-config libpng12-dev


$ mkdir ~/.pip/
$ vim ~/.pip/pip.conf
[global]
trusted-host =  mirrors.aliyun.com
index-url = http://mirrors.aliyun.com/pypi/simple

                     numpy: yes [not found. pip may install it below.]
          install_requires: yes [handled by setuptools]
                    libagg: yes [pkg-config information for 'libagg' could not
                            be found. Using local copy.]
                  freetype: no  [The C/C++ header for freetype2 (ft2build.h)
                            could not be found.  You may need to install the
                            development package.]
                       png: no  [pkg-config information for 'libpng' could not
                            be found.]
                     qhull: yes [pkg-config information for 'libqhull' could not
                            be found. Using local copy.]

$ pip3 install pyinstaller setuptools cython numpy

download  bcolz-x.x.x-cpxx-cpxxm-win_amd64.whl line_profiler-x.x.x-cpxx-cpxxm-win_amd64.whl wheel-0.30.0-py2.py3-none-any.whl
$ pip3 install bcolz-x.x.x-cpxx-cpxxm-win_amd64.whl line_profiler-x.x.x-cpxx-cpxxm-win_amd64.whl wheel-0.30.0-py2.py3-none-any.whl

$ pip3 install rqalpha
$ rqalpha mod install ctp
$ rqalpha mod enable ctp
$ vi ~/.rqalpha/mod_config.yml
mod:
  ctp: {
    enabled: true,
   # CTP 登录信息
    "login": {
        'user_id': "xxxxxx",
        'password': "xxxxxx",
        'broker_id': "9999",
    },
    # 事件相关设置
    "event": {
        # 是否使用默认的 CTP 实时数据源
        "enabled": True,
        # 是否在非交易时间段内触发行情事件
        "all_day": False,
        "address": "tcp://180.168.146.187:10010",
    },
    # 交易相关设置
    "trade": {
        # 是否使用默认的 CTP 交易接口
        "enabled": True,
        "address": "tcp://180.168.146.187:10000",
    },
  }


rqalpha run -rt p -fq 1m -f buy_and_hold.py --account future 10000 -mc ctp.enabled True