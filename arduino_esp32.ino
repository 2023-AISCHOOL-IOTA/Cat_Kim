#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <WiFi.h>

// Wi-Fi 설정
const char* ssid = "www";     // 여기에 Wi-Fi SSID 입력
const char* password = "ya201022"; // 여기에 Wi-Fi 비밀번호 입력

// 릴레이 모듈
const int relayPin = 23;  // 릴레이 제어용 디지털 핀 (IO23 핀)

// LCD2004 설정
LiquidCrystal_I2C lcd(0x27, 20, 4);  // 주소, 열 수, 행 수

// DHT11 센서 설정
#define DHTPIN 5          // D1 R32 보드의 IO5 핀
#define DHTTYPE DHT11     // DHT11 센서 타입
DHT dht(DHTPIN, DHTTYPE);

// DS18B20 센서 설정
const int oneWireBus = 18;  // 예시로 18번 핀을 사용
OneWire oneWire(oneWireBus);
DallasTemperature sensors(&oneWire);

// XKC-Y25-NPN 센서 설정
const int sensorPin = 19;  // XKC-Y25-NPN 센서의 디지털 출력이 연결된 핀 번호 (D19 핀)

WiFiServer server(80);  // 웹 서버 포트 설정

void setup() {
  pinMode(relayPin, OUTPUT);
  pinMode(sensorPin, INPUT);
  
  Serial.begin(9600);

  // Wi-Fi 연결
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.println("IP address: ");

  Serial.println(WiFi.localIP()); 
  
  lcd.init();
  lcd.backlight();
 
  dht.begin();
  sensors.begin();
  
  server.begin();  // 웹 서버 시작
}

void loop() {
  // DHT11 센서 읽기
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  if (!isnan(humidity) && !isnan(temperature)) {
    lcd.setCursor(0, 1);
    lcd.print("Humidity: ");
    lcd.print(static_cast<int>(humidity));
    lcd.print("%");
    lcd.setCursor(0, 2);
    lcd.print("Temp : ");
    lcd.print(static_cast<int>(temperature));
    lcd.print("C");
  }
  delay(2000);
  
  // DS18B20 센서 읽기
  sensors.requestTemperatures();
  float temperatureC = sensors.getTempCByIndex(0);
  float temperatureF = sensors.toFahrenheit(temperatureC);
  lcd.setCursor(0, 3);
  lcd.print("Temp : ");
  lcd.print(static_cast<int>(temperatureC));
  lcd.print("C");
  delay(1000);
  
  // XKC-Y25-NPN 센서 읽기
  int sensorValue = digitalRead(sensorPin);
  lcd.setCursor(-10, 4);
  lcd.print("Water Level: ");
  lcd.print(sensorValue == HIGH ? "Yes" : "No");
  delay(1000);

  // DS18B20 센서 값에 따른 릴레이 제어
  if (static_cast<int>(temperatureC) >= 25) {
    digitalWrite(relayPin, HIGH);
  } else if (static_cast<int>(temperatureC) >= 28) {
    digitalWrite(relayPin, LOW);
  }
  
  // 클라이언트 요청 처리
  WiFiClient client = server.available();
  if (client) {
    String response = "<html><body>";
    response += "<h1>Sensor Data</h1>";
    response += "<p>Humidity: " + String(static_cast<int>(humidity)) + "%</p>";
    response += "<p>Temperature: " + String(static_cast<int>(temperature)) + "C</p>";
    response += "<p>DS18B20 Temperature: " + String(static_cast<int>(temperatureC)) + "C</p>";
    response += "<p>Water Level: ";
    response += (sensorValue == HIGH ? "Yes" : "No");
    response += "</p>";
    response += "</body></html>";
    
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println("Connection: close");
    client.println();
    client.println(response);
    
    delay(10);
    client.stop();
  }
}
