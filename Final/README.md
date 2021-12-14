These are the files for Ryan Lange's EE629 final project. 


## Temperature & Humidity

Materials:

1x Raspberry Pi (I used 3B Model)

1x DHT22 Sensor

Cables

1x 10kΩ resistor




First and foremost, set up the circuit for a DHT22 sensor on your Raspberry Pi

![image](https://user-images.githubusercontent.com/53006579/145725288-2e44a265-50a2-4bb3-addc-9131c9e5e298.png)

Next run some standard updates

`sudo apt-get update`
`sudo apt-get upgrade`
`sudo pip3 install --upgrade setuptools`


We will be using `python3` and `pip3` for the code, so maike sure you have the Python3 packages installed


Then install the library for the DHT22 sensor, as well as the Adafruit IO library

`sudo pip3 install Adafruit_DHT

pip3 install adafruit-io`


Next create an account at [Adafruit IO](https://io.adafruit.com)
After your account is created, navigate to your dashboards and find the My Key tab above your dashboards. Take a note of the active AIO key, since you'll need it later for updating the temp_humidity.py script. Next find the Feeds tab, click it, and then click view all to view the Feeds page. Here you'll create two new feeds by clicking New Feed and naming one Temperature and one Humidity. No description is required. 

Then click back to the Dashboard page, and on the dashboard page click Create Dashboard and name it whatever you please. Once created, click into the dashboard and find the gear icon towards the top right. Click the gear, then find and click the line chart. Check the boxes to include the Temperature and Humidity feeds you created and click Next Step. Keep everything the same and optionally title the block and hit create block. Once the Python script is edited with your Adafruit info and the code is running, the data from the sensors will automatically be sent to your dashboard and displayed graphically in the block.


You can also create a folder to store Python file if you wish

`mkdir GardEx

cd GardEx`


Inside the new folder clone the Python file

`wget https://raw.githubusercontent.com/glimped/IoT/main/Final/temp_humidity.py`


Then edit the file to include your active IO key and Adafruit IO username, overwriting the sections that say YOUR_IO_KEY and YOUR_IO_USERNAME 

`nano temp_humidity.py`


To run the file, enter the following

`python3 temp_humidity.py`


And check your Adafruit IO dashboard and you should see your sensor data updating every 10 seconds




## GA1A12S202 Analog Light Sensor

Materials

1x Arduino Uno with cables

1x GA1A12S202 Analog Light Sensor

Jumper cables



This part of the project is only available on an Arduino microcontroller. To start, connect your light sensor to the Arduino Uno by either directly connecting them or connecting them via a breadboard as seen in the two photos below

![image](https://user-images.githubusercontent.com/53006579/146092549-bc2f63f0-8a3b-4987-8566-4ecacd52a668.png)


![image](https://user-images.githubusercontent.com/53006579/146092567-6cc7ede4-1804-4b36-8974-6379c4103a59.png)



Next connect your Arduino Uno to your computer. Then download and install the [Arduino IDE](https://www.arduino.cc/en/software), as well as the [libraries for the light sensor](https://github.com/arduinolearning/Arduino-Libraries/tree/master/GA1A12S202)

After installing the IDE, download the GA1A12S202 folder from the linked GitHub and copy the files into the libraries folder in your Arduino IDE installation folder. 

Next download the Light_Sensor script and open it in the Arduino IDE. Once in the IDE, click the tools tab at the top left and select the port associated with your Arduino Uno, it should tell you which port is connceted to the Uno. Once that's done, click the upload button at the top left next to the verify button that looks like a checkmark. After the code is successfully uploaded to the Uno, open the Serial Monitor by clicking the magnifying glass icon at the top right. The Serial Monitor will display raw and Lux values based on how much light it's receiving. It should look like the screenshot below.



![Screenshot (315)](https://user-images.githubusercontent.com/53006579/146093958-a1f2c702-0605-4da6-86b2-bae13fed39eb.png)
