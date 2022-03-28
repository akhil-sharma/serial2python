long randomNumber;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  randomSeed(1000);
}

void loop() {
  //
  char message_stream_code[] = "6240fd80e4440ac4daa4fb6e";
  char message_text[] = "This is a sample message text sent from arduino.";
  
  Serial.print(message_text);
  Serial.print("#");
  Serial.println(message_stream_code);
  delay(10000);
}
