// Smart Light Controlling Using Sound
// Components: Arduino Uno, KY-038 Sound Sensor, Relay Module

const int soundSensor = A0;   // Sound sensor connected to A0
const int relayPin = 5;       // Relay connected to digital pin 5

int threshold = 500;          // Sound threshold value
bool lightState = false;      // Light state

void setup() {
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW);
  Serial.begin(9600);
}

void loop() {

  int soundValue = analogRead(soundSensor);
  Serial.println(soundValue);

  // Detect clap (sound above threshold)
  if (soundValue > threshold) {

    lightState = !lightState;  // Toggle light state

    if (lightState) {
      digitalWrite(relayPin, HIGH);
      Serial.println("Light ON");
    } else {
      digitalWrite(relayPin, LOW);
      Serial.println("Light OFF");
    }

    delay(500); // debounce delay to avoid multiple triggers
  }

}
