#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <DHT.h>
#include <SoftwareSerial.h>

// DHT11 센서 (디지털 2번 핀에 연결)
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// DS18B20 센서
#define ONE_WIRE_BUS 3
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

// XKC-Y25-NPN 센서
const int sensorPin = 4;

// 1채널 릴레이 모듈 (디지털 7번 핀에 연결)
const int relayPin = 7;

// 2004 LCD 디스플레이 (I2C 통신)
LiquidCrystal_I2C lcd(0x27, 20, 4);

// 블루투스 통신 모듈 (디지털 6번 핀 - RX, 디지털 5번 핀 - TX)
SoftwareSerial bluetooth(6, 5);

void setup() {
  Serial.begin(9600);
  bluetooth.begin(9600);

  // DHT11 센서 초기화
  dht.begin();

  // DS18B20 센서 초기화
  sensors.begin();

  // XKC-Y25-NPN 센서 초기화
  pinMode(sensorPin, INPUT);

  // 1채널 릴레이 모듈 초기화
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW); // 초기 상태로 릴레이를 꺼둡니다.

  // 2004 LCD 디스플레이 초기화
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Welcome to Arduino!");
  lcd.setCursor(1, 1);
  lcd.print("2004 CLCD TEST");
  lcd.setCursor(2, 2);
  lcd.print("Hello Domeakit");
  lcd.setCursor(3, 3);
  lcd.print("4Line Display");
}

void loop() {
  // 블루투스 모듈로부터 데이터 수신
  if (bluetooth.available()) {
    char data = bluetooth.read();
    Serial.print("Received from Bluetooth: ");
    Serial.println(data);
  }

  // DHT11(온습도) 센서로부터 온습도 값 읽어오기
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // DS18B20(수중온도센서) 센서로부터 온도 값 읽어오기
  sensors.requestTemperatures();
  float temperatureC = sensors.getTempCByIndex(0);
    // 온도 값들을 int로 변환하여 저장
  int t_int = static_cast<int>(t);
  int temperatureC_int = static_cast<int>(temperatureC);

  // XKC-Y25-NPN(비접촉 수위센서) 센서 값 읽기
  int sensorValue = digitalRead(sensorPin);

  // 수온이 25도 이하인 경우 릴레이를 켜둡니다.
  if (temperatureC <= 25) {
    digitalWrite(relayPin, HIGH);
  }
  // 수온이 28도 이상이 되면 릴레이를 끕니다.
  else if (temperatureC >= 28) {
    digitalWrite(relayPin, LOW);
  }
  // (이전 코드 유지)

  // LCD 디스플레이에 정보 표시
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Humidity: ");
  lcd.print(static_cast<int>(h)); // 습도 값을 반올림하여 정수로 변환하여 출력
  lcd.print(" %");
  lcd.setCursor(1, 1);
  lcd.print("Temperature(DHT11): ");
  lcd.print(t_int);
  lcd.print(" °C");
  lcd.setCursor(2, 2);
  lcd.print("Temperature(DS18B20): ");
  lcd.print(temperatureC_int);
  lcd.print(" °C");
  lcd.setCursor(3, 3);
  lcd.print("Water Detected: ");
  lcd.print(sensorValue == HIGH ? "Yes" : "No");

  // 시리얼 모니터에 정보 출력
  Serial.print("Humidity: ");
  Serial.print(static_cast<int>(h)); // 습도 값을 반올림하여 정수로 변환하여 출력
  Serial.print(" %\t");
  Serial.print("Temperature(DHT11): ");
  Serial.print(t_int);
  Serial.print(" °C\t");
  Serial.print("Temperature(DS18B20): ");
  Serial.print(temperatureC_int);
  Serial.print(" °C\t");
  Serial.print("Water Detected: ");
  Serial.println(sensorValue == HIGH ? "Yes" : "No");

  delay(5000); // 5초마다 데이터 업데이트
}