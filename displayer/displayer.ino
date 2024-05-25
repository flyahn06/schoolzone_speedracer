// +--------------+--------------+-----------------------------------------------------------------+
// |    Author    |     Date     |                            Changed                              |
// +--------------+--------------+-----------------------------------------------------------------+
// |   flyahn06   |  2023/05/17  | Feat: implement digit displayer                                 |
// +-------------+--------------+------------------------------------------------------------------+

int A = 12;
int B = 8;
int DP  = 4;
int D = 6;
int E = 7;
int F = 11;
int G = 3;
int D1 = 13;
int D2 = 10;
int D3 = 9;
int D4 = 2;
int C = 5;

int pos = 0;
int digit = 0;

int current_digits[4] = {0, 0, 0, 0};

void initialize(int position) {
    switch(position) {
        case 0:
            digitalWrite(D1, HIGH);
            digitalWrite(D2, LOW);
            digitalWrite(D3, LOW);
            digitalWrite(D4, LOW);
            break;
        case 1:
            digitalWrite(D1, LOW);
            digitalWrite(D2, HIGH);
            digitalWrite(D3, LOW);
            digitalWrite(D4, LOW);
            break;
        case 2:
            digitalWrite(D1, LOW);
            digitalWrite(D2, LOW);
            digitalWrite(D3, HIGH);
            digitalWrite(D4, LOW);
            break;
        case 3:
            digitalWrite(D1, LOW);
            digitalWrite(D2, LOW);
            digitalWrite(D3, LOW);
            digitalWrite(D4, HIGH);
            break;
    }
}

void display(int position, int value) {
    // DP를 다룰 마땅한 방법이 없어서 -1로...
    initialize(position);
    digitalWrite(DP, HIGH);

    switch (value) {
        case -1:
            digitalWrite(DP, HIGH);
            break;
        case 0:
            digitalWrite(A, LOW);
            digitalWrite(B, LOW);
            digitalWrite(C, LOW);
            digitalWrite(D, LOW);
            digitalWrite(E, LOW);
            digitalWrite(F, LOW);
            digitalWrite(G, HIGH);
            break;
        case 1:
            digitalWrite(A, HIGH);
            digitalWrite(B, HIGH);
            digitalWrite(C, HIGH);
            digitalWrite(D, HIGH);
            digitalWrite(E, LOW);
            digitalWrite(F, LOW);
            digitalWrite(G, HIGH);
            break;
        case 2:
            digitalWrite(A, LOW);
            digitalWrite(B, LOW);
            digitalWrite(C, HIGH);
            digitalWrite(D, LOW);
            digitalWrite(E, LOW);
            digitalWrite(F, HIGH);
            digitalWrite(G, LOW);
            break;
        case 3:
            digitalWrite(A, LOW);
            digitalWrite(B, LOW);
            digitalWrite(C, LOW);
            digitalWrite(D, LOW);
            digitalWrite(E, HIGH);
            digitalWrite(F, HIGH);
            digitalWrite(G, LOW);
            break;
        case 4:
            digitalWrite(A, HIGH);
            digitalWrite(B, LOW);
            digitalWrite(C, LOW);
            digitalWrite(D, HIGH);
            digitalWrite(E, HIGH);
            digitalWrite(F, LOW);
            digitalWrite(G, LOW);
            break; 
        case 5:
            digitalWrite(A, LOW);   
            digitalWrite(B, HIGH);   
            digitalWrite(C, LOW);   
            digitalWrite(D, LOW);   
            digitalWrite(E, HIGH);   
            digitalWrite(F, LOW);   
            digitalWrite(G, LOW);    
            break;
        case 6:
            digitalWrite(A, LOW);
            digitalWrite(B, HIGH);
            digitalWrite(C, LOW);
            digitalWrite(D, LOW);
            digitalWrite(E, LOW);
            digitalWrite(F, LOW);
            digitalWrite(G, LOW);
            break;
        case 7:
            digitalWrite(A, LOW);
            digitalWrite(B, LOW);
            digitalWrite(C, LOW);
            digitalWrite(D, HIGH);
            digitalWrite(E, HIGH);
            digitalWrite(F, HIGH);
            digitalWrite(G, HIGH);
            break;
        case 8:
            digitalWrite(A, LOW);
            digitalWrite(B, LOW);
            digitalWrite(C, LOW);
            digitalWrite(D, LOW);
            digitalWrite(E, LOW);
            digitalWrite(F, LOW);
            digitalWrite(G, LOW);
            break;
        case 9:
            digitalWrite(A, LOW);
            digitalWrite(B, LOW);
            digitalWrite(C, LOW);
            digitalWrite(D, LOW);
            digitalWrite(E, HIGH);
            digitalWrite(F, LOW);
            digitalWrite(G, LOW);
            break;
    }
    delay(1);
}

void setup() {
    Serial.begin(9600);
    pinMode(A, OUTPUT);     
    pinMode(B,  OUTPUT);     
    pinMode(C, OUTPUT);     
    pinMode(D, OUTPUT);     
    pinMode(E, OUTPUT);     
    pinMode(F, OUTPUT);     
    pinMode(G,  OUTPUT);   
    pinMode(D1, OUTPUT);  
    pinMode(D2, OUTPUT);  
    pinMode(D3,  OUTPUT);  
    pinMode(D4, OUTPUT);  
    pinMode(DP, OUTPUT);
}

void loop() {
    if (!Serial.available()) {
        for (int i = 0; i < 4; i++) {
            display(i, current_digits[i]);
        }
        return;
    }
    
    int temp = Serial.parseInt();
    Serial.read();  // 개행 skip
    digit = temp % 10;
    pos = (temp - digit) / 10;
    pos--;

    current_digits[pos] = digit;
}