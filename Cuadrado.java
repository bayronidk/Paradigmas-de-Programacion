public class Cuadrado{
    private String color;
    private double lado;

    public Cuadrado(String color, double lado){
        this.color = color;
        this.lado = lado;
    }

    public String getColor(){
        return color;
    }

    public double getArea(){
        return area();
    }

    public double getPerimetro(){
        return perimetro();
    }

    private double area(){
        return lado * lado;
    }

    private double perimetro(){
        return 4 * lado;
    }

        public static void main(String[] args){
            Cuadrado cuadrado = new Cuadrado("Verde", 15.0);
            System.out.println("Color del cuadrado: " + cuadrado.getColor());
            System.out.println("Área del cuadrado: " + cuadrado.getArea());
            System.out.println("Perímetro del cuadrado: " + cuadrado.getPerimetro());
        }
    
}