public class Hexagono{
    String color;
    double lado;
    double apotema;

    public Hexagono(String color, double lado, double apotema){
        this.color = color;
        this.lado = lado;
        this.apotema = apotema;
    }

    public double getArea() {
        return area();
    }

    public double getPerimetro() {
        return perimetro();
    }

    public String getColor() {
        return color;
    }

    private double perimetro(){
        return lado * 6;
    }

    private double area(){
        return ((lado*6) * apotema)/2;
    }

    public static void main(String[] args) {
        Hexagono hexagono = new Hexagono("Naranja", 6.0,5.0);
        System.out.println("Color del hexágono: " + hexagono.getColor());
        System.out.println("Área del hexágono: " + hexagono.getArea());
        System.out.println("Perímetro del hexágono: " + hexagono.getPerimetro());
    }

}