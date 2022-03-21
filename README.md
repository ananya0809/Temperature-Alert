#### Temperature Alert and Prediction Model

Hardware Requirements: 
1. Microcontroller
2. Temperature Sensor
3. Male and Female Wires

Software Requirements:
1. Python3
2. Javascript
3. Cloud Interface(optional)
4. Twilio
5. Mailgun/SMTP
6. Telegram Account

Sending Alerts:
- Edit the ```sampleconf.py``` file with API keys, Device ID, email ID, Auth_Token, SSID, etc
- link the configuration file to code in order to connect though API keys
- Run code to test custom alert messages sent across email, SMS and via telegram
- Add a threshold value to receive alerts in case the Temperature crosses the value

Temperature Prediction:
1. **Prediction points:** This number tells the Visualizer how many future data points need to be predicted. By default, the Visualizer spaces the points with the data collection time in the hardware configuration of the product. So if you set the product to collect data every 5 minutes, and select 6 prediction points, the Visualizer will predict the trend and show 6 points up to 30 minutes into the future.

2. **No. Polynomial coefficients:** Polynomial Visualizer processes the given input time-dependent data, and outputs the coefficients of the function of the form:
which most closely resembles the trend in the input data. This number tells the Visualizer how many elements should be present in the function i.e. the value of n.
![img.png](img.png)
3. **Frame Size:** These are the number of previous data points the Visualizer will use to predict the trend of the data. For example, if you set this value to 5, the Visualizer will use the previous 5 points to predict the trend.

![img_1.png](img_1.png)