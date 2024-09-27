int data = 2; 
// se 1, N-S abre, se 2, L-O abre.

int semaforoNorteSul = 2; // Pino para controlar semáforo Norte-Sulsemana 
int semaforoRedNS = 1;

int semaforoLesteOeste = 4; // Pino para controlar semáforo Leste-Oeste
int semaforoRedLO = 3;

void setup() {
  // Configurar os pinos de saída para os semáforos
  pinMode(semaforoNorteSul, OUTPUT); // Norte-Sul
  pinMode(semaforoLesteOeste, OUTPUT); // Leste-Oeste
  pinMode(semaforoRedNS, OUTPUT);
  pinMode(semaforoRedLO, OUTPUT);
}

void loop() {

  if (data == 1) {
      digitalWrite(semaforoNorteSul, HIGH);  // Abrir semáforo Norte-Sul
      digitalWrite(semaforoRedNS, LOW);
      digitalWrite(semaforoLesteOeste, LOW); // Fechar semáforo Leste-Oeste
      digitalWrite(semaforoRedLO, HIGH);
    
  } 
  else if (data == 2) {
      digitalWrite(semaforoNorteSul, LOW);   // Fechar semáforo Norte-Sul
      digitalWrite(semaforoRedNS, HIGH);
      digitalWrite(semaforoLesteOeste, HIGH);// Abrir semáforo Leste-Oeste
      digitalWrite(semaforoRedLO, LOW);
  }
}
