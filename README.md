# Pahe Bypasser

A buggy method to automate link grabbing from pahe (It is what it is)

## Usage

```python
python main.py

Enter the pahe url: https://pahe.abcd/xyz
```

## Require
```
1. Google Chrome or Chromium Browser (Latest)
   https://www.chromium.org/getting-involved/download-chromium/
   
2. ChromeDriver (Latest) 
   https://chromedriver.chromium.org/
``` 

## NOTE
```
  For ARM Linux, grab chromedriver for arm64 linux from
  https://github.com/electron/electron/releases
  
  Make sure you have changed the path of chromedriver accordingly in settings.py
  
  The script currently has a sequential flow and parallel execution flow ( Using MultiProcessing ) . 
  Use the optimal one for your use case [ read main.py ]
```
