long randomNumber;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  randomSeed(1000);
}

void loop() {
  //
  char name[] = "akhil";
  // repeatedly send some information to the serial port
  randomNumber = random(1, 26);
  Serial.print(randomNumber);
  Serial.print(" ");
  Serial.println(name);
  delay(10000);
}
