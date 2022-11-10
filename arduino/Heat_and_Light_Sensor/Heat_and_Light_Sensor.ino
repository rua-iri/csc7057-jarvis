//Declare all the variables to be used later
const int heatSensPin = A0;
const int lightSensPin = A1;

int heatSensVal, lightSensVal;
int sensorCount = 0;
int maxCount = 1000;
float temperature;
float totalTemp = 0;
long totalLight = 0;

String dataString;


void setup() {
  Serial.begin(9600);

  while(!Serial) {
    
  }

}

void loop() {
  //Measure the reading from both sensors
  heatSensVal = analogRead(heatSensPin);
  lightSensVal = analogRead(lightSensPin);

  //convert the sensor reading to a celsius value
  temperature = (((heatSensVal / 1024.0) * 5.0) - 0.5) * 100;

  //add these values to their respective totals and increment the counter
  totalTemp += temperature;
  totalLight += lightSensVal;
  sensorCount ++;


  //print the averages if a limit has been met
  if (sensorCount==maxCount) {
    //convert the values to string and concatenate them
    dataString = String((totalTemp/sensorCount)) + "," + String((totalLight/sensorCount));
    Serial.println(dataString);

    //reset the variables
    totalTemp = 0;
    totalLight = 0;
    sensorCount = 0;
  }

//  delay(1);
  

}
