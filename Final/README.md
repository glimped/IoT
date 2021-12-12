These are the files for Ryan Lange's EE629 final project. 
Materials:
1x Raspberry Pi (I used 3B Model)
1x DHT22 Sensor
Cables
1x 10kΩ resistor



First and foremost, set up the circuit for a DHT22 sensor on your Raspberry Pi

![image](https://user-images.githubusercontent.com/53006579/145725288-2e44a265-50a2-4bb3-addc-9131c9e5e298.png)

Next run some standard updates

`sudo apt-get update
sudo apt-get upgrade
sudo pip3 install --upgrade setuptools`

We will be using `python3` and `pip3` for the code, so maike sure you have the Python3 packages installed

Then install the library for the DHT22 sensor, as well as the Adafruit IO library

`sudo pip3 install Adafruit_DHT
pip3 install adafruit-io`

Next create an account at [Adafruit IO](https://io.adafruit.com)
After your account is created, follow [this](https://learn.adafruit.com/adafruit-io-basics-temperature-and-humidity/adafruit-io-setup) guide to setup 
your Dashboard to receive the DHT22 sensor data. Additionally, it will guide you to your AIO Key, which you will need to update along with your username 
in the temp_humidity.py file.

Based on your preference, you can also create a folder to store the data and python file

`mkdir GardEx
cd GardEx`

Inside the new folder clone the Python file

`wget https://raw.githubusercontent.com/glimped/IoT/main/Final/temp_humidity.py`

Then edit the file to include YOUR_IO_KEY and YOUR_IO_USERNAME with their actual values

`nano temp_humidity.py`

To run the file, enter the following

`python3 temp_humidity.py`

And check your Adafruit IO dashboard and you should see your sensor data updating every 10 seconds
