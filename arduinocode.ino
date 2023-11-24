void setup() {
  Serial.begin(9600);
}
void turnOnMicrowave() {
  //Suppose that the microwave is connected to pin 6 on arduino
  digitalWrite(6, HIGH);
  delay(1000);  // Delay for 1 second
  digitalWrite(6, LOW);
}
void loop() {
  if (Serial.available()) {
    // Reading the incoming JSON signal
    StaticJsonDocument<100> doc;
    DeserializationError error = deserializeJson(doc, Serial);
    if (error) {
      Serial.print("Error parsing JSON: ");
      Serial.println(error.c_str());
      return;
    }
    // Check if the signal is for turning on the microwave
    String action = doc["action"];
    if (action == "turn_on") {
      // Get the delay time
      int delayTime = doc["delay"];
      // Wait for the specified delay time
      delay(delayTime * 1000);
      turnOnMicrowave();
    }
  }
}
