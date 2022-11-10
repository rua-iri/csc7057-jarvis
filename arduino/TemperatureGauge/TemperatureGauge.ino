
const int sensorPin = A0;
const float baselineTemp = 20.0;

//delcare the sensor value, voltage and
//temperature before they are used
int sensorVal, temp_count;
int max_count = 1000;
float voltage, temperature, total_temp;

void setup() {
  Serial.begin(9600);
  temp_count = 0;

  while(!Serial) {
    
  }
}

void loop() {
  //read sensor value and convert it to celsius
  sensorVal = analogRead(sensorPin);
  temperature = (((sensorVal / 1024.0) * 5.0) - 0.5) * 100;
  
  //add temperature up to total_temp and increment temp_count
  total_temp += temperature;
  temp_count++;

  //calculate average over many measurements
  //this makes readings much more reliable
  if (temp_count==max_count) {
    Serial.println(total_temp/temp_count);
    temp_count = 0;
    total_temp = 0;
  }
  
}
