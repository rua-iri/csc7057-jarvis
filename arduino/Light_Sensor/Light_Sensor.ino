
const int lightSensPin = A1;

int lightSensVal = 0;
int lightCount = 0;
long totalLight = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  
  while(!Serial) {
    
  }

}



void loop() {
  // put your main code here, to run repeatedly:
  lightSensVal = analogRead(lightSensPin);
  
  totalLight += lightSensVal;
  lightCount++;

  
  if(lightCount==500) {
    Serial.println(totalLight/lightCount);
    String someString = String(totalLight) + " / " + String(lightCount) + "\n";
    Serial.println(someString);
    totalLight = 0;
    lightCount = 0;
  }

  delay(1);
}
