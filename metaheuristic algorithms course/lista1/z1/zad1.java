
import java.util.Random;
import java.util.concurrent.TimeUnit;
import java.util.*;


/* Wojciech Wroblewski algorytmy metaheurystyczne zad1  lista1 */
public class zad1 {


    /*local search*/
    public static void findMinima(String function, int time){

            // generujemy losowy wektor z zekresu
            double minima[]=generateRandomVector();
            double vector[]= new double[4];
            //sasiedztwem przeszukiwania lokalnego jest sfera o zmiennym promieniu
            double radious;
            time=time*1000;
            double end =System.currentTimeMillis()+time;

            switch (function){

                case "0":
                    while(System.currentTimeMillis()<=end){
                        
            //generujemy  punkt w sasiedztwie i sprawdzamy czy jest kandydatem
                         radious =Math.random();
                        vector=generatePointOnSphere(radious,minima);
                        if(functionHappyCat(vector)<functionHappyCat(minima)){
                            minima=vector;
                        }
                        else
                            continue;
                    }
                        System.out.println(minima[0]+" "+minima[1]+" "+minima[2]+" "+minima[3]+" "+functionHappyCat(minima));
             
                    break;
                default:
                    while(System.currentTimeMillis()<=end){

                        radious =Math.random(); 
                        vector=generatePointOnSphere(radious,minima);
                        if(functionGriewank(vector)<functionGriewank(minima)){
                            minima=vector;
                            
                            
                        }
                        else
                            continue;
                    }
               
                    System.out.println(minima[0]+" "+minima[1]+" "+minima[2]+" "+minima[3]+" "+functionGriewank(minima));
                    break;
            }
    }

    public static double distance(double vector[],double randomVector[]) {


        return  Math.pow(Math.pow(vector[0]-randomVector[0],2)+
                        +Math.pow(vector[1]-randomVector[1],2)+
                        +Math.pow(vector[2]-randomVector[2],2)+
                        +Math.pow(vector[3]-randomVector[3],2),0.5);
    }
    //zwraca wspolrzedna o typie double z zakresu
    public static double cor() {
        double start = -5;
        double end = 5;
        double random = new Random().nextDouble();
        double result = start + (random * (end - start));
        return  result;
    }

    //generowanie punktu na sferze sasiedztwa
    public static double[] generatePointOnSphere(double radious,double[] minimum) {
        double random1 = new Random().nextDouble();
        double random2 = new Random().nextDouble();
       // double random3 = new Random().nextDouble();
       // double random4 = new Random().nextDouble();

        double start=-1;double end = 1;
        double result1 = start + (random2* (end - start));
        double result2 = start + (random1 * (end - start));
        double result3 = start + (random1 * (end - start));
        double result4 = start + (random1 * (end - start));

        double vector[]={result1,result2,result3,result4};
        double temp=0;
        while(temp ==0){

            temp=Math.sqrt(Math.pow(vector[0]-minimum[0],2)+Math.pow(vector[1]-minimum[1],2)+Math.pow(vector[2]-minimum[2],2)+Math.pow(vector[3]-minimum[3],2));
        }

        temp = 1.0/temp;

        for(int i=0;i<4;i++){
            vector[i]=vector[i]*radious*temp;
        }
        return  vector;
    }

    public static double[] generateRandomVector(){
        double vector[]= new double[4];

        for (int i=0;i<vector.length;i++){
            vector[i]=cor();
        }
        return vector;
    }


    public static void print(double[] vector,double min){

        for(int k=0;k<vector.length;k++){
            System.out.println(vector[k]);
        }
        System.out.println(min);


    }
    public static double  functionHappyCat(double  vector[]){

        return Math.pow(Math.pow(Math.pow(vector[0],2.0)+Math.pow(vector[1],2.0)+Math.pow(vector[2],2.0)+Math.pow(vector[3],2.0)- 4,2.0),(1.0/8.0)) +
                + 0.25*(0.5*(Math.pow(vector[0],2.0)+Math.pow(vector[1],2.0)+Math.pow(vector[2],2)+Math.pow(vector[3],2))+
                        +vector[0]+vector[1]+vector[2]+vector[3])+0.5 ;
    }
    
    public static double functionGriewank(double vector[]){

        return 1+(Math.pow(vector[0],2)+Math.pow(vector[1],2)+Math.pow(vector[2],2)+Math.pow(vector[3],2))/4000.0-(Math.cos(vector[0]/1) * Math.cos(vector[1]/Math.sqrt(2)) * Math.cos(vector[2]/Math.sqrt(3)) * Math.cos(vector[3]/Math.sqrt(2)));
    }

  
    public static int time;
    public static String function;
    public  static void main(String[] args) {
       
      Scanner scanner = new Scanner(System.in);
       time = scanner.nextInt();
       function = scanner.next();
       scanner.close();
      
      
       findMinima(function,time);
    
       
            
    }
}
