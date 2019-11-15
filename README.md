# chrome cast CLI
デスクトップをChromecastでミラーリングする

# Requirements
+ python 3.x
+ Google Chrome
+ chromedriver
  + Google Chrome のバージョンと同じものを選ぶ
  + https://chromedriver.chromium.org/downloads

# Install
1. clone
```
$ git clone 
```

2. install
```
$ pipenv install

or

$ pip install -r reqiurements.txt 
```

# Settings
+ CHROME_PROFILE_PATH: /path/to/profile
  + Chromeで `chrome://version` にアクセスすると確認できる
+ CHROME_DRIVER_PATH: /path/to/chromedriver

# Cast your desktop
```
$ pipenv run python main.py DEVICE_NAME

or

$ python3 main.py DEVICE_NAME
```