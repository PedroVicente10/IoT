   double alpha=0.75;
   int period=20;
   double refresh=0.0;

void setup(void)
{
  Serial.begin(9600);
  pinMode(A0,INPUT);
}

void loop(void)
{

   static double oldValue=0;
   static double oldrefresh=0;

   int beat=analogRead(A0);

   double value=alpha*oldValue+(0-alpha)*beat;
   refresh=value-oldValue;

   Serial.print(" Heart Monitor "); 
   Serial.print("          ");
   Serial.println(beat/10);

   oldValue=value;
   oldrefresh=refresh;
   delay(period*10);

}
